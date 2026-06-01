"""
Web Dashboard Server - aiohttp based

Provides REST API and dashboard HTML for monitoring the trading bot.
"""

import asyncio
import json
import logging
import os
import time
from pathlib import Path
from typing import Any

from aiohttp import web

logger = logging.getLogger(__name__)

_bot = None
_start_time = time.time()


def _json_serial(obj: Any) -> Any:
    if hasattr(obj, "isoformat"):
        return obj.isoformat()
    return str(obj)


def _safe(obj, attr, default=None):
    try:
        return getattr(obj, attr, default)
    except Exception:
        return default


# === API ===

async def api_status(request):
    bot = _bot
    if not bot:
        return web.json_response({"error": "not ready"}, status=503)
    next_cycle = None
    if hasattr(bot, "scheduler") and bot.scheduler:
        try:
            next_cycle = bot.scheduler.get_next_cycle_seconds()
        except Exception:
            pass
    total_trades = 0
    daily_pnl = 0.0
    try:
        from alpha_trading_bot.core.state_persistence import StatePersistence
        sp = StatePersistence()
        st = sp.load_state()
        total_trades = _safe(st, "total_trades", 0)
        daily_pnl = _safe(st, "daily_pnl", 0.0)
    except Exception:
        pass
    return web.json_response({
        "running": _safe(bot, "_running", False),
        "initialized": _safe(bot, "_initialized", False),
        "test_mode": _safe(bot.config.trading, "test_mode", True) if bot.config and bot.config.trading else True,
        "symbol": _safe(bot.config.exchange, "symbol", "") if bot.config and bot.config.exchange else "",
        "leverage": _safe(bot.config.exchange, "leverage", 0) if bot.config and bot.config.exchange else 0,
        "next_cycle_seconds": next_cycle,
        "total_trades": total_trades,
        "daily_pnl": round(daily_pnl, 2),
        "uptime_seconds": int(time.time() - _start_time),
    }, dumps=lambda o: json.dumps(o, default=_json_serial))


async def api_market(request):
    bot = _bot
    if not bot or not _safe(bot, "_exchange"):
        return web.json_response({"error": "exchange not connected"}, status=503)
    try:
        md = await bot._exchange.get_market_data()
        return web.json_response({
            "price": md.get("price", 0),
            "high": md.get("high", 0),
            "low": md.get("low", 0),
            "change_percent": md.get("change_percent", 0),
            "technical": md.get("technical", {}),
        }, dumps=lambda o: json.dumps(o, default=_json_serial))
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)


async def api_position(request):
    bot = _bot
    if not bot:
        return web.json_response({"has_position": False})
    try:
        pm = _safe(bot, "position_manager")
        if not pm:
            return web.json_response({"has_position": False})
        has = pm.has_position()
        ctx = None
        if has and bot._exchange:
            try:
                md = await bot._exchange.get_market_data()
                ctx = pm.get_position_context(md.get("price", 0))
            except Exception:
                pass
        return web.json_response({"has_position": has, "context": ctx},
                                 dumps=lambda o: json.dumps(o, default=_json_serial))
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)


async def api_signals(request):
    try:
        from alpha_trading_bot.ai.client import get_signal_distribution
        dist = await get_signal_distribution()
        return web.json_response({"distribution": dist, "timestamp": time.time()},
                                 dumps=lambda o: json.dumps(o, default=_json_serial))
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)


async def api_trades(request):
    try:
        from alpha_trading_bot.core.state_persistence import StatePersistence
        sp = StatePersistence()
        limit = int(request.query.get("limit", "50"))
        trades = sp.get_recent_trades(limit=limit)
        return web.json_response({"trades": trades, "count": len(trades)},
                                 dumps=lambda o: json.dumps(o, default=_json_serial))
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)


async def api_config(request):
    bot = _bot
    if not bot or not bot.config:
        return web.json_response({"error": "config not loaded"}, status=503)
    c = bot.config
    return web.json_response({
        "ai_mode": _safe(c.ai, "mode", "?"),
        "ai_provider": _safe(c.ai, "default_provider", "?"),
        "investment_type": os.getenv("INVESTMENT_TYPE", "moderate"),
        "stop_loss_percent": _safe(c.stop_loss, "stop_loss_percent", 0),
        "take_profit_percent": _safe(c.stop_loss, "take_profit_percent", 0),
        "cycle_minutes": _safe(c.trading, "cycle_minutes", 15),
        "smart_tp_sl": os.getenv("SMART_TP_SL_ENABLED", "false").lower() == "true",
        "trailing_stop": os.getenv("TRAILING_STOP_ENABLED", "false").lower() == "true",
    }, dumps=lambda o: json.dumps(o, default=_json_serial))


async def index_handler(request):
    html = Path(__file__).parent / "templates" / "index.html"
    if html.exists():
        return web.FileResponse(html)
    return web.Response(text="Dashboard not found", status=404)


def create_app(bot=None):
    global _bot
    _bot = bot
    app = web.Application()
    app.router.add_get("/api/status", api_status)
    app.router.add_get("/api/market", api_market)
    app.router.add_get("/api/position", api_position)
    app.router.add_get("/api/signals", api_signals)
    app.router.add_get("/api/trades", api_trades)
    app.router.add_get("/api/config", api_config)
    app.router.add_get("/", index_handler)
    return app


async def start_web_server(bot, host="0.0.0.0", port=8501):
    app = create_app(bot)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()
    logger.info(f"[Web] Dashboard: http://localhost:{port}")
    print(f"\n  Dashboard: http://localhost:{port}\n")
    while True:
        await asyncio.sleep(3600)

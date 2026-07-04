#!/usr/bin/env python3
"""交易约束层单元测试。"""

from modules.indicators import DailyData
from modules.simulator.execution_constraints import (
    TradeConstraints,
    get_trade_constraints,
    is_price_limit_hit,
    next_trading_date,
)


def test_main_board_price_limit():
    prev = DailyData(
        ts_code="000001.SZ",
        trade_date="20240101",
        open=10,
        high=11,
        low=9,
        close=10,
        vol=1000,
        amount=10000,
        pct_chg=0,
    )
    kline = DailyData(
        ts_code="000001.SZ",
        trade_date="20240102",
        open=11.1,
        high=11.1,
        low=11.0,
        close=11.0,
        vol=1000,
        amount=10000,
        pct_chg=10,
    )
    c = get_trade_constraints("000001.SZ", kline, prev)
    assert c.can_buy is False
    assert "涨停" in c.reason


def test_kcb_20pct_limit():
    prev = DailyData(
        ts_code="688001.SH",
        trade_date="20240101",
        open=10,
        high=11,
        low=9,
        close=10,
        vol=1000,
        amount=10000,
        pct_chg=0,
    )
    kline = DailyData(
        ts_code="688001.SH",
        trade_date="20240102",
        open=12.1,
        high=12.1,
        low=12.0,
        close=12.0,
        vol=1000,
        amount=10000,
        pct_chg=20,
    )
    c = get_trade_constraints("688001.SH", kline, prev)
    assert c.can_buy is False


def test_st_filter_and_5pct():
    prev = DailyData(
        ts_code="000002.SZ",
        trade_date="20240101",
        open=5,
        high=5.5,
        low=4.5,
        close=5,
        vol=1000,
        amount=10000,
        pct_chg=0,
    )
    kline = DailyData(
        ts_code="000002.SZ",
        trade_date="20240102",
        open=5.26,
        high=5.26,
        low=5.25,
        close=5.25,
        vol=1000,
        amount=10000,
        pct_chg=5,
    )
    c = get_trade_constraints("000002.SZ", kline, prev, name="*ST 测试", allow_st=False)
    assert c.is_st is True
    assert c.can_buy is False


def test_halted_stock():
    prev = DailyData(
        ts_code="000003.SZ",
        trade_date="20240101",
        open=10,
        high=10,
        low=10,
        close=10,
        vol=1000,
        amount=10000,
        pct_chg=0,
    )
    kline = DailyData(
        ts_code="000003.SZ",
        trade_date="20240102",
        open=10,
        high=10,
        low=10,
        close=10,
        vol=0,
        amount=0,
        pct_chg=0,
    )
    c = get_trade_constraints("000003.SZ", kline, prev)
    assert c.is_halted is True
    assert c.can_sell is False


def test_trade_constraints_dataclass_defaults():
    c = TradeConstraints(can_buy=True, can_sell=True, reason="正常交易")
    assert c.price_limit is None
    assert c.price_floor is None
    assert c.is_st is False
    assert c.is_halted is False


def test_next_trading_date_basic():
    dates = ["20240101", "20240102", "20240103"]
    assert next_trading_date(dates, "20240101") == "20240102"
    assert next_trading_date(dates, "20240102") == "20240103"
    assert next_trading_date(dates, "20240103") == ""


def test_is_price_limit_hit_main_board():
    kline = DailyData(
        ts_code="000001.SZ",
        trade_date="20240102",
        open=11.0,
        high=11.1,
        low=11.0,
        close=11.0,
        vol=1000,
        amount=10000,
        pct_chg=10,
    )
    hit, reason = is_price_limit_hit(kline, prev_close=10.0, ts_code="000001.SZ")
    assert hit is True
    assert "涨停" in reason


def test_is_price_limit_hit_kcb_20pct():
    kline = DailyData(
        ts_code="688001.SH",
        trade_date="20240102",
        open=12.0,
        high=12.1,
        low=12.0,
        close=12.0,
        vol=1000,
        amount=10000,
        pct_chg=20,
    )
    hit, reason = is_price_limit_hit(kline, prev_close=10.0, ts_code="688001.SH")
    assert hit is True
    assert "12.00" in reason

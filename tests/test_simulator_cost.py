"""
模拟器成本模型单元测试
"""

from __future__ import annotations

from modules.simulator import CostModel
from modules.simulator.cost_model import calculate_costs


def test_buy_cost_with_min_commission():
    costs = calculate_costs(10000.0, "BUY", CostModel())
    assert costs["commission"] == 5.0
    assert costs["stamp_duty"] == 0.0
    assert costs["total"] == 5.0 + 0.1


def test_sell_cost_includes_stamp_duty():
    costs = calculate_costs(20000.0, "SELL", CostModel())
    assert costs["stamp_duty"] == 20000.0 * 0.0005
    assert costs["total"] == max(20000.0 * 0.00025, 5.0) + costs["stamp_duty"] + 0.2


def test_partial_sell_has_stamp_duty():
    costs = calculate_costs(30000.0, "PARTIAL_SELL", CostModel())
    assert costs["stamp_duty"] == 30000.0 * 0.0005
    assert costs["commission"] == max(30000.0 * 0.00025, 5.0)


def test_stamp_duty_disabled():
    model = CostModel(apply_stamp_duty_on_sell=False)
    costs = calculate_costs(20000.0, "SELL", model)
    assert costs["stamp_duty"] == 0.0
    assert costs["total"] == max(20000.0 * 0.00025, 5.0) + 0.2

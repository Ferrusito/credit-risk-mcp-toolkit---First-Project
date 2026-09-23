"""Tests unitarios para risk_tools.py — sin dependencia del protocolo MCP."""

import pytest

from credit_risk_mcp.risk_tools import calculate_expected_loss


def test_calculate_expected_loss_valid_inputs() -> None:
    result = calculate_expected_loss(pd=0.05, lgd=0.45, ead=100_000)
    assert result["expected_loss"] == pytest.approx(2250.0)


@pytest.mark.parametrize("pd", [-0.1, 1.1])
def test_calculate_expected_loss_invalid_pd_raises(pd: float) -> None:
    with pytest.raises(ValueError):
        calculate_expected_loss(pd=pd, lgd=0.45, ead=100_000)


def test_calculate_expected_loss_negative_ead_raises() -> None:
    with pytest.raises(ValueError):
        calculate_expected_loss(pd=0.05, lgd=0.45, ead=-1)
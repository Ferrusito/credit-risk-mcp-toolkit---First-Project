"""Entrypoint MCP: expone risk_tools como herramientas invocables por el LLM."""

import logging

from mcp.server.fastmcp import FastMCP

from credit_risk_mcp.risk_tools import calculate_expected_loss as _calculate_expected_loss

logging.basicConfig(level=logging.INFO)
mcp = FastMCP("credit-risk-toolkit")


@mcp.tool()
def calculate_expected_loss(pd: float, lgd: float, ead: float) -> dict[str, float]:
    """Calcula la Pérdida Esperada (EL) a partir de PD, LGD y EAD."""
    try:
        return _calculate_expected_loss(pd, lgd, ead)
    except ValueError:
        logging.getLogger(__name__).exception("Input inválido en calculate_expected_loss")
        raise


if __name__ == "__main__":
    mcp.run()
"""Lógica de negocio pura, sin dependencia del protocolo MCP."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def calculate_expected_loss(pd: float, lgd: float, ead: float) -> dict[str, float]:
    """
    Calcula la Pérdida Esperada: EL = PD x LGD x EAD.

    Args:
        pd: Probability of Default, en [0, 1].
        lgd: Loss Given Default, en [0, 1].
        ead: Exposure at Default, en unidades monetarias (>= 0).

    Returns:
        Diccionario con el resultado y los inputs validados.

    Raises:
        ValueError: si algún parámetro está fuera de rango válido.
    """
    _validate_ratio(pd, "pd")
    _validate_ratio(lgd, "lgd")
    if ead < 0:
        raise ValueError(f"EAD no puede ser negativo: {ead}")

    expected_loss = round(pd * lgd * ead, 2)
    logger.info(
        "EL calculada: %.2f (PD=%.4f, LGD=%.4f, EAD=%.2f)", expected_loss, pd, lgd, ead
    )
    return {"expected_loss": expected_loss, "pd": pd, "lgd": lgd, "ead": ead}


def _validate_ratio(value: float, name: str) -> None:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name.upper()} debe estar entre 0 y 1, recibido: {value}")
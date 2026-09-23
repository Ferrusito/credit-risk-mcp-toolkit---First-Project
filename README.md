# Credit Risk MCP Toolkit

Servidor MCP en Python que expone herramientas de riesgo de crédito
(actualmente: cálculo de Expected Loss) a clientes compatibles con
el Model Context Protocol.

## Requisitos previos
- Python 3.10+
- Git

## Instalación
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
```

## Probar localmente
```bash
mcp dev src/credit_risk_mcp/server.py
```

## Tests
```bash
pytest tests/
```
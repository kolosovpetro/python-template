
python -m pip install uv
uv init
uv add requests
uv add --dev pytest ruff mypy

# reinstall packages
uv sync --reinstall

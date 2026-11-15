# init project
uv init my-project
cd my-project

# pin python version
uv python pin 3.14

# create venv
uv venv

# activate venv
source .venv/bin/activate

# deactivate venv
deactivate

# install dev dependencies
uv add requests
uv add --dev pytest ruff mypy

# run python
uv run python examples/main.py

# run tests
uv run pytest

# reinstall packages
uv sync --reinstall

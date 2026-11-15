# install dev dependencies
uv pip install -r requirements.txt

# run python
uv run python examples/args/main.py --arg1 "Cat" --arg2 "Dog" --name "Petro" --surname "Kolosov"

# inside venv
python examples/args/main.py --arg1 "Cat" --arg2 "Dog" --name "Petro" --surname "Kolosov"

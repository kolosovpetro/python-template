import subprocess

def main() -> None:
    print("Hello from python-template!")
    fruits = ["Apple", "Orange", "Watermelon"]
    for fruit in fruits:
        print(fruit)

    for index, fruit in enumerate(fruits):
        print(index, fruit)
        print(f'The fruit is {fruit} with number {index}')

    commands = [
        ["git", "status"],
        ["git", "branch", "--show-current"],
        ["git", "log", "-1", "--oneline"],
    ]

    for command in commands:
        result = run_cli_command(command)
        print(result.stdout.strip())

def run_cli_command(command: list[str], timeout: int = 60) -> str:
    result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
        )
    return result

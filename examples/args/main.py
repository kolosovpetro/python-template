import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python-template",
        description="Python Template CLI application",
    )

    parser.add_argument(
        "--arg1",
        type=str,
        required=True,
        help="First argument",
    )

    parser.add_argument(
        "--arg2",
        type=str,
        required=True,
        help="Second argument",
    )

    parser.add_argument(
        "--name",
        type=str,
        required=False,
        help="Name",
        default="Petro",
    )

    parser.add_argument(
        "--surname",
        type=str,
        required=False,
        help="Surname",
        default="Kolosov",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    print(f"Argument 1: {args.arg1}")
    print(f"Argument 2: {args.arg2}")
    print(f"Argument name: {args.name}")
    print(f"Argument surname: {args.surname}")


if __name__ == "__main__":
    main()

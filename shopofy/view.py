import argparse
from os.path import isfile
import sys


def get_args():
    parser = argparse.ArgumentParser(
        description="Shopofy: A tool to find position for a given Schottky power."
    )

    parser.add_argument(
        "--rqmap", type=str, metavar="FILE", help="Path to the rqmap file."
    )

    parser.add_argument("--power", type=float, help="The power value.")

    parser.add_argument(
        "--nomap",
        action="store_true",
        help="Ignore rqmap file and calculate position without it.",
    )

    args = parser.parse_args()

    if not args.nomap and not args.rqmap:
        print(
            "Error: You must provide --rqmap unless --nomap is used.", file=sys.stderr
        )
        parser.print_help()
        sys.exit(1)

    if args.nomap and args.rqmap:
        parser.error("You cannot use both --rqmap and --nomap at the same time.")

    if args.rqmap and not isfile(args.rqmap):
        parser.error(f'Can\'t find file "{args.rqmap}"')

    return args


def get_power_input() -> float:
    while True:
        try:
            power = float(input("Enter the impedance map value: "))
            return power
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def ask_for_file() -> str | None:
    choice = input("Do you want to provide an rqmap file? (y/n): ").strip().lower()
    if choice == "y":
        path = input("Enter the path to the rqmap file: ").strip()
        return path
    return None


def print_result(position):
    print(f"The position for your given power is {position:.3f} mm")

import argparse
from os.path import isfile


def get_args():
    parser = argparse.ArgumentParser(
        description="Shopofy: A tool to find position for a given Schottky power."
    )

    parser.add_argument(
        "-rq", "--rqmap", type=str, metavar="FILE", help="Path to the rqmap file."
    )

    parser.add_argument("-p", "--power", type=float, help="The power value.")

    args = parser.parse_args()

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


def print_result(position):
    print(f"The position for your given power is {position:.3f} mm")

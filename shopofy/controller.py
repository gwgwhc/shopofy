from .rqmap import load_rqmap, generate_rqmap, get_position
from .view import get_args, get_power_input, ask_for_file, print_result


class ShopofyController:
    def __init__(self):
        self.args = get_args()

    def run(self):
        power = self.handle_power()
        current_rqmap = self.handle_rqmap()
        position = get_position(current_rqmap, power)
        print_result(position)

    def handle_power(self):
        if self.args.power:
            return self.args.power
        return get_power_input()

    def handle_rqmap(self):
        if self.args.nomap:
            return generate_rqmap()

        if self.args.rqmap:
            return load_rqmap(self.args.rqmap)

        rqmap_path = ask_for_file()
        if rqmap_path:
            return load_rqmap(rqmap_path)
        return generate_rqmap()

from unary_gate import UnaryGate


class NotGate(UnaryGate):

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        if a == 0:
            return 1
        else:
            return 0


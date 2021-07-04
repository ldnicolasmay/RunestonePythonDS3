from binary_gate import BinaryGate


class OrGate(BinaryGate):

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


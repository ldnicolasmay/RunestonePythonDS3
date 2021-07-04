from logic_gate import LogicGate


class BinaryGate(LogicGate):

    def __init__(self, label):
        # LogicGate.__init__(self, label)
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return int(
                    input(f"Enter pin A input for gate {self.get_label()}: ")
                    )
        else:
            return self.pin_a.get_from_gate().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return int(
                    input(f"Enter pin B input for gate {self.get_label()}: ")
                    )
        else:
            return self.pin_b.get_from_gate().get_output()
    
    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b == source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


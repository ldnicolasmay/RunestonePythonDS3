class UnaryGate(LogicGate):

    def __init__(self, label):
        # LogicGate.__init__(self, label)
        super().__init__(label)
        self.pin = None

    def get_pin(self):
        return int(input(f"Enter pin input for gate {self.get_label()}: "))


class Singleton:

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        self.value = ""

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
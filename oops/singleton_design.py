class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print(cls._instance)
            cls._instance = super().__new__(cls)
        print(cls._instance)
        return cls._instance


    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value

s = Singleton()
s.setValue("Hi I am Balaji")
print(s.getValue())
s2 = Singleton()
class computer:

    brand = "Telusko AI"

    def __init__(self, cpu, ram, ssd):
        print("init called")
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd

    def config(self):
        print("config : ", self.cpu, self.ram, self.ssd)

    @classmethod
    def info(cls):
        return cls.brand

    @staticmethod
    def go_to_bytes(gb):
        return gb * (1024**3)


com1 = computer("i5", "16GB", "512GB")
com2 = computer("i9", "96GB", "2TB")

com1.config()
com2.config()

print(computer.go_to_bytes(16))
print(computer.info())

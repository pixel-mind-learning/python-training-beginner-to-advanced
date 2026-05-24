class Laptop:
    def build(self):
        print("Laptop builds")


class Desktop:
    def build(self):
        print("Desktop builds")


class Tablet:
    def open_pdf(self):
        print("Opening pdf...")


class Alien:
    def code(self, machine: Laptop):
        print("Alien builds")
        machine.build()


asus_rog = Laptop()
beast = Desktop()
lenovo_tab = Tablet()

navin = Alien()
# navin.code(asus_rog)
# navin.code(beast)
navin.code(lenovo_tab)

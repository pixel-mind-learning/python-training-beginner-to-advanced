from abc import ABC, abstractmethod  # abstract class


class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass


class TeluskoPay(PaymentGateway):
    def pay(self):
        print("paying using TeluskoPay...")


class RazorPay(PaymentGateway):
    def pay(self):
        print("paying using RazorPay...")


class Purchase:
    def __init__(self, gateway):
        self.gateway = gateway

    def checkout(self):
        print("checking out...")

        self.gateway.pay()


gateway1 = RazorPay()
gateway2 = TeluskoPay()

purchase = Purchase(gateway2)

purchase.checkout()

from abc import ABC, abstractmethod

class Payments(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payments):
    def process_payment(self, amount):
        print(f"Processing credit card payment of Rs{amount}")

class UPIPayment(Payments):
    def process_payment(self, amount):
        print(f"Processing UPI payment of Rs{amount}")

# Example usage
credit_card = CreditCardPayment()
credit_card.process_payment(100)
upi = UPIPayment()
upi.process_payment(200)

#  The following line would raise an error since Payments is an abstract class
# payment = Payments()
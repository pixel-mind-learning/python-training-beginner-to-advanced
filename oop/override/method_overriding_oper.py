a = 5

print(a.__str__())
# print(type(a.__str__()))
# print(type(a))


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name} : {self.balance}"

    def __add__(me, you):
        return Account("combined", me.balance + you.balance)

    def __gt__(self, other):
        return self.balance > other.balance


user1 = Account("navin", 1000)
user2 = Account("kiran", 2000)

combined = user1 + user2

print(user1.__str__())
print(user2)
print(combined)

if user1 > user2:
    print("navin pays the bill")
else:
    print("kiren pays the bill")

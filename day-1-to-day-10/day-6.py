import csv

#   # Exception
#   # Object Oriented Programming: Encapsulation, Inheritance, Polymorphism, Abstraction

try: 
    age = int(input("Insert your age: "))
    print(age)

except:
    print("Invalid age")
   

class Item:
    pay_rate = 0.8
    all_items = []

    def __init__(self, name: str, price:float, quantity = 1) -> None:

        # run validations to the received arguments
        assert price >= 0, f'Price must be greater than 0'
        assert quantity >=0, f'Quantity '

        # assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all_items.append(self)

    def calculate_total_price(self) -> float:
        return self.quantity * self.price
    
    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate 

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f'Item{self.name, self.price, self.quantity}'
    
    # Read only property
    @property
    def name_length(self):
        return len(self.name)
    
    @property
    def name(self):
        return self.__name
    

item1 = Item('Phone', 100, 1)

print(item1.name_length)
print(item1.name)
class Smartphone:
    def __init__(self, brand, model, os):
        self.brand = brand
        self.model = model
        self.os = os
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"The '{self.brand} {self.model}' is not powered on.")
        else:
            print(f"The '{self.brand} {self.model}' is already on.")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"The '{self.brand} {self.model} is now powered off.")
        else:
            print(f"The '{self.brand} {self.model} is already off.")

# Create an instance of the class
my_phone = Smartphone('Apple', 'Iphone 15 Pro', 'iOs 17.5')

# Demonstrate usage
# my_phone.power_on()
my_phone.power_off()
#
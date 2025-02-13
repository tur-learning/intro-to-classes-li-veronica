#my class will be for different purses
class Purses:
    def __init__(self, brand, color, model, EUR_value):
        self.brand = brand
        self.color = color
        self.model = model
        self.EUR_value = EUR_value

    def print_info(self):
        print(f"The {self.color} {self.brand} {self.model} is worth an estimated {self.EUR_value} euros.") 

    def update_value(self, new_value):
        self.EUR_value = new_value
        print(f"The estimated value for the {self.color} {self.brand} {self.model} has updated to: {self.EUR_value}")

    def currency_conversion(self):
        GBP_value = self.EUR_value * 0.83
            # as of 13/2/25 the exchange rate of GBP is 0.83
        USD_value = self.EUR_value * 1.04
            # as of 13/2/25 the exchange rate of USD is 1.04
        print(f"The value in GBP is {GBP_value} pounds and the value in dollars is {USD_value} dollars.")

from classes import Purses

def main():
    purse1 = Purses("Hermès", "Black", "Birkin 30", 15000)
    purse2 = Purses("Chanel", "Red", "Classic Flap", 7000)
    purse3 = Purses("Chanel", "Black", "Boy Bag", 4000)
    purse4 = Purses("Dior", "Beige", "Saddle Bag", 3500)
    purse5 = Purses("Gucci", "Green", "Jackie Bag", 2500)

    purse1.print_info()
    purse2.print_info()
    purse3.print_info()
    purse4.print_info()
    purse5.print_info()

    # Show currency conversion
    purse1.currency_conversion()
    purse2.currency_conversion()
    purse3.currency_conversion()
    purse4.currency_conversion()
    purse5.currency_conversion()

    # Update value for purse3 and show again
    purse1.update_value(25000)
    purse1.print_info()

main()
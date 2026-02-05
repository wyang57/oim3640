# a = input("Enter an integer: ") #How to make sure input is integer
# a = int(a)
# print(type(a))

# #check odd or even
# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# A product would cost $100, how much tax do we pay?

from tifffile import product


def calc_tax(price):
    '''Calculate product tax based on given price'''
# product = 100 #in dollars
    tax_rate = 0.0625
    price = float(input('Enter the product price: '))
    tax = price * tax_rate
    # print(f'The tax on a product that costs ${price} is ${tax}')
    print(tax)
    return None

# calc_tax(100)
# calc_tax(20)
tax_computer = calc_tax(computer_price)
tax_iphone = calc_tax(iphone_price)


total_tax = calc_tax(computer_price)+calc_tax
(iphone_price)
print(total_tax)





import math
def basePlusVatCalculate(basePrice):
    result = math.ceil(basePrice*1.07*100)/100
    return "{:.2f}".format(result)
basePrice = float(input('Please enter base price:'))
print(basePlusVatCalculate(basePrice))

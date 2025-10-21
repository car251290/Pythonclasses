
def unit_rate(total_amount, number_of_units):
        if number_of_units == 0:
            return None  
        return total_amount / number_of_units

def percentage(part, whole):
        if whole == 0:
            return None  
        return (part / whole) * 100


unit_rate(100,4)
percentage(3,4)


def unit_rate_calculate():
      num = int("Enter a number:")
      rate = 1
      calculate = num /rate
unit_rate_calculate()


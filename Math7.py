
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


## create a function where I will calculate the interest rate of the bank 
def calculate_interest(principal, rate, time):
    """
    Calculate the simple interest.

    Parameters:
    principal (float): The principal amount.
    rate (float): The annual interest rate (in percentage).
    time (float): The time the money is invested for (in years).

    Returns:
    float: The calculated interest.
    """
    interest = (principal * rate * time) / 100
    return interest
# Example usage
if __name__ == "__main__":
    p = 1000  # principal amount
    r = 5     # annual interest rate in percentage
    t = 3     # time in years

    interest = calculate_interest(p, r, t)
    print(f"The interest on a principal amount of {p} at an annual rate of {r}% for {t} years is: {interest}")


    ## function with the rate and the income of 1000 dollar per month 
    def calculate_monthly_interest(income, rate, months):
        """
        Calculate the interest earned on monthly income.

        Parameters:
        income (float): The monthly income amount.
        rate (float): The annual interest rate (in percentage).
        months (int): The number of months the income is invested.

        Returns:
        float: The calculated interest.
        """
        principal = income * months
        time = months / 12  # convert months to years
        interest = (principal * rate * time) / 100
        return interest
    
    # Example usage
    if __name__ == "__main__":
        monthly_income = 1000  # monthly income
        annual_rate = 5        # annual interest rate in percentage
        investment_months = 12 # number of months

        monthly_interest = calculate_monthly_interest(monthly_income, annual_rate, investment_months)
        print(f"The interest on a monthly income of {monthly_income} at an annual rate of {annual_rate}% for {investment_months} months is: {monthly_interest}")
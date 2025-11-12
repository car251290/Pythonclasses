def calculate_commission(sale_price, fee_rate):
    """
    Calculate commission using the formula: Fee = Sale Price × Fee Rate
    
    Args:
        sale_price (float): The price of the sale
        fee_rate (float): Commission rate (e.g., 0.05 for 5%)
    
    Returns:
        float: Commission amount
    """
    return sale_price * fee_rate

def calculate_total_pay(base_salary, commission):
    """
    Calculate total pay using the formula: Total Pay = Base Salary + Fee
    
    Args:
        base_salary (float): Base salary amount
        commission (float): Commission amount
    
    Returns:
        float: Total pay before taxes
    """
    return base_salary + commission

def calculate_taxes(total_pay, tax_rate):
    """
    Calculate taxes on total pay.
    
    Args:
        total_pay (float): Total pay amount
        tax_rate (float): Tax rate (e.g., 0.15 for 15%)
    
    Returns:
        float: Tax amount
    """
    return total_pay * tax_rate

def calculate_net_pay(total_pay, taxes):
    """
    Calculate net pay after taxes.
    
    Args:
        total_pay (float): Total pay before taxes
        taxes (float): Tax amount
    
    Returns:
        float: Net pay after taxes
    """
    return total_pay - taxes

def calculate_sales_compensation(sale_price, fee_rate, base_salary, tax_rate=0.0):
    """
    Complete sales compensation calculation using individual functions.
    
    Args:
        sale_price (float): The price of the sale
        fee_rate (float): Commission rate (e.g., 0.05 for 5%)
        base_salary (float): Base salary amount
        tax_rate (float): Tax rate (e.g., 0.15 for 15%), optional
    
    Returns:
        dict: Dictionary containing all calculated values
    """
    # Calculate each component using separate functions
    commission = calculate_commission(sale_price, fee_rate)
    total_pay = calculate_total_pay(base_salary, commission)
    taxes = calculate_taxes(total_pay, tax_rate) if tax_rate > 0 else 0
    net_pay = calculate_net_pay(total_pay, taxes)
    
    return {
        'sale_price': sale_price,
        'commission': commission,
        'base_salary': base_salary,
        'total_pay': total_pay,
        'tax_rate': tax_rate,
        'taxes': taxes,
        'net_pay': net_pay
    }

def display_sales_report(result):
    """
    Display a formatted sales compensation report.
    
    Args:
        result (dict): Result from calculate_sales_compensation function
    """
    print("=" * 50)
    print("         SALES COMPENSATION REPORT")
    print("=" * 50)
    print(f"Sale Price:           ${result['sale_price']:,.2f}")
    print(f"Commission:           ${result['commission']:,.2f}")
    print(f"Base Salary:          ${result['base_salary']:,.2f}")
    print(f"Total Pay:            ${result['total_pay']:,.2f}")
    
    if result['tax_rate'] > 0:
        print(f"Tax Rate: {result['tax_rate']:.1%}")
        print(f"Taxes:  ${result['taxes']:,.2f}")
        print(f"Net Pay (After Tax):  ${result['net_pay']:,.2f}")
    
    print("=" * 50)

# Example usage and testing
if __name__ == "__main__":
    # Example 1: Basic calculation
    print("Example 1: Basic Commission Calculation")
    result1 = calculate_sales_compensation(
        sale_price=10000,
        fee_rate=0.05,  # 5% commission
        base_salary=3000
    )
    display_sales_report(result1)
    
    print("\n")
    
    # Example 2: With taxes
    print("Example 2: Commission with Taxes")
    result2 = calculate_sales_compensation(
        sale_price=25000,
        fee_rate=0.08,  # 8% commission
        base_salary=4000,
        tax_rate=0.22   # 22% tax rate
    )
    display_sales_report(result2)
    
    print("\n")
    
    # Example 3: Multiple sales calculation
    print("Example 3: Multiple Sales Summary")
    sales_data = [
        {'sale_price': 5000, 'fee_rate': 0.06},
        {'sale_price': 8000, 'fee_rate': 0.06},
        {'sale_price': 12000, 'fee_rate': 0.06}
    ]
    
    base_salary = 2500
    tax_rate = 0.18
    total_commission = 0
    
    print("Individual Sales:")
    for i, sale in enumerate(sales_data, 1):
        result = calculate_sales_compensation(
            sale_price=sale['sale_price'],
            fee_rate=sale['fee_rate'],
            base_salary=0,  # Don't add base salary for individual sales
            tax_rate=0      # Calculate tax on total at the end
        )
        total_commission += result['commission']
        print(f"  Sale {i}: ${sale['sale_price']:,} × {sale['fee_rate']:.1%} = ${result['commission']:,.2f}")
    
    # Calculate total with base salary and taxes
    total_result = calculate_sales_compensation(
        sale_price=sum(sale['sale_price'] for sale in sales_data),
        fee_rate=0,  # Commission already calculated
        base_salary=base_salary + total_commission,  # Add pre-calculated commission to base
        tax_rate=tax_rate
    )
    
    print(f"\nTotal Commission:     ${total_commission:,.2f}")
    print(f"Base Salary:          ${base_salary:,.2f}")
    print(f"Gross Pay:            ${base_salary + total_commission:,.2f}")
    print(f"Taxes ({tax_rate:.0%}):           ${(base_salary + total_commission) * tax_rate:,.2f}")
    print(f"Net Pay:              ${(base_salary + total_commission) * (1 - tax_rate):,.2f}")
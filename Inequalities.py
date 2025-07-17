def check_triangle_inequality(a, b, c):
    """
    Checks if the given sides satisfy the triangle inequality theorem.
    The sum of any two sides must be greater than the third side.
    """
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def main():
    print("Triangle Inequality Checker")
    try:
        # Input the sides of the triangle
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        
        # Check the triangle inequality
        if check_triangle_inequality(a, b, c):
            print("The sides satisfy the triangle inequality theorem.")
        else:
            print("The sides do NOT satisfy the triangle inequality theorem.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
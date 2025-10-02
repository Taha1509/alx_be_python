
def safe_divide(numerator, denominator):
    try:
        numerator = float(input("enter the numerator number:"))
        denominator = float(input("enter the denominator number:"))

        result = numerator / denominator

    except ValueError:
        print("Error: Please enter valid numbers!")
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        
    else:
        print(f"Success! {numerator} ÷ {denominator} = {result}")
        
    finally:
        print("Operation completed. Thank you for using the calculator!")    
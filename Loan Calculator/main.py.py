def calculate_loan_payment(principal,annual_intrest_rate, months):
    monthly_intrest_rate =  annual_intrest_rate / 12 / 100
    
    if monthly_intrest_rate == 0:
        monthly_payment = principal / months
    else:
        monthly_payment = (
            principal * (monthly_intrest_rate * (1 + monthly_intrest_rate) ** months)/((1+monthly_intrest_rate)**months-1)
        )
        return monthly_payment
    
def main():
    print("welcome to the loan calculator!")
    principal = floatValidation("enter the loan amount: $")
    annual_intrest_rate =  floatValidation("enter the annual interest rate(as a percentage):")
    months = intValidation("enter the number of months:")
    monthly_payment = calculate_loan_payment(principal,annual_intrest_rate, months)
    print(f"your monthly payment is ${monthly_payment:.2f}")

def floatValidation(question):
    while True:
        try:
            value = float(input(question))
            return value
        except ValueError:
            print("please enter a valid number")
            continue

def intValidation(question):
    while True:
        try:
            value = int(input(question))
            return value
        except ValueError:
            print("input should be a valid number")

if __name__ == "__main__":
    main()
    

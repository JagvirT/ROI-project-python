class Company():
    def __init__(self, name):
        self.name = name

    def monthly_income(self):
        while True:
            try:
                rental_income = int(input("What is your monthly rental income from tenants?"))
                misc_income= int(input("Are there any other sources of income monthly, if so please input that number:"))
            except ValueError:
                continue
            else:
                break
        new_income = rental_income + misc_income
        print(f'Your monthly income: ${new_income}')

    def expenses(self):
        while True:
            try:
                tax_a = int(input("How much in taxes are you paying on the property monthly?"))
                utilities = input("Are paying ulilities yourself or not? (Please answer yes or no):".lower())
                if utilities == "yes":
                        util_owner = int(input("How much in utilities are you paying monthly?"))
                elif utilities == "no":
                    util_owner = 0
                ask_insurance_owner = input("Do you have a insurance monthly(yes/no)".lower())
                if ask_insurance_owner == 'yes':
                    insurance_owner = int(input("How much is the insurance monthly?"))
                elif ask_insurance_owner == 'no':
                    insurance_owner = 0
                if_vacancy = input("In case of vacancy on property, do you want to set aside money for future vacancies(yes or no?)".lower())
                if if_vacancy == 'yes':
                    vacancy_owner = int(input("How much would would like to set aside?"))
                elif if_vacancy == 'no':
                    vacancy_owner = 0
                prop_mortgage = int(input("How much is the mortgage on the property?"))
                ask_misc_expense = (input("Are there any miscellaneous expenses on the property? (yes or no)".lower()))
                if ask_misc_expense == 'yes':
                    misc_expenses = int(input("Please add all other expenses and input the value:"))
                elif ask_misc_expense == 'no':
                    misc_expenses = 0
            except ValueError:
                continue
            else:
                break
        total_expenses = tax_a + util_owner + insurance_owner + vacancy_owner + prop_mortgage + misc_expenses
        print(f'Your total expenses are ${total_expenses}.')


    def cash_flow_monthly(self):
        print("Please calculate monthly income and expenses within this program before proceeding")
        while True:
            try:
                total_income = int(input("What is your total income monthly?"))
                second_total_expenses = int(input("What is your total expenses monthly?"))
            except ValueError:
                continue
            else:
                break
        subract_income_expenses = total_income - second_total_expenses
        print(f'Your total cash flow monthly is ${subract_income_expenses}.')

    def cash_on_cash_roi(self):
        print("Please know monthly expenses before proceeding")
        while True:
            try:
                ask_down_payment = input("Did you put a down payment on the property? (yes/no)".lower())
                if ask_down_payment == 'yes':
                    down_payment = int(input("How much did you pay for the down payment?"))
                elif ask_down_payment == 'no':
                    down_payment = 0
                ask_closing_costs = input("Did you pay closing costs?(yes or no)")
                if ask_closing_costs == 'yes':
                    closing_cost = int(input("How much did you pay in closing costs?"))
                elif ask_closing_costs == 'no':
                    closing_cost = 0
                ask_misc_cost = input('Are there any other extra payments made for the property? (yes or no)'.lower())
                if ask_misc_cost == "yes":
                    misc_cost = int(input("Please total those miscallaneous costs on the property and provide the value:"))
                if ask_misc_cost == 'no':
                    misc_cost = 0
            except ValueError:
                continue
            else:
                break
        total_investment = down_payment + closing_cost + misc_cost
        ask_monthly_cash_flow = int(input('What is your total monthly cash flow that was calculated earlier?'))
        property_roi = ((ask_monthly_cash_flow * 12) / total_investment)  * 100
        print(f'Your ROI on this property yearly is {str(round(property_roi,2))}%.')

property = Company('Bigger Pockets')

def runner():
    while True:
        user_input = input("What would you like to do? (monthly income, monthly expenses, monthly cash flow, ROI, or quit)")
        if user_input == "quit":
            print("Thank you for using our services!")
            break
        elif user_input == 'monthly income':
            property.monthly_income()
        elif user_input == 'monthly expenses':
            property.expenses()
        elif user_input == 'monthly cash flow':
            property.cash_flow_monthly()
        elif user_input == 'ROI':
            property.cash_on_cash_roi()
        else:
            print("Invalid input, please try again.")
runner()


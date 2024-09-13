
import time

expenses = {"name 1": {"Expense Amount": 9999, "Expense Category":       
                    "Housing", "Expense Description": "example desc"},

            "name 2": {"Expense Amount": 12345, "Expense Category":       
                       "Transportation", "Expense Description": "example desc"},

            "name 3": {"Expense Amount": 3540, "Expense Category": 
                       "Housing", "Expense Description": "example desc"}
            }

time.sleep(0.5)
print("\nWelcome to your personal expense tracker.")

def start():
    
    time.sleep(0.5)
    print("\nWhat would you like to do today?")
    time.sleep(0.2)
    print("1. Check Total Expenses")
    time.sleep(0.2)
    print("2. Check Expenses per Category")
    time.sleep(0.2)
    print("3. Check a List of all Expenses with Details")
    time.sleep(0.2)
    print("4. Add an Expense")
    time.sleep(0.2)
    print("5. Remove an Expense")
    time.sleep(0.2)
    print("6. Close Expense Tracker")
    time.sleep(0.5)

    try:
        menu_input = int(input("[1/6]: "))

        if menu_input == 1:
            print("\nYou have selected 1. Check Total Expenses.")
            time.sleep(0.2)
            expense_total()

        elif menu_input == 2:
            print("\nYou have selected 2. Check Expenses per Category.")
            time.sleep(0.2)
            expense_category()

        elif menu_input == 3:
            print("\nYou have selected 3. Check a List of all Expenses with Details.")
            time.sleep(0.2)
            expense_detail()

        elif menu_input == 4:
            print("\nYou have selected 4. Add an Expense.")
            time.sleep(0.2)
            add_expense()

        elif menu_input == 5:
            print("\nYou have selected 5. Remove an Expense.")
            time.sleep(0.2)
            remove_expense()

        elif menu_input == 6:
            print("\nYou have selected 6. Close Expense Tracker.")
            time.sleep(0.2)
            print("Expense Tracker will now close.")
            time.sleep(0.2)
            return

        else:
            print("\nYou have to select a number between 1 - 6. You will be brought back to the menu.")
            time.sleep(0.2)
            start()

    except ValueError as v:
        print(f"\nAn Error has Occurred (ValueError): {v}")
        time.sleep(1)
        print("You will be brought back to the menu. Please make sure to follow instructions properly to avoid future errors.")
        time.sleep(0.5)
        start()
        
    except Exception as e:
        print(f"\nAn Error has Occurred (Other Error): {e}")
        time.sleep(1)
        print("You will be brought back to the menu. Please make sure to follow instructions properly to avoid future errors.")
        time.sleep(0.5)
        start()


def expense_total():
    print("\nTotal Expenses will now be listed.")

    e_total = 0

    for name, info in expenses.items():
        for val in info.values():
            if isinstance(val, int):                
                e_total += val

    time.sleep(0.5)
    print(f"\n£{"%.2f" % float("%.2f" % e_total / 100)}")
    time.sleep(0.5)
    input("\nPress Enter to continue.")
    time.sleep(0.5)
    start()

def expense_category():
    print("\nWhich category would you like to view?")
    print("1. Housing")
    time.sleep(0.2)
    print("2. Transportation")
    time.sleep(0.2)
    print("3. Food & Dining")
    time.sleep(0.2)
    print("4. Entertainment & Leisure")
    time.sleep(0.2)
    print("5. Health & Wellness")
    time.sleep(0.2)
    print("6. Personal Care")
    time.sleep(0.2)
    print("7. Education & Personal Development")
    time.sleep(0.2)
    print("8. Family & Childcare")
    time.sleep(0.2)
    print("9. Savings & Investments")
    time.sleep(0.2)
    print("10. Dept Repayment")
    time.sleep(0.2)
    print("11. Gifts & Donations")
    time.sleep(0.2)
    print("12. Miscellaneous")
    time.sleep(0.2)
    print("13. Emergencies & Unexpected Expense")
    time.sleep(0.2)
    print("14. Business Expense")
    time.sleep(0.2)
    
    try:
        
        e_category = int(input("[1/14]: "))
        time.sleep(0.5)
        
        if e_category == 1:
            print("\nYou have chosen 1. Housing.")
            e_category = "Housing" 

        elif e_category == 2:
            print("\nYou have chosen 2. Transportation.")
            e_category = "Transportation"

        elif e_category == 3:
            print("\nYou have chosen 3. Food & Dining.")
            e_category = "Food & Dining"

        elif e_category == 4:
            print("\nYou have chosen 4. Entertainment & Leisure.")
            e_category = "Entertainment & Leisure"

        elif e_category == 5:
            print("\nYou have chosen 5. Health & Wellness.")
            e_category = "Health & Wellness"

        elif e_category == 6:
            print("\nYou have chosen 6. Personal Care.")
            e_category = "Personal Care"

        elif e_category == 7:
            print("\nYou have chosen 7. Education & Personal Development.")
            e_category = "Education & Personal Development"

        elif e_category == 8:
            print("\nYou have chosen 8. Family & Childcare.")
            e_category = "Family & Childcare"

        elif e_category == 9:
            print("\nYou have chosen 9. Savings & Investments.")
            e_category = "Savings & Investments"

        elif e_category == 10:
            print("\nYou have chosen 10. Dept Repayment.")
            e_category = "Dept Repayment"

        elif e_category == 11:
            print("\nYou have chosen 11. Gifts & Donations.")
            e_category = "Gifts & Donations"

        elif e_category == 12:
            print("\nYou have chosen 12. Miscellaneous.")
            e_category = "Miscellaneous"

        elif e_category == 13:
            print("\nYou have chosen 13. Emergencies & Unexpected Expenses.")
            e_category = "Emergencies & Unexpected"

        elif e_category == 14:
            print("\nYou have chosen 14. Business Expenses.")
            e_category = "Business"

        else:
            time.sleep(0.2)
            print("\nYou have to select a number between 1 - 14. You will be brought back to the start of the Check Expense by Category menu.")
            time.sleep(1)
            expense_category()
            
    except ValueError as v:
        time.sleep(0.5)
        print(f"\nAn Error has Occurred (ValueError): {v}")
        time.sleep(1)
        print("You will be brought back to the menu. Please make sure to follow instructions properly to avoid future errors.")
        time.sleep(0.5)
        start()
        
    except Exception as e:
        time.sleep(0.5)
        print(f"\nAn Error has Occurred (Other Error): {e}")
        time.sleep(1)
        print("You will be brought back to the menu. Please make sure to follow instructions properly to avoid future errors.")
        time.sleep(0.5)
        start()
    
    category_total = 0
    
    for name, info in expenses.items():
        if e_category in info.values():
            time.sleep(0.4)
            print("\n\033[1m",name,"\n\033[0m")
            time.sleep(0.4)
            for key in info:
                time.sleep(0.2)
                if isinstance(info[key], int):
                    print(key + ":", f"£{"%.2f" % float(info[key] / 100)}")
                    category_total += info[key]
                else:
                    print(key + ":", info[key])
    time.sleep(0.4)                    
    print(f"\n\033[1mCategory Total: £{float("%.2f" % category_total / 100)}\033[0m")
    
    time.sleep(0.5)
    input("\nPress Enter to continue.")
    time.sleep(0.5)
    start()
                        
def expense_detail():
    print("\nExpenses with all details will be listed.")

    for name, info in expenses.items():
        time.sleep(0.4)
        print("\n\033[1m",name,"\n\033[0m")
        time.sleep(0.4)
        for key in info:
            time.sleep(0.2)
            if isinstance(info[key], int):
                print(key + ":", f"£{"%.2f" % float(info[key] / 100)}")
            else:
                print(key + ":", info[key])

    time.sleep(0.5)
    input("\nPress Enter to continue.")
    time.sleep(0.5)
    start()

def add_expense():

    print("\nPlease provide the details of the expense you would like to add below")
    time.sleep(0.5)
    e_name = input("\nExpense Name: ")
    time.sleep(0.2)
    e_amount = float(input("\nExpense Amount: £"))
    time.sleep(0.2)
    e_desc = input("\nExpense Description: ")
    time.sleep(0.2)
    print("\nExpense Category")
    time.sleep(0.2)
    print("1. Housing")
    time.sleep(0.2)
    print("2. Transportation")
    time.sleep(0.2)
    print("3. Food & Dining")
    time.sleep(0.2)
    print("4. Entertainment & Leisure")
    time.sleep(0.2)
    print("5. Health & Wellness")
    time.sleep(0.2)
    print("6. Personal Care")
    time.sleep(0.2)
    print("7. Education & Personal Development")
    time.sleep(0.2)
    print("8. Family & Childcare")
    time.sleep(0.2)
    print("9. Savings & Investments")
    time.sleep(0.2)
    print("10. Dept Repayment")
    time.sleep(0.2)
    print("11. Gifts & Donations")
    time.sleep(0.2)
    print("12. Miscellaneous")
    time.sleep(0.2)
    print("13. Emergencies & Unexpected Expense")
    time.sleep(0.2)
    print("14. Business Expense")
    time.sleep(0.2)
    
    try:
        
        e_category = int(input("[1/14]: "))
        time.sleep(0.5)

        if e_category == 1:
            print("\nYou have chosen 1. Housing.")
            e_category = "Housing" 

        elif e_category == 2:
            print("\nYou have chosen 2. Transportation.")
            e_category = "Transportation"

        elif e_category == 3:
            print("\nYou have chosen 3. Food & Dining.")
            e_category = "Food & Dining"

        elif e_category == 4:
            print("\nYou have chosen 4. Entertainment & Leisure.")
            e_category = "Entertainment & Leisure"

        elif e_category == 5:
            print("\nYou have chosen 5. Health & Wellness.")
            e_category = "Health & Wellness"

        elif e_category == 6:
            print("\nYou have chosen 6. Personal Care.")
            e_category = "Personal Care"

        elif e_category == 7:
            print("\nYou have chosen 7. Education & Personal Development.")
            e_category = "Education & Personal Development"

        elif e_category == 8:
            print("\nYou have chosen 8. Family & Childcare.")
            e_category = "Family & Childcare"

        elif e_category == 9:
            print("\nYou have chosen 9. Savings & Investments.")
            e_category = "Savings & Investments"

        elif e_category == 10:
            print("\nYou have chosen 10. Dept Repayment.")
            e_category = "Dept Repayment"

        elif e_category == 11:
            print("\nYou have chosen 11. Gifts & Donations.")
            e_category = "Gifts & Donations"

        elif e_category == 12:
            print("\nYou have chosen 12. Miscellaneous.")
            e_category = "Miscellaneous"

        elif e_category == 13:
            print("\nYou have chosen 13. Emergencies & Unexpected Expenses.")
            e_category = "Emergencies & Unexpected"

        elif e_category == 14:
            print("\nYou have chosen 14. Business Expenses.")
            e_category = "Business"

        else:
            time.sleep(0.2)
            print("\nYou have to select a number between 1 - 14. You will be brought back to the start of the Add Expense menu.")
            time.sleep(1)
            add_expense()
            
    except ValueError as v:
        time.sleep(0.5)
        print(f"\nAn Error has Occurred (ValueError): {v}")
        time.sleep(1)
        print("You will be brought back to the menu. Please make sure to follow instructions properly to avoid future errors.")
        time.sleep(0.5)
        start()
        
    except Exception as e:
        time.sleep(0.5)
        print(f"\nAn Error has Occurred (Other Error): {e}")
        time.sleep(1)
        print("You will be brought back to the menu. Please make sure to follow instructions properly to avoid future errors.")
        time.sleep(0.5)
        start()

    time.sleep(0.5)
    add_confirm(e_name, e_amount, e_desc, e_category)

def add_confirm(e_name, e_amount, e_desc, e_category):

    print("\nThe new expense you would like to add is: ")
    time.sleep(0.2)
    print(f"Expense Name: {e_name}")
    time.sleep(0.2)
    print(f"Expense Amount: £{"%.2f" % e_amount}")
    time.sleep(0.2)
    print(f"Expense Description: {e_desc}")
    time.sleep(0.2)
    print(f"Expense Category: {e_category}")
    time.sleep(0.2)
    add = input("\nIs This Correct? [Y/N]: ")
    time.sleep(0.5)
    
    try:
        
        if add.lower() == "y":
            
            if e_name in expenses:
                e_current = expenses[e_name]["Expense Amount"] / 100
                print(f"\nExpense {e_name} already exists, £{"%.2f" % e_amount} will be added to the existing amount of £{ "%.2f" % e_current}.")
                e_amount = e_amount * 100
                expenses[e_name]["Expense Amount"] += int(e_amount) 
                time.sleep(0.2)
                print("\nWould you like to go back to:")
                print("1. Add Expense")
                print("2. Main Menu")
                back = int(input("[1/2]: "))
                time.sleep(0.5)

                if back == 1:
                    add_expense()

                elif back == 2:
                    start()
                            
                else:
                    print("You have to select 1 or 2. You will be moved back to the main menu.")
                    time.sleep(0.5)
                    start()
            else:
                print(f"Expense {e_name} has been added.")
                e_amount = e_amount * 100
                expenses[e_name] = {"Expense Amount": int(e_amount), "Expense Description": e_desc, "Expense Category": e_category}
                time.sleep(0.2)
                print("\nWould you like to go back to:")
                print("1. Add Expense")
                print("2. Main Menu")
                back = int(input("[1/2]: "))
                time.sleep(0.5)
                
                if back == 1:
                    add_expense()

                elif back == 2:
                    start()
                            
                else:
                    print("You have to select 1 or 2. You will be moved back to the main menu.")
                    time.sleep(0.5)
                    start()
            
        elif add.lower() == "n":
            print("\nIt seems something has been entered wrong.")
            time.sleep(0.2)
            print("Would you like to go back to:")
            print("1. Add Expense")
            print("2. Main Menu")
            back = int(input("[1/2]: "))
            time.sleep(0.5)
            
            if back == 1:
                add_expense()

            elif back == 2:
                start()
                        
            else:
                print("You have to select 1 or 2. You will be moved back to the main menu.")
                time.sleep(0.5)
                start()

        else:
            print("You must input Y or N to continue.")
            time.sleep(1)
            add_confirm(e_name, e_amount, e_desc, e_category)

    except ValueError as v:
        time.sleep(0.5)
        print(f"\nAn Error has Occurred (ValueError): {v}")
        time.sleep(1)
        print("You will be brought back to the menu. Please make sure to follow instructions properly to avoid future errors.")
        time.sleep(0.5)
        start()
        
    except Exception as e:
        time.sleep(0.5)
        print(f"\nAn Error has Occurred (Other Error): {e}")
        time.sleep(1)
        print("You will be brought back to the menu. Please make sure to follow instructions properly to avoid future errors.")
        time.sleep(0.5)
        start()

def remove_expense():
    
    print("\nYou have chosen to remove an expense.")
    time.sleep(0.2)
    print("Which expense would you like to remove?")
    time.sleep(0.5)
    print("")
    
    num = 0
    
    for name in expenses:
            time.sleep(0.2)
            num += 1
            print(f"{num}.",name)
       
    num += 1     
    time.sleep(0.2)
    print(f"{num}. Remove all")
    time.sleep(0.2)
    
    try:
        
        choice = int(input(f"[1/{num}]: "))
        time.sleep(0.5)
        limit = len(expenses)

        if choice <= limit:
            
            remove = list(expenses)[choice - 1]
            del expenses[f"{str(remove)}"]
            
            print(f"\n{remove} Has been removed.")
            time.sleep(0.5)
            print("\nWould you like to go back to:")
            time.sleep(0.2)
            print("1. Remove Expense")
            time.sleep(0.2)
            print("2. Main Menu")
            time.sleep(0.2)
            back = int(input("[1/2]: "))
            time.sleep(0.5)
            
            if back == 1:
                remove_expense()

            elif back == 2:
                start()
            
            else:
                print(f"\nYou have to select a number between 1 - 2. Please make sure to follow instructions properly to avoid future errors.")
                time.sleep(1)
                print("You will be brought back to the main menu.")
                time.sleep(0.5)
                start()
                
        elif choice == limit + 1:
            print("\nYou have chosen to remove all expenses recorded in the expense tracker.")
            time.sleep(0.5)
            confirm = input("\nAre you sure you want to remove all expenses? [Y/N]: ")
            
            if confirm.lower() == "y":
                expenses.clear()
                print("\nAll expenses removed.")
                time.sleep(0.2)
                print("You will be brought back to the main menu.")
                time.sleep(0.5)
                start()
                
            elif confirm.lower() == "n":
                print("\nYou have chosen not to remove all expenses.")
                time.sleep(0.5)
                print("\nWould you like to go back to:")
                time.sleep(0.2)
                print("1. Remove Expense")
                time.sleep(0.2)
                print("2. Main Menu")
                time.sleep(0.2)
                back = int(input("[1/2]: "))
                time.sleep(0.5)
            
            if back == 1:
                remove_expense()

            elif back == 2:
                start()
            
            else:
                print(f"\nYou have to select a number between 1 - 2. Please make sure to follow instructions properly to avoid future errors.")
                time.sleep(1)
                print("You will be brought back to the main menu.")
                time.sleep(0.5)
                start()
                
        else:
            print(f"\nYou have to select a number between 1 - {num}. Please make sure to follow instructions properly to avoid future errors.")
            time.sleep(1)
            print("You will be brought back to the main menu.")
            time.sleep(0.5)
            start() 
             
    except ValueError as v:
        time.sleep(0.5)
        print(f"\nAn Error has Occurred (ValueError): {v}")
        time.sleep(1)
        print("You will be brought back to the menu. Please make sure to follow instructions properly to avoid future errors.")
        time.sleep(0.5)
        start()
        
    except Exception as e:
        time.sleep(0.5)
        print(f"\nAn Error has Occurred (Other Error): {e}")
        time.sleep(1)
        print("You will be brought back to the menu. Please make sure to follow instructions properly to avoid future errors.")
        time.sleep(0.5)
        start()
            
        
start()


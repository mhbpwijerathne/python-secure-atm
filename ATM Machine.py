correct_pin = "7343"
balance = 25000
attempts = 0


print("=== WELCOME TO PYTHON BANK ===")

while attempts < 3 :
    pin = input(" Enter Your PIN ")
    if pin  == correct_pin :
        print("Login Successful! Welcome Harsha ")
        break
    else:
        attempts += 1
        remaining = 3 - attempts

        if attempts > 0 :
            print(f"WRONG PIN! Please Try Again.{remaining}attempts")

        else:
            print("Your Attempts almost Over. Your Card Is Temporary Locked!")


while True: 
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = input("Select option: ")

    if choice == "1":
        print(f"Balance :  Rs.{balance}")
    elif choice == "2":
        amount = float(input("Enter Withdrawal Amount: Rs."))
        if amount > (balance-1000) :
            print("Insufficient funds!")
            print("Reason: You must keep a Rs. 1000 balance in your account.")
            print(f"Maximum amount yoou can withdraw is :Rs. {balance-1000}")
        else:
            new_balance = balance - amount
            print(f"Please Collect Your Cash: Rs.{amount}")
            print(f"Remaning Balance: Rs. {new_balance}")

    elif choice == "3":
        deposit_amount = int(input("Enter the amount to deposit:"))
        if deposit_amount > 0 :
            balance += deposit_amount
            print("Deposit Successful!Rs. {deposit_amount}")
            print(f"New Balance : Rs.{balance}")
        else:
            print("Invalid Amount!")
             

    elif choice == "4" :
        print("\nThank you for using our PYTHON BANKap ATM. Goodbye!")
        break
    else:
        print("Invalid option! Try again.")

            
    
        

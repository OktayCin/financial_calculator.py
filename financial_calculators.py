import math

print('''           

                       .'`. ,'`.
                  .---./    u    \,---.
               ___|    \    |    /    |___
              \    `.   \   |   /   .'    /
               \_    `.  \  |  /  .'    _/
             .-' `-._  `.:::::::.'  _.-' `-.
             \       `-;:::::::::;-'       /
              >~------~:::::::::::~------~<
             /      _.-;:::::::::;-._      \\
             `-._.-'   .`.::::::'.   `-._.-'
                /    .'  /  |  \  `.    \\
               /___.'   /   |   \   `.___\\
                   |   /    |    \    |
                   `--'\   .n.   /`---'
                        `.'   `.'          
             WELCOME TO NATURAL FINANCIALS INC.
        ==========================================                        

SERVICES MENU:

Investment Calculator: to calculate the amount of interest you'll earn on your investment
Bond Calculator: to calculate the amount you'll have to pay on a home loan

''')


#Validate user's response. Force user to only choose INVESTMENT or BOND.

while True:
   
    choose_cal = input('Choose a calculator. "Investment" or "Bond": ').upper()
    

    #Questions to ask if user chooses "INVESMENT"

    if choose_cal == "INVESTMENT":
        print("You chose the Investment Calculator\n")
        
        deposit = float(input("What is your deposit amount? £"))
        round(deposit, 2)

        interest_rate_inv = float(input("What is the percentage interest rate?: "))
        round(interest_rate_inv, 2)
        
        years_to_invest = int(input("How many years do yo plan on investing? "))
        round(years_to_invest, 2)
        

        #Force user to choose "SIMPLE" or "COMPOUND"

        while True:    
            interest_type = input('Which interest type do you want? "simple" or "compound": ').upper()


            #If user chooses SIMPLE

            if interest_type == "SIMPLE":
                simple_return =  deposit * (1 + (interest_rate_inv / 100) * years_to_invest)
                round(simple_return, 2)

                print(f"Based on the simple rate, your investment is expected to return £{simple_return}")
                
                break
                

            #If user chooses COMPOUND
                
            elif interest_type == "COMPOUND":
                compound_return = deposit * math.pow((1 + (interest_rate_inv /100)), years_to_invest)
                round(compound_return, 2)

                print(f"Based on the compound rate, your investment is expected to return £{round(compound_return, 2)}")
                break


            #If user doesn't give the required response

            else:
                print('Error. Choose only "simple" or "compound".\n')
                continue
        
        break
    

    #Questions to ask if user  chooses "BOND"
    
    if choose_cal == 'BOND':
        print("You chose the Bond Calculator\n")

        property_value = int(input("Enter the property value: £"))
        annual_interest_rate = float(input("Enter the percentage interest rate?: "))
        monthly_interest_rate = (annual_interest_rate / 100) / 12
        months = int(input("How many months to repay the bond?: "))

        repayment = (monthly_interest_rate * property_value)/(1 - (1 + monthly_interest_rate)**(- months))
        round(repayment, 2)

        print(f"Your monthly repayment will be £{round(repayment, 2)}")

        break


    #Force user to choose "INVESTMENT" or "BOND" in the initial question

    else:
        print('Error. Choose "Investment" or "Bond". Try again!\n')
        continue
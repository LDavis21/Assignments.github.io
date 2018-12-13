workable_hours = 8
tax_rate = .3

#ask if days or hours
days = input("Calculate by days? (y/n)")
active = True

while active == True:
    if days == 'y':
        time_off = float(input("Great! How many days would you like off?"))
        #ask how much they make per hour
        hourly_wage = float(input("What's your hourly wage?"))
        #Get amount earned by finding out how much each day is worth at your hourly rate
        earned = time_off * (hourly_wage * workable_hours)
        #Subtract your taxed income
        taxes = earned * tax_rate
        final_cost = earned - taxes
        print("You should budget for ${}".format(int(final_cost)))
        active = False
    elif days == 'n':
        time_off = int(input("Great! Let's calculate by the hour. How many hours?"))
        #ask how much they make per hour
        hourly_wage = int(input("What's your hourly wage?"))
        #Get amount earned during time off
        earned = time_off * (hourly_wage)
        #Subtract your taxed income
        taxes = earned * tax_rate
        final_cost = earned - taxes
        print("You should budget for ${}".format(str(final_cost)))
        active = False
    else:
        print("Sorry, couldn't understand that.")
        days = input("Calculate by days? (y/n)")
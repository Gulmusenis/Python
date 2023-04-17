#Create salesperson_revenue dictionary
salesperson_revenue = {
    "Ben": 0,
    "Omer": 0,
    "Karen": 0,
    "Celine": 0,
    "Sue": 0,
    "Bora": 0,
    "Rose": 0,
    "Ellen": 0
}

#Define enter_revenue function
def enter_revenue(name,revenue):
    global salesperson_revenue
    salesperson_revenue[name] += revenue

#Asking user employee name and revenue as input if the user enters "quit" break the loop
print('If you want to exit from the loop enter "quit"')
while True:
    name = input("Employee name:")
    if name == "quit":
        break
    revenue = int(input("Enter revenue:"))
    enter_revenue(name,revenue)
    print(f"{name}'s revenue is {salesperson_revenue[name]}")

#Print the salesperson_revenue dictionary
print(salesperson_revenue)
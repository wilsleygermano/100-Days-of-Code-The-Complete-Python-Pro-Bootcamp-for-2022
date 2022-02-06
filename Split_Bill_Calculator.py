#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the bill split calculator!")

bill = input("What is the total cost of the bill?\n")
tip = input("How much tip would you like o give: 10, 12 or 15?\n")
person = input("How many people to split the bill?\n")

bill_float = float(bill)
tip_int = int(tip)
person_int = int(person)

tip_percent = tip_int / 100

bill_tipped = bill_float + (bill_float * tip_int)

total_cost = bill_float / person_int

print(f"Each person should pay: ${total_cost}")

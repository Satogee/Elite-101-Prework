#purpose of this code is to make a chatbot that gives


#different responses based on the age inputed, and list 

# products for you to choose and give you an option to 
#exit if user is not satifed with any of the options presented.

print("Welcome to the Elite 101 chatbot!!")

#stores user name in the name variable 

name = input("Please enter your name:")

print(f"Nice to meet you, {name}!") 

#stores user age in the age variable 

age = int(input("How old are you?:"))

#eldest age at top and youngest at bottom (oldest has an if statement while the rest has elif)

#added elif on rest so multiple messages won't print

if age >= 30:
  print(f"Welcome {name}, you've lived long! How may I help you?:")

elif age >= 18:
  print(f"Welcome {name}, oh to be {age} again, how may I help you?:")
#prints certain message if their ages are 18 and greater but less than 30

elif age >= 17:
  print(f"Welcome {name}, aproaching adulthood I see! what can I do for you?:")
 
#prints certain message if their between ages 16-17

if age == 13:
  print(f"Oh, to be an teenager again, what can I do for you? {name}")
#prints certain message if their age is 13

elif age <= 12:
  print("Welcome little one, how may I help you?")
#prints certain message if their between ages 0- 12

elif age <= 15:
    print(f"Welcome {name}, what can I do for you?:")
#prints certain message if their between ages 14-15
#def function display_inventory prints all the options for user to choose

def display_inventory():
  print("1.toys for kids")
  print("2.airpod products ")
  print("3.Men/Woman clothes")
  print("4.leave/exit")
  
#def function "inventory" prints the options of the #inventory and displays the options 



display_inventory()  
user_choice = int(input("Choose from the following options:"))
def view_inventory():
  barbie_dolls = 4.00
  big_dinosaur_toys = 5.00
  small_dinosaur_toys = 8.00
  print(f"barbie dolls: {barbie_dolls}\n\nbig dinosaur toys: {big_dinosaur_toys}\n\nsmall dinosaur toys: {small_dinosaur_toys}\n")
  print("Is there anything that interests you?")
  customer_interest = input("If so please enter:")
  if customer_interest =="barbie dolls":
    print("great choice")
    amount = int(input(f"How many {customer_interest} would you like to buy: "))
    total = barbie_dolls * amount 
    print(f"your total due is {total} dollars")
  elif customer_interest == "big dinosaur toys":
    print("excellent choice!")
    amount = int(input(f"How many {customer_interest} would you like to buy?: "))
    total = big_dinosaur_toys * amount 
    print(f"your total due is {total} dollars")
  elif customer_interest == "small dinosaur toys":
    print("nice choice!")
    amount = int(input(f"How many {customer_interest} would you like to buy?: "))
    total = small_dinosaur_toys * amount 
    print(f"your total due is {total} dollars")
  else:
    print("Invalid , Please try again.")
    
     
  
def woman_man_clothes():
  crop_top = 4.00
  oversized_Tshirt = 25.00
  oversized_cargo_pants = 35.00
  shirt = 5.00
  print(f"crop tops: {crop_top}\n\noversized T-shirts: {oversized_Tshirt}\n\nOversized cargo pants: {oversized_cargo_pants}\n\nShirts: {shirt}\n")
  print("Is there anything that interests you?")
  customer_interest = input("If so please enter:")
  if customer_interest =="crop tops":
    print("great choice")
    amount = int(input(f"How many {customer_interest} would you like to buy: "))
    total = crop_top * amount 
    print(f"your total due is {total} dollars")
  elif customer_interest == "oversized tshirts":
    print("excellent choice!")
    amount = int(input(f"How many {customer_interest} would you like to buy?: "))
    total = oversized_Tshirt * amount 
    print(f"your total due is {total} dollars")
  elif customer_interest == "oversized cargo pants":
    print("nice choice!")
    amount = int(input(f"How many {customer_interest} would you like to buy?: "))
    total = oversized_cargo_pants * amount 
    print(f"your total due is {total} dollars")
  elif customer_interest == "shirts":
    print("nice choice!")
    amount = int(input(f"How many {customer_interest} would you like to buy?: "))
    total = shirts * amount 
    print(f"your total due is {total} dollars")
  else:
    print("Invalid , Please try again.")
def iphone_products():
  
  airpods = 69.00
  airpods_pro = 100.00
  airpods_pro_max = 160.00
  print(f"airpods: {airpods}\n\nairpods pro: {airpods_pro}\n\nairpods pro max: {airpods_pro_max}\n")
  print("Is there anything that interests you?")
  customer_interest = input("If so please enter:")
  if customer_interest =="airpods":
    print("great choice")
    amount = int(input(f"How many {customer_interest} would you like to buy: "))
    total = airpods * amount 
    print(f"your total due is {total} dollars")
  elif customer_interest =="airpods pro":
    print("great choice")
    amount = int(input(f"How many {customer_interest} would you like to buy: "))
    total = airpods_pro * amount 
    print(f"your total due is {total} dollars")
  elif customer_interest =="airpods pro max":
    print("great choice")
    amount = int(input(f"How many {customer_interest} would you like to buy: "))
    total = airpods_pro_max * amount 
    print(f"your total due is {total} dollars")
if user_choice == 1:
    view_inventory()
    
elif user_choice == 2:
    iphone_products()
elif user_choice == 3:
  woman_man_clothes()
elif user_choice == 4:
  print("Goodbye, have an nice day!")

else: 
  print("Invalid, please try again")


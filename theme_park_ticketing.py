print('welcome to The "Python Adventure Park"')
name=input("enter your name:").title()
age=int(input("enter your age:"))
adult= 40.00
child= 25.00
senior= 30.00
photo = 10.00
meal= 15.00
order_number=5832
price=0
if age<=5:
     print("The ticket is free")
elif age>5 and age<18:
    price +=child
    print(f"The ticket price is:\n{child}")

elif age>17 and age<66:             
    price+=adult
    print(f"The ticket price is:\n{adult}")
elif age>65:
    price+=senior
    print(f"The ticket price is:\n{senior}")
else:
    print("Please enter valid Age")
want_photos=input('Do you want photos"yes or no"?:')
if want_photos=="no":
     print(f'your price without photos is:\n{price}')
elif want_photos=="yes":
    price+=photo
    print(f'your price with photos is:\n{price}')
want_meal=input('Would you like to have meal"yes or no"?:')
if want_meal=="no":
    print(f'your final bill without meal is:\n{price}')
elif want_meal=="yes":
    price+=meal
    print(f'your final bill with meal is:\n{price}')
day=input('is today tuesday,"yes or no"?:\n')
if day=="yes"and age>5 and age<18 or age>65:
    price=price-5
    print(f"you got lucky discount final price is:\n{price}")
a=int(input('enter your order number:'))
if (a%2==0):
    print("Congratulations! Your even order number wins you a free popcorn! 🍿")
      
print(f"your final Total is:{price}")   
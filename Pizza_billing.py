
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
bill = 0
if size == "l":
    bill+=25
elif size == "m":
    bill+=20
elif size=="s":
    bill+=15
else:
    print("invalid size:")
if pepperoni =="y" and (size =="l" or size=="m"):
    bill+=3
elif pepperoni=="y" and size=="s":
    bill+=2
if extra_cheese=="y":
    bill+=1
print(f"Your bill is:{bill}")
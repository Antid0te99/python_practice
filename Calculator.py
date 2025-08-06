from art import logo
print(logo)
def calculator(n1,n2):
    n1=int(input("enter first number:"))
    while True:
        opt=input("choose the option:\n'+'\n'-'\n'*'\n'/':\n")
        n2=int(input("enter second number:"))
        a=0
        if opt=="+":
            a = n1+n2
            print (a)
        elif opt=="-":
            a = n1-n2
            print(a)
        elif opt=="*":
            a = n1*n2
            print(a)
        elif opt=="/":
            a=n1%n2
            print(a)
        else:
            print("invalid input")
            break

    play_again = input(f"Type 'y' to continue calculating with {a}, or type 'n' to start a new calculation: ")
    if play_again == "y":
        n1=a
    else:
        print("\n"*20)
calculator("n1","n2")
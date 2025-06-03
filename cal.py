def calculator():
    print("welcome to calculator ")

    try:
        num1=float(input("enter the first number: "))
        num2=float(input("enter the second number "))

        print("select an operation ")
        print("1 .Addition(+)")
        print(" 2. Subtraction(-)")
        print("3 Multiplication (*)")
        print("4. Division (/)")

        choice=input("enter your choice")

        if choice =="1":
            res=num1+num2
            print(f"\nResult ={res}")
        elif choice =="2":
            res=num1-num2
            print(f"\nResult :{res}")
        elif choice=="3":
            res=num1*num2
            print(f"result :{res}")
        elif choice =="4":
            
            if num2!=0:
                res=num1/num2
                print(f" result :{res}") 
            else:
                print("error cannot divide  by zero ")     

        else:
            print("Invalid operation ")
    except ValueError:
        print("invalid input")

calculator()        

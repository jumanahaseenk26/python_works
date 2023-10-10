while True:
    try:
        x=int(input("Enter the number:"))
        y=int(input("Enter the number: "))
        z=x/y
        print(z)
        break
    except ValueError:
        print("please enter a valid number")
    except ZeroDivisionError:
        print("Do not divisible by zero")
    except TypeError:
        print("Enter")
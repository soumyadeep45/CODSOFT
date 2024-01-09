# It is a simple calculator where user can calculate basic arithmetic operations of two numbers.

def addition(a, b) :
    return a + b 
    
def substraction (a, b) :
    return a - b 
    
def multiplication(a, b) :
    return a * b 
    
def division(a, b) :
    if b == 0 :
        return "You can not divide by zero"
    return a / b 

print("HEllO! WELCOME TO SIMPLE CALCULATOR.")    
print("Select a operation from below :")
print("""  Press "1" for Addition.""")
print("""  Press "2" for Substraction.""")
print("""  Press "3" for Multiplication.""")
print("""  Press "4" for Division.""")

while True:
    select = input("\nEnter opperation choice(1/2/3/4): ")

    if select in ('1', '2', '3', '4'):
        try:
            n1 = float(input("\nEnter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid Input. Please enter a number. ")
            continue
        if select == '1':
            print(n1 , "+" , n2 ,"=", addition(n1, n2))
        elif select == '2':
            print(n1 , "-", n2 , "=", substraction(n1, n2)) 
        elif select == '3':
            print(n1 , "*" , n2 , "=", multiplication(n1, n2))
        elif select == '4':
            print(n1, "/", n2 , "=", division(n1, n2))

        while True:
            calculate_again = input("\nWant to do another calculation?(Yes/No): ").lower()
            if calculate_again == 'yes':
                break
            if calculate_again == 'no':
                exit()
            else:
                print("Please enter 'Yes' or 'No'.") 
    else:
        print("Invalid Input. Please select a valid operation (1/2/3/4).")
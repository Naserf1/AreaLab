import math

def menu():
    print("1. Area of Rectangle")
    print("2. Perimeter of Rectangle")
    print("3. Area of Circle")
    print("4. Exit")
    pick = int(input("1,2,3, OR 4? "))
    return pick

def AreaRectangle(width,length):
    return int((width*length))
def PerimeterRectangle(widthh,lengthh):
    return int(2*(widthh+lengthh))
def AreaCircle(radius):
    return int(math.pi*(radius)*(radius))

def main():
    choice = menu()
    while choice != 4:
        if choice == 1:
                width = eval(input("Enter Width:"))
                length = eval(input("Enter Length:"))
                print (str(AreaRectangle(width,length)))
        elif choice == 2:
                widthh = eval(input("Enter Width:"))
                lengthh = eval(input("Enter Length:"))
                print (str(PerimeterRectangle(widthh,lengthh)))
        elif choice == 3:
                radius = eval(input("Enter radius:"))
                print (str(AreaCircle(radius)))
        else:
            print("invalid choice")
        choice = menu()
        
    

main()

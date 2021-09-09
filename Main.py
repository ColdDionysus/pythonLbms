import borrow
import Return

    
def starting():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Hello and Welcome to our library management system")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")

    print("The Available Books in our library are : \n")
    borrow.book_list()
    print("\n")
    while(True):
        
        print("Enter 1 to borrow a book: ")
        print("Enter 2 to return a book:  ")
        print("Enter 3 to exit")
        try:
            num = int(input("Enter a value here: "))
            
            if num == 1:
                borrow.borrowBook()
                borrow.book_list()
                    
            elif num == 2:
                
                Return.return_book()
                Return.book_list()
                

            elif num == 3:
                print("\n")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Thank You For Using Library Management System")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
                break

            else:
                print("\n")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Invalid Input detected! Please input valid Number")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
        except:
            print("\n")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Invalid Input detected! Please input valid Number")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++ \n")
        
        
    
starting()

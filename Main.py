import borrow
import Return

#the start function is the core function of the program
def start():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Library Management System ------------------------")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")

    print("The Available Books in our library are : \n")
    #here from borrow module the book_list() is helps in carrying the operation of showing the books.
    borrow.book_list()
    print("\n")
    while(True): #loops continues here
        
        print("Enter 1 to borrow a book: ")
        print("Enter 2 to return a book:  ")
        print("Enter 3 to exit")
        try:
            num = int(input("Enter a value here: "))
            #num takes the input from the user
            if num == 1:
                #borrow book function takes from the module borrow and helps in borrowing books
                borrow.borrowBook()
                #borrow book function takes from the module borrow and shows the book_list
                borrow.book_list()
                    
            elif num == 2:
                #while num ==2 it goes in the return section
                #return_book function takes from the module return
                Return.return_book()
                #return_book function takes from the module return and shows the book_list
                Return.book_list()
                

            elif num == 3:
                #while num ==3 the program exit with the following message.
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
        
        
    
start()

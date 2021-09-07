import borrow
import Return
import sys
    
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
        
        num = int(input("Enter a value here: "))
        
        if num == 1:
            loop=True
            while loop==True:
                
                borrow.borrowBook()
                borrow.book_list()
                
                
                break
            
            
            
            

        elif num == 2:
            print("You are in return \n")
            Return.return_book()
            Return.book_list()
            

        elif num == 3:
            sys.exit()
            
            

        else:
            print("\n")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Invalid Input detected! Please input valid Number")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++ \n")

        
    
starting()

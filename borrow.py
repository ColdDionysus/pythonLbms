import datetime
#this is the module of the datetime imported from the python library

def lists(): #the function lists helps in the file list from the Books.txt and returns it to the dictionary.
    file = open("Books.txt", "r")
    listBooks = []
    dictionary = {}
    for each in file:
        line = each.replace("\n", "")
        listBooks.append(line.split(","))
        for i in range(1, len(listBooks)+1):
            each = i
            dictionary[each] = listBooks[i-1]
    file.close()
    return dictionary #dictionary returns in the format from the key, value





#the function book_list returns the book list from the file and the lists() function where the list of book in tabular format is shown
def book_list():
    print("--------------------------------------------------------------------------------------")
    print("Book ID"+"      "+"Book Name"+"          "+" Author" +
          "                      "+"Quantity"+"    "+"Price")
    print("------------------------------------------------------------------------------------")
    listBooks = lists()
    for key, value in listBooks.items():
        print("  ", key, "       ",
              value[0], " ", value[1], "      ", value[2], "      ", value[3])
    print("------------------------------------------------------------------------------------")

#this function change_quantity while book is borrowed 
def change_quantity(val):
    listBooks = lists()
    quantity = int(listBooks[val][2])-1
    listBooks[val][2] = str(quantity).zfill(2)
    file = open("Books.txt", "w")
    for key, value in listBooks.items():
        file.write(value[0]+","+value[1]+","+value[2]+","+value[3]+"\n")
    file.close()
    print("Books ID: "+str(val) + "has been successfully borrowed")

#this function total is used to calculate the total value of the book from the file.
def total(I, val):
    listBooks = lists()
    price1 = (listBooks[I][3])
    price2 = (listBooks[val][3])
    p1 = float(price1.strip("$"))
    p2 = float(price2.strip("$"))
    total = round(p1+p2, 2)
    return str(total) #this returns total as a string
#this bill returns the bill in the text file 
def bill(name, I, ID, t, d):
    listBooks = lists()
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    second = str(datetime.datetime.now().second)
    
    with open("Borrow-"+name+""+year+""+month+""+day+""+second+".txt", "w+") as f:
        f.write("+++++++++++++++++++++++++++++++++++ \n")
        f.write("    Library Management System       \n")

        f.write("\n Book is borrowed by: "+name+"\n")
        f.write("The time of borrowed book is: "+t+"\n")
        f.write("The date of borrowed book is : "+d+"\n")
        f.write("The borrowed book is: "+listBooks[I][0])
        f.write(", "+listBooks[ID][0]+", ")

# this function borrowBook() helps in the borrowing of the book in the list file and updates in the book list
def borrowBook():
    try:
        I = int(input("Enter ID of the book you want to borrow: "))
        
        listBooks = lists()
        if I >= 0 and I <= 5:
            if int(listBooks[I][2]) > 0:
                print("\n+++++++++++++++++++++")
                print("Book is available")
                print("+++++++++++++++++++++ \n")

                name = input(
                    "Enter the name of person who want to borrow the books: ")
                change_quantity(I) #this change quantity and I pass to change quantity function
                
        
                dt = datetime.datetime.now()
                t = dt.strftime("%H:%M:%S")
                d = dt.strftime("%d/%m/%Y")
                s = 0

                
                while(True):
                    YesNo = input(
                        "If 'Yes' please enter 'Y' or No for 'N' to cancel this borrowing process")

                    if YesNo == "y" or YesNo == "Y":

                        s = s+1
                        ID = int(
                            input("Enter id of the book that you want to borrow: "))
                        # validation(ID)
                        listBooks = lists()
                        if ID >= 0 and ID <= 5:
                            if int(listBooks[ID][2]) > 0:
                                print("\n +++++++++++++++++++++")
                                print("Book is available")
                                print("+++++++++++++++++++++ \n")
                                change_quantity(ID)
                                bill(name, I, ID, t, d)

                                

                                print("\n")
                                total(I, ID)
                                
                                

                            else:
                                print("\n")
                                print("Book is not available")
                                print("\n")
                        else:
                            print("\n")
                            print("Please Provide a valid number")
                            print("\n")
                    else:
                        print("\n \n")
                        print("Thank You "+name+" For Borrowing Books")
                        break

                        
            else:
                print("\n")
                print("Book is not available")
                print("\n")
        else:
            print("\n")
            print("Please Provide a valid number")
            print("\n")
    
    except:
        print("\n")
        print("++++++++++++++++++++++++++++++++++++++")
        print("Invalid Input detected")
        print("++++++++++++++++++++++++++++++++++++++")

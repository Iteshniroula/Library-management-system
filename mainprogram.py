import os
import datetime
import display


name_of_BOOKS=[]    # creating empty list
Total_price=[]
return_price=[]          
return_bookName=[]
# creating class
class LMS(display.Display): # using interface
     
    def __init__(self,name_of_the_books):  # creating constructor
        self.name_of_the_books="List_of_the_books.txt"
        self.liabry_dictionary={}   # creating empty dictionary to store booname,bookauthor,quantity,price.
        book_id=1001  # declearing Id for unique book_id
        with open("List_of_the_books.txt","r") as f:   # opening txt file
            txt=f.readlines()  # reading text file and readlines convert txt in list
        for i in txt:
            content=i.split(",") # spliting txt by comma
            self.liabry_dictionary.update({str(book_id):{"BookTitle": content[0], "BookAuthor" : content[1],"Quantity_of_books" : content[2],"Price_of_books" : content[3]}})
            book_id=book_id+1


    
    


    def display_for_lend_and_borrow(self):   ## displaying book for lend and borrow
        print("------------------Book list---------------------------")
        print ("BookID","\t","BookTitle")
        for keys,value in self.liabry_dictionary.items():
           print(keys,"\t\t",value.get("BookTitle"))


    def lend_book(self):  # creating function to lend books
        book_ID=input("Enter the book_ID you wanna lend:  ")  
        if int(book_ID) <0:  # checking whether the book id is negative or not
            print("The book_id you entered is negative")
        else:
            if book_ID in self.liabry_dictionary.keys():
                if (int(self.liabry_dictionary[book_ID]["Quantity_of_books"] ) > 0):
                    name_of_lender= str(input("Enter your name: "))
                    adress_of_lender = input("Enter you adress: ")
                    bookName=self.liabry_dictionary[book_ID]["BookTitle"]
                    name_of_BOOKS.append(bookName)
                    date_time = datetime.datetime.now()
                    price=int(self.liabry_dictionary[book_ID]["Price_of_books"])
                    Total_price.append(price)
                    t=0
                    for price_of_each_book in range(0,len(Total_price)):
                        t=t+Total_price[price_of_each_book]

   
                    update_read=open("List_of_the_books.txt","r")
                    update_write=open("tempory_file.txt","w")
                    Quantity=int(self.liabry_dictionary[book_ID]["Quantity_of_books"])
                    choose=" "
                    while(choose):
                        choose=update_read.readline()
                        spl=choose.split(",")
                        if len(choose)>0:
                            if (spl[0]== str(self.liabry_dictionary[book_ID]["BookTitle"] )):
                                bookname=self.liabry_dictionary[book_ID]["BookTitle"]
                                book_author=self.liabry_dictionary[book_ID]["BookAuthor"]
                                book_quantity=Quantity-1
                                bprice=self.liabry_dictionary[book_ID]["Price_of_books"]
                                update_write.write(bookname+","+book_author+","+str(book_quantity)+","+bprice)
                            else:
                                update_write.write(choose)
                    update_read.close()
                    update_write.close()
                    os.remove("List_of_the_books.txt")
                    os.rename("tempory_file.txt","List_of_the_books.txt")
    #A Borrow Note is provided after borrowing the books
                    
                    borrow_write=open("BorrowNote.txt","w")
                    borrow_write.write("\n")
        
                    borrow_write.write("Name of the person :" +str( name_of_lender)+"\n")
                    borrow_write.write("+++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    borrow_write.write("Adress of lender is: "+ str(adress_of_lender)+"\n")
                    borrow_write.write("+++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    borrow_write.write("Issued date and time is :" + str(date_time)+"\n")
                    borrow_write.write("+++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    borrow_write.write("==========================================================\n")
                    borrow_write.write("Total price of the book you lend is : "+str(t)+"$"+"\n")
                    borrow_write.write("+++++++++++++++++++++++++++++++++++++++\n The book you lend is : ")
                    for i in range (len(name_of_BOOKS)):
                        borrow_write.write(str(name_of_BOOKS[i])+"\n")
                    borrow_write.close()
                    more=input ("Do you want more Books[Yes or NO]: ")
                    asking=more.lower()
                    if (asking=="yes"):
                        print("Thanks for lending the book "+bookName+"\t on "+str(date_time))
                        return self.lend_book()
                    elif(asking=="no"):
                        print("Thanks for lending the book "+bookName+"\t on "+str(date_time))
                    else:
                        print("Error in choosing the value.Please choose carefully")
                    
                else:
                    print("The bookName is out of stock")
            else:
                print("The code you entered is wrong.Please try again")
                return self.lend_book()
            
           
# creating function to perform return_book

    def Return_book(self):
        return_book_ID=input("Please enter the code of the bookName you want to return:")
        Days=int(input("Enter the number of Days you have borrowed the books for:"))
        if int(return_book_ID)<0:
            print("The book_id you entered is negative")
        else:
            if return_book_ID in self.liabry_dictionary.keys():
                name_of_lender= str(input("Enter Your Full Name: "))
                bookName=self.liabry_dictionary[return_book_ID]["BookTitle"]
                return_bookName.append(bookName)
                price=int(self.liabry_dictionary[return_book_ID]["Price_of_books"])
                date_time = datetime.datetime.now()
                return_price.append(price)
                reutrn_total=0
                for price_of_each_book in range(0,len(return_price)):
                    reutrn_total=reutrn_total+return_price[price_of_each_book]
                # for fine
                fineday=0
                if (Days>10):
                    print("Fine is charged because you are late returning the book.")
                    fineday=Days-10
                    fineprice=(1/10)*reutrn_total*fineday
                elif (Days<=10):
                    print("The book was returned on time, and I hope you have a great time.")
                    fineprice=0
                else:
                    print("The input you have entered is wrong.")
                    return self.Return_book()

                GandTotal=reutrn_total+fineprice
    
                return_write=open("ReturnNote.txt","w")
                return_write.write("---------------------------Book Return Notice----------------------------------------------\n")
                return_write.write("\n")
                return_write.write("Name of the person :" +str( name_of_lender)+"\n")
                return_write.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                return_write.write("Issued date and time is :" +str(date_time)+"\n")
                return_write.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                return_write.write("Fine for the book is :"+str(fineprice)+"$"+"\n")
                return_write.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                return_write.write("Total price: "+str(GandTotal)+"$"+"\n")
                return_write.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                return_write.write("Books Returned by lender is: \n")
                for i in range (len(return_bookName)):
                    return_write.write(str(return_bookName[i])+"\n")
                return_write.close()
  ## updating the quantity
                return_read=open("List_of_the_books.txt","r")
                return_write=open("tempory_file.txt","w")
                Quantity=int(self.liabry_dictionary[return_book_ID]["Quantity_of_books"])
                choose=" "
                while(choose):
                    choose=return_read.readline()
                    returnsplit=choose.split(",")
                    if len(choose)>0:
                        if (returnsplit[0]== str(self.liabry_dictionary[return_book_ID]["BookTitle"] )):
                            return_book_Name=self.liabry_dictionary[return_book_ID]["BookTitle"]
                            return_author=self.liabry_dictionary[return_book_ID]["BookAuthor"]
                            return_quantity=Quantity+1
                            return_PRICE=self.liabry_dictionary[return_book_ID]["Price_of_books"]
                            return_write.write(return_book_Name+","+return_author+","+str(return_quantity)+","+return_PRICE)
                        else:
                            return_write.write(choose)
                return_read.close()
                return_write.close()
                os.remove("List_of_the_books.txt")
                os.rename("tempory_file.txt","List_of_the_books.txt")
            
                more=input ("Do you have other books to retrun[YES or NO]: ")
                asking=more.lower()
                if (asking=="yes"):
                    return self.Return_book()
                elif(asking=="no"):
                    print("Book Return is sucessfully done\n thank you")
                else:
                    print("You made some error while choosing,check it out once")
            else:
                print("The bookID you are returing is not correct")
                return self.Return_book()
            
# main function
    def main():
        while(True):
            print("---------------------------Welcome to Libary Mangement System---------------------------")
            print("------------------------------------------------------------------------------------------------------------")
            print("--------------------------Choose press key to perform-----------------------------------")
            print("Press D for display Books")
            print("Press L for lend_book books")
            print("Press R for return lended books")
            print("Press Q for quit the program")
     # try and expept       
            try:
                choose=input("Enter the key to choose: ")
                print()
                content=choose.lower()
                if (content=="d"):
                   print("You choose to display books")
                   display.Display.display_all_books(self=display.Display)
                elif(content=="l"):
                    print("You choose to lend books")
                    constuctor.display_for_lend_and_borrow()
                    constuctor.lend_book()
                elif (content=="r"):
                    print("You choose to return books")
                    constuctor.display_for_lend_and_borrow()

                    constuctor.Return_book()
                elif(content=="q"):
                     
                     print("Thnaks for visiting our Libiary. keep coming")
                     exit()
                else:
                    print("Please Enter the valid press key")
            except ValueError:
                print("The input is incorrcet.")
 
                print("Please Enter correct input")
# calling constuctor
constuctor=LMS("List_of_the_books.txt")



# call main function
LMS.main()

    

            

class Display():
    def display_all_books(self):
        print("------------------List of all bookname , author , quantity and  price ---------------------------")
        with open("List_of_the_books.txt") as f:
            txt = f.read()
        print(txt)

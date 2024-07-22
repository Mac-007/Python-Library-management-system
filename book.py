# Global list to store books

import pandas as pd

class book_management():
    
    def __init__(self,CSV_path):
        #self.title=title
        #self.author=author
        #self.isbn=isbn
        self.CSV_path=CSV_path
        self.df = pd.read_csv(self.CSV_path)

    def add_book(self,title,author,isbn):
        #df=pd.read_csv(self.CSV_path)
        print("title=",title)
        
        if isbn in self.df["ISBN"].values:
            print(f"{isbn} ISBN already exist !!")
        else:
            new_row = {"title": title, "author":author,"ISBN":isbn}
            self.df.loc[len(self.df)] = new_row
            self.df.to_csv(self.CSV_path, index=False)
                   
            print(f"{title} book added !!")
        
    def list_books(self):
        print("List of Books:")
        for index, row in self.df.iterrows():
            isbn = row['ISBN']
            if '#' not in isbn:
                print(f"Title: {row['title']}, Author: {row['author']}, ISBN: {isbn}")



    

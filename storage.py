import pandas as pd
import os

class storage_management():
    def __init__(self,user_details_csv,books_record_details_csv):
        self.user_details_csv=user_details_csv
        self.books_record_details_csv=books_record_details_csv
    
    def check_user_details(self):
        if os.path.isfile(self.user_details_csv):
            print("User CSV Database found")
        else:
            print("User CSV Database not found. Creating...")
            df = pd.DataFrame(columns=["User ID","Username", "password","Issued Books"])
            df.to_csv(self.user_details_csv, index=False)
            print("User CSV Database created.")
    
    def check_book_details(self):
        if os.path.isfile(self.books_record_details_csv):
            print("Books CSV Database found")
        else:
            print("Books CSV Database not found. Creating...")
            df = pd.DataFrame(columns=["title", "author","ISBN"])
            df.to_csv(self.books_record_details_csv, index=False)
            print("Books CSV Database created.")
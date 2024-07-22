
import pandas as pd

class User_details():
    def __init__(self,username,user_id,CSV_Path):
        self.username=username
        self.user_id=user_id
        self.CSV_Path=CSV_Path
        
    def encrypt(self,text, key):
        encrypted_text = ""
        for char in text:
            encrypted_text += chr(ord(char) ^ key)
        return encrypted_text

    def decrypt(encrypted_text, key):
        decrypted_text = ""
        for char in encrypted_text:
            decrypted_text += chr(ord(char) ^ key)
        return decrypted_text
    
    def user_check(self):
        pass
    
    def add_user(self):
        df=pd.read_csv(self.CSV_Path)
        
        if self.username in df["Username"].values:
            print(f"{self.username} Username already exist !!")
        else:
            password = input("Enter user Password: ")
            while not password.strip():  # Check if the input is empty or blank
                print("password cannot be empty or blank.")
                password = input("Enter user Password: ")
            
            password=self.encrypt(password,10)
            
            new_row = {"User ID":self.user_id,"Username": self.username, "password":password}
            df.loc[len(df)] = new_row
            df.to_csv(self.CSV_Path, index=False)
                   
            print(f"{self.username} User created !!")
    
    
    def update_user(self):
        pass
    






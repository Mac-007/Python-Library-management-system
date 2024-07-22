import pandas as pd

class check_out():
    
    def __init__(self,user_id,isbn,user_details_csv,books_record_details_csv):
        self.user_id=user_id
        self.isbn=isbn
        self.user_details_csv=user_details_csv
        self.books_record_details_csv=books_record_details_csv
        self.df1=pd.read_csv(self.user_details_csv)
        self.df2=pd.read_csv(self.books_record_details_csv)
        
    def checkout_book(self):
        idx_user = self.df1.index[self.df1['User ID'] == int(self.user_id)].tolist()
        print(self.isbn)
        isbn_dtype = self.df2['ISBN'].dtype
        print("Data type of ISBN column in df2:", isbn_dtype)

        idx = self.df2.index[self.df2['ISBN'] == self.isbn].tolist()
        print(idx)
      
        if idx_user:
            if idx:
                row_idx_user = idx_user[0]
              
                values_to_append = [self.isbn] 
                existing_value = self.df1.at[row_idx_user, 'Issued Books']
                
                if isinstance(existing_value, str):
                    updated_value = existing_value + ', ' + ', '.join(values_to_append)
                else:
                    updated_value = ', '.join(values_to_append)
                
                # Update the DataFrame with the new value
                self.df1.at[row_idx_user, 'Issued Books'] = updated_value
                
                # Write the modified DataFrame back to the CSV file
                self.df1.to_csv(self.user_details_csv, index=False)
                print(f"Added ISBN {self.isbn} to the 'Issued Books' of User ID {self.user_id}")
                
                row_idx = idx[0]
                self.df2.loc[row_idx, 'ISBN'] = '#' + self.isbn
               
                self.df2.to_csv(self.books_record_details_csv, index=False)
                #print(f"Marked book record with ISBN {isbn} with '#'")
            else:
                print(f"Book record with ISBN {self.isbn} not found")
        else:
            print(f"User with ID {self.user_id} not found") 
            
        
          
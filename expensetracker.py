import csv
import os
from datetime import datetime


file_name = "expenses.csv"

if not os.path.exists(file_name):

   with open(file_name,'w', newline='') as file:
     
        writer= csv.writer(file)
        writer.writerow(["ID","DATE","AMOUNT","CATAGORY","DESCRIPTION"])

def addexpenses():
    date=input("Enter the date in format of (YYYY-MM-DD) or press enter to add todays date:")     

    if not date:
       date= datetime.today().strftime('%Y-%m-%d')
       amount=input("Enter amount:")
       catagory=input("Enter the catagory (eg Fun,Food etc):")
       discription=input("Enter the discription:")


       with open(file_name,'r') as file:
         line=list(csv.reader(file))
         next_id=len(line)

       with open(file_name,'a',newline='') as file:
         writer= csv.writer(file)
         writer.writerow([next_id,date,amount,catagory,discription])
         
    print("Exicuted successfully")
   
def viewexpenses():

     with open(file_name,'r') as file:

        reader=csv.reader(file) 

        for row in reader:
           print(f"{row[0]:<5}{row[1]:<15}{row[2]:<15}{row[3]:<25}{row[4]}")

def deleteexpenses():
   
   viewexpenses()

   del_id=input("Enter the id of row to be deleated:")

   updated_list=[]  
   deleted = False          

   with open(file_name,'r') as file:
       
       reader= csv.reader(file)

       
       for row in reader:
           
           if row[0] != del_id:
              updated_list.append(row)
           else:
               deleted = True   
  
   with open(file_name,'w') as file:
      
        writer= csv.writer(file)
        writer.writerows(updated_list)


   if deleted:
      print("The Expanse has been deleated")
   else:
      print("The expanse has not been found")  

         
def main():

   while True:

      print("\n___Expense_tracker____")     
      print("1.Add expenses")
      print("2.view expenses")
      print("3.Delete expenses")
      print("4.Exit")
    
      choise=input("Enter the choise:")
   
      if choise == "1":
       addexpenses()
      elif choise =="2":
       viewexpenses()
      elif  choise == "3":
        deleteexpenses()
      elif choise == "4":
         print("Exiting expense traker")
         break
      else:
        print("invalid option")     
                 
if __name__=="__main__":
   main()
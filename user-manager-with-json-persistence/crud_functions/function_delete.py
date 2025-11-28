
import sys
from crud_functions.class_function import Delete
from colors import red, yellow, blue, cyan, white, reset 

def Eliminar():
    
    while True:
        print(f"\n{blue}=============================={reset}")
        print(f"\n{cyan}1.{reset} {white}Delete a user{reset}")
            
        print(f"\n{blue}=============================={reset}")
        delete_1 = input(f"\n{white}Do you want to {yellow}delete{reset} a user? y/n:{reset} ")
            
        if delete_1 == "y":
            
            data_user = int(input("Delete with index: "))
            
            delete = Delete("json_storage\\users.json")
            delete = delete.deleteusers(data_user)
          
            print(f"\n{white}The user '{data_user}' has been{reset} {red}deleted.{reset}")
                    
        elif delete_1 == "n":   
            print(f"\n{cyan}1.{reset} {white}Return to the main menu{reset}")
            print(f"{cyan}2.{reset} {white}Exit the application{reset}") 
            selection = input(f"\n{white}What would you like to do?:{reset} ")
            match selection:
                case "1":
                    break
                case "2":
                    print(f"\n{yellow}See you soon!{reset}\n")
                    sys.exit()
            
                      
if __name__ == "__main__":
    Eliminar()
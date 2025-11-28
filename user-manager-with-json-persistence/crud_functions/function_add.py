import sys
from crud_functions.class_function import Add
from crud_functions.models import Users
from colors import  yellow, blue, cyan, white, reset
def Agregar():
    
    while True:  
        print(f"\n{blue}=============================={reset}")
        user_1 = input(f"\n{white}Do you want to{reset} {yellow}create{reset} {white}a new user? y/n:{reset} ")
        if user_1 == "y":
            print("Order is: id,name,lastname,age,country,skills,role,active")
            data_user = input("Introduce los datos del usuario en el orden descrito anteriormente: ")
            id,na,las,age,con,sk,ro,ac = data_user.split(",")
            user = Users(id.strip(),na.strip(),las.strip(),int(age.strip()),con.strip(),sk.strip(),ro.strip(),ac.strip())
            añadir = Add("json_storage\\users.json")
            añadir = añadir.addUser(user)
            confirmation_user_data = input("User agregado exitosamente.¿Quieres ver los datos? y/n: ")
            if confirmation_user_data == "y":
                print(data_user)
                 
            elif confirmation_user_data == "n":
                pass
            
        elif user_1 == "n":
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
    Agregar()
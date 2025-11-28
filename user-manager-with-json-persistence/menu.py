from colors import yellow, blue, cyan, white, reset
from crud_functions import function_add as fun_add, function_view as fun_view, function_complete as fun_com, function_delete as fun_del 


def Menu():
    
    while True:
        print(f"\n{blue}=============================={reset}")
        print(f"{white}Welcome! What would you like to do?{reset}")
        print(f"{blue}======={reset}{white}INTERACTIVE MENU{reset}{blue}======={reset}\n")
        
        print(f"{cyan}1.{reset} {white}Add User{reset}")
        print(f"{cyan}2.{reset} {white}View User{reset}")
        print(f"{cyan}3.{reset} {white}User Active {reset}")
        print(f"{cyan}4.{reset} {white}Delete User{reset}")
        print(f"{cyan}5.{reset} {white}Exit{reset}")
        opcion = input(f"\n{white}Select an option:{reset} ")
        match opcion:
            case "1":
                fun_add.Agregar()
            case "2":
                print(f"\n{blue}=============================={reset}")
                print(f"\n{white}Program users are:{reset} ")
                fun_view.Ver()
            case "3":
                fun_com.modify_user()
                
            case "4":
                fun_del.Eliminar()
            case "5": 
                print(f"\n{yellow}See you soon!{reset}\n")
                break
if __name__ == "__main__":
    Menu()  
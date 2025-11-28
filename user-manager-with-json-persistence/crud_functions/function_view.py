import sys
from crud_functions.class_function import View
from colors import yellow, cyan, white, reset

def Ver():
    
    print("\n")
    print("1.VIew all users")
    print("2.View user for index")
    view_decision = input("What would you like to do?: ")
    
    if view_decision == "1":
        
        view  = View("json_storage\\users.json")
        view = view.viewusers()
        print(view)
        
    elif view_decision == "2":
        
        index_view = int(input("\nWrite teh index for view user: "))
        view  = View("json_storage\\users.json")
        view = view.viewusers(index_view)
        print(view)
        
    print(f"{cyan}1.{reset} {white}Return to the main menu{reset}")
    print(f"{cyan}2.{reset} {white}Exit the application{reset}")
    selection = input(f"\n{white}What would you like to do?:{reset} ")
    
    match selection:
        case "1":
            return
        case "2":
            print(f"\n{yellow}See you soon!{reset}\n")
            sys.exit()
            
if __name__ == "__main__":
    Ver()
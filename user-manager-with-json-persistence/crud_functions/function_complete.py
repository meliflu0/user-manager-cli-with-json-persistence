import sys
from crud_functions.class_function import Modify
from colors import green, yellow, blue, cyan, white, reset 
def modify_user():
  
    while True:
        print(f"\n{blue}=============================={reset}")
        complete = input(f"\n{white}Did you {yellow}modify{reset} a user? y/n:{reset} ")
    
        if complete == "y":
            data_user = input("Modify in this order with ',': index/caracteristic/content.\n\nExmple 0,id,3\n\n")
            index_json,caracteristic,content = data_user.split(",")
            
            modify_progress = Modify("json_storage\\users.json")
            modify_progress = modify_progress.modifyusers(index=int(index_json.strip()),value=caracteristic.strip(),key=content.strip())
          
            print(f"\n{white}User '{index_json}'{reset} {green}modify succesfully.{reset}")
        elif complete == "n":   
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
    modify_user()        
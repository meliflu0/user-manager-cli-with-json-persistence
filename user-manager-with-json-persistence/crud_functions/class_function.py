from crud_functions.models import DataBase


class Add(DataBase):
    def addUser(self,data):
        self.data["users"].append(data.estructure_db())
        
        self.dumpJsonDb()
        
class View(DataBase):    
    def viewusers(self, index=None):
        user = self.data["users"]
        
        if  index is None:
            return user
        elif index < 0 or index >= len(user):
            return f"Error: índice {index} fuera de rango"
        return user[index]

    
class Delete(DataBase):
    def deleteusers(self,index=None):
       user = self.data["users"]
       
       if  index is None:
          return user
       elif index < 0 or index >= len(user):
          return f"Error: índice {index} fuera de rango"
       
       user = user.pop(index)
       self.dumpJsonDb()
       return f"Usuario eliminado: "    

class Modify(DataBase):
    def modifyusers(self,index=None,key=None,value=None):
        user = self.data["users"]
        
        if  index is None:
          return user
        elif index < 0 or index >= len(user):
          return f"Error: índice {index} fuera de rango"
      
        user = user[index]
        
        user[key]=value
        if key not in user:
            return F"Error de valor"
        self.dumpJsonDb()
      

        
# usr = Users("2","sebastian","calderon",20,"colombia","mamon","joder")
# añadir = Add("json_storage\\users.json")
# añadir.addUser()

#print(usr.estructure_db())
# view  = View("json_storage\\users.json")
# view = view.viewusers(1)

# delete = Delete("json_storage\\users.json")
# delete = delete.deleteusers(0)
# print(delete)

# delete = Modify("json_storage\\users.json")
# delete = delete.modifyusers(index=0,value="active",key="online")

# print(delete)

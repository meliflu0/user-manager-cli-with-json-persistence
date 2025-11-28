
class Users:
    def __init__(self,id,name,lastname,age,country,skills,role,active):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.country = country
        self.skills = skills
        self.role = role
        self.active = active
    def estructure_db(self):
        return  {
        "id" : self.id,
        "name" : self.name,
        "lastname" : self.lastname,
        "age" : self.age,
        "country" : self.country,
        "Skills" : self.skills,
        "role" : self.role,
        "active" : self.active
        }        
class DataBase:
    def __init__(self,archivo):
        self.archivo = archivo
        self.data = self.loadJsonDb()
        
    def loadJsonDb(self):
        import json
        with open(self.archivo,"r", encoding="UTF=8") as user_file:
            return  json.load(user_file)
    
    def dumpJsonDb(self):
        import json
        with open(self.archivo,"w", encoding="UTF=8") as user_file:
            json.dump(self.data, user_file, indent=4, ensure_ascii=False)
             
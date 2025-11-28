def delete_by_id(self, user_id):
    users = self.data["users"]

    for i, user in enumerate(users):
        if user.get("id") == str(user_id):
            deleted = users.pop(i)
            self.save()
            return f"Usuario eliminado: {deleted}"

    return f"No existe usuario con id {user_id}"


def delete_by_id(self, value=None,key=None):
    users = self.data["users"]

    for i, user in enumerate(users):
        if user.get(value) == str(key):
            deleted = users.pop(i)
            self.save()
            return f"Usuario eliminado: {deleted}"

    return f"No existe usuario con id {key}"



data_user = input("Delete in this order with ',': index/caracteristic/content.\n\nExmple 0,id,3")
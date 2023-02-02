# coding:utf-8
from practice_9_12_01 import User


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("-" + privilege)
        else:
            print("- This user has no privileges.")


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super(Admin, self).__init__(first_name, last_name, username, email, location)
        # super().__init__(first_name, last_name, username, email, location)

        self.privileges = Privileges()



from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDTextButton

from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem
from kivy.properties import StringProperty

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file("screen1.kv")  
    def build(self):
        return self.screen

    # def on_start(self):
    #     self.fps_monitor_start()

    def add(self):
        # accepting input from the user
        username = self.screen.ids.username.text
        password = self.screen.ids.password.text
        # accepting password input from the user
        if username and password:
            with open("passwords.txt", 'a') as f:
                f.write(f"{username} {password}\n")
            
            print("data saved")
            # messagebox.showinfo("Success", "Password added !!")
            self.dialog = MDDialog(
                title="Success",
                type="simple",
                text =  "Password added !!"
            )
            self.dialog.open()

        else:
            # messagebox.showerror("Error", "Please enter both the fields")
            # print("Please enter both the fields")
            self.dialog = MDDialog(
                title="Error",
                type="simple",
                text = "Please enter both the fields"
            )
            self.dialog.open()

    
    def get(self):
        # accepting input from the user
        username = self.screen.ids.username.text

        # creating a dictionary to store the data in the form of key-value pairs
        passwords = {}
        try:
            # opening the text file
            with open("passwords.txt", 'r') as f:
                for k in f:
                    i = k.split(' ')
                    # creating the key-value pair of username and password.
                    passwords[i[0]] = i[1]
        except:
            # displaying the error message
            print("ERROR !!")

        if passwords:
            mess = "Your passwords:\n"
            for i in passwords:
                if i == username:
                    mess += f"Password for {username} is {passwords[i]}\n"
                    break
            else:
                mess += "No Such Username Exists !!"
            print("Passwords", mess)
            self.dialog = MDDialog(
                title="Passwords",
                type="simple",
                text = mess
            )
            self.dialog.open()

            # messagebox.showinfo("Passwords", mess)
        else:
            # messagebox.showinfo("Passwords", "EMPTY LIST!!")
            print("Passwords", "EMPTY LIST!!")
            self.dialog = MDDialog(
                title="Passwords",
                type="simple",
                text = "EMPTY LIST!!"
            )
            self.dialog.open()


    def getlist(self):
        # creating a dictionary
        passwords = {}

        # adding a try block, this will catch errors such as an empty file or others
        try:
            with open("passwords.txt", 'r') as f:
                for k in f:
                    i = k.split(' ')
                    passwords[i[0]] = i[1]
        except:
            print("No passwords found!!")

        if passwords:
            mess = "List of passwords:\n"
            for name, password in passwords.items():
                # generating a proper message
                mess += f"Password for {name} is {password}\n"
            # Showing the message
            # messagebox.showinfo("Passwords", mess)
            self.dialog = MDDialog(
                title="Passwords",
                type="simple",
                text = mess
            )
            self.dialog.open()
        else:
            # messagebox.showinfo("Passwords", "Empty List !!")
            self.dialog = MDDialog(
                title="Passwords",
                type="simple",
                text ="Empty List !!"
            )
            self.dialog.open()


    def delete(self):
        # accepting input from the user
        username =  self.screen.ids.username.text

        # creating a temporary list to store the data
        temp_passwords = []

        # reading data from the file and excluding the specified username
        try:
            with open("passwords.txt", 'r') as f:
                for k in f:
                    i = k.split(' ')
                    if i[0] != username:
                        temp_passwords.append(f"{i[0]} {i[1]}")

            # writing the modified data back to the file
            with open("passwords.txt", 'w') as f:
                for line in temp_passwords:
                    f.write(line)

            # messagebox.showinfo(
            #     "Success", f"User {username} deleted successfully!")
            self.dialog = MDDialog(
                title= "Success",
                type="simple",
                text =f"User {username} deleted successfully!"
            )
            self.dialog.open()
        except Exception as e:
            # messagebox.showerror("Error", f"Error deleting user {username}: {e}")
            self.dialog = MDDialog(
                title= "Error",
                type="simple",
                text = f"Error deleting user {username}: {e}"
            )
            self.dialog.open()

MainApp().run()
import tkinter as tk
from form import SearchForm
from controls import UsersControl


root = tk.Tk()
# root.title = ("SEARCH FORM")
root.geometry("300x400")

control = UsersControl("test_db.db")
search_form = SearchForm(root, control)


root.mainloop()


#нужно создать форму, куда сами добавляем пользователя
# добавить пользователя в БД
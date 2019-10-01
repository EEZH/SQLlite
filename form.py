import tkinter as tk


class SearchForm(tk.Frame):
    def __init__(self, master=None, service=None):
        super().__init__(master)
        self.service = service
        self.pack()
        self.render_form()
        self.result_field = self.render_result([])

    def render_result(self, result):
        field = tk.Frame(self)
        field.pack()

        for user in result:
            user_str = f"name: {user[1]}; surname: {user[2]}; age: {user[3]}"
            row = tk.Label(field, text=user_str)
            row.pack()

        return field

    def render_form(self):
        form = tk.Frame(self)
        form.pack()

        input_search = tk.Entry(form)
        input_search.pack(side=tk.RIGHT)

        btn_search = tk.Button(form, text="Search", command=lambda: self.search(input_search))
        btn_search.pack(side=tk.RIGHT)

        btn_add = tk.Button(form, text="Add user", command=lambda: self.add_user_render())
        btn_add.pack(side=tk.TOP)

    def search(self, input_search):
        query = input_search.get()
        result = self.service.search_match_users_by_name(query)
        self.result_field.destroy()

        self.result_field = self.render_result(result)

    def add_user_render(self):
        top_window = tk.Toplevel()
        top_window.geometry("300x200")
        top_window.title = ("Add user")

        lbl_main = tk.Label(top_window, text="Введите информацию:").grid(sticky="W", row=0, column=0, columnspan=3)

        input_name = tk.Entry(top_window)
        input_name.grid(sticky="W", row=1, column=1)
        lbl_name = tk.Label(top_window, text="Имя:").grid(sticky="W", row=1, column=0)

        input_surname = tk.Entry(top_window)
        input_surname.grid(sticky="W", row=2, column=1)
        lbl_surname = tk.Label(top_window, text="Фамилия:").grid(sticky="W", row=2, column=0)

        input_age = tk.Entry(top_window)
        input_age.grid(sticky="W", row=3, column=1)
        lbl_age = tk.Label(top_window, text="Возраст:").grid(sticky="W", row=3, column=0)

        input_email = tk.Entry(top_window)
        input_email.grid(sticky="W", row=4, column=1)
        lbl_email = tk.Label(top_window, text="e-mail:").grid(sticky="W", row=4, column=0)

        input_mobile = tk.Entry(top_window)
        input_mobile.grid(sticky="W", row=5, column=1)
        lbl_mobile = tk.Label(top_window, text="№ телефона:").grid(sticky="W", row=5, column=0)

        btn_accept_user = tk.Button(top_window, text="Accept", command=lambda: self.on_click(
            input_name, input_surname, input_age, input_email, input_mobile, root=top_window))
        btn_accept_user.grid(row=7, column=1)

        return top_window

    def add_user(self, input_name, input_surname, input_age, input_email, input_mobile):
        query_name = input_name.get()
        query_surname = input_surname.get()
        query_age = input_age.get()
        query_email = input_email.get()
        query_mobile = input_mobile.get()

        result = self.service.add_user(query_name, query_surname, query_age, query_email, query_mobile)

        return result

    def close_window(self, root):
        root.destroy()

    def on_click(self, input_name, input_surname, input_age, input_email, input_mobile, root):
        self.add_user(input_name, input_surname, input_age, input_email, input_mobile)
        self.close_window(root)
        self.result_field.destroy()
        self.result_field = self.render_add_result(self.service.last_row())



    def render_add_result(self, user):
        field = tk.Frame(self)
        field.pack()
        anounce = tk.Label(field, text="Добавлен пользователь:")
        anounce.pack()
        user_str = f"name: {user[1]}; surname: {user[2]}; age: {user[3]}"
        row = tk.Label(field, text=user_str)
        row.pack()

        # self.result_field.destroy()
        # self.result_field = self.render_add_result()

        return field

        # self.result_field.destroy()
        # user = self.service.last_row()
        # self.result_field = self.render_result(result)



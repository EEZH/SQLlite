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
            user_str= f"name: {user[1]}; surname: {user[2]}; age: {user[3]}"
            row = tk.Label(field,text=user_str)
            row.pack()

        return field

    def render_form(self):
        form = tk.Frame(self)
        form.pack()

        input_search = tk.Entry(form)
        input_search.pack(side=tk.RIGHT)

        btn_search = tk.Button(form, text="Search", command=lambda :self.search(input_search))
        btn_search.pack(side=tk.RIGHT)


    def search(self, input_search):
        query = input_search.get()
        result = self.service.search_match_users_by_name(query)
        self.result_field.destroy()

        self.result_field = self.render_result(result)




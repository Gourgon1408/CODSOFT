import tkinter as tk
from tkinter import messagebox
import csv

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def update_task(self, index, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = description

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def toggle_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = not self.tasks[index].completed

    def save_tasks(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task.description, task.completed])

    def load_tasks(self, filename):
        try:
            with open(filename, 'r', newline='') as file:
                self.tasks = []
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        description, completed = row
                        task = Task(description)
                        task.completed = completed == 'True'
                        self.tasks.append(task)
        except FileNotFoundError:
            pass

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.todo_list = ToDoList()
        self.todo_list.load_tasks("tasks.txt")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, pady=10)
        self.task_listbox.bind("<Double-1>", self.toggle_task_completed)

        self.update_button = tk.Button(self.frame, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=0, pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, pady=5)

        self.load_tasks()

    def add_task(self):
        description = self.task_entry.get()
        if description:
            self.todo_list.add_task(description)
            self.task_entry.delete(0, tk.END)
            self.load_tasks()
            self.todo_list.save_tasks("tasks.txt")
            messagebox.showinfo("Success", "Task added successfully!")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            new_description = self.task_entry.get()
            if new_description:
                self.todo_list.update_task(index, new_description)
                self.task_entry.delete(0, tk.END)
                self.load_tasks()
                self.todo_list.save_tasks("tasks.txt")
                messagebox.showinfo("Success", "Task updated successfully!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.todo_list.delete_task(index)
            self.load_tasks()
            self.todo_list.save_tasks("tasks.txt")
            messagebox.showinfo("Success", "Task deleted successfully!")

    def toggle_task_completed(self, event):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.todo_list.toggle_task_completed(index)
            self.load_tasks()
            self.todo_list.save_tasks("tasks.txt")

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            task_text = task.description
            if task.completed:
                task_text += " (Completed)"
            self.task_listbox.insert(tk.END, task_text)

    def on_closing(self):
        self.todo_list.save_tasks("tasks.txt")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

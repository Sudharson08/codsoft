import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        # Frame for the task input
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_task_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_task_btn.pack(side=tk.LEFT)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Buttons for operations
        self.delete_task_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_btn.pack(pady=5)

        self.mark_complete_btn = tk.Button(root, text="Mark as Complete", command=self.mark_complete)
        self.mark_complete_btn.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            self.tasks[selected_index] = task + " [Completed]"
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, self.tasks[selected_index])
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

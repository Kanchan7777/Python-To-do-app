import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.tasks = []

        # Entry box for new task
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        # Add task button
        add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        add_btn.pack(pady=5)

        # Task listbox
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.pack(pady=10)

        # Buttons for complete and delete
        complete_btn = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        complete_btn.pack(pady=5)

        delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_btn.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, t in enumerate(self.tasks):
            display = f"{'[x]' if t['completed'] else '[ ]'} {t['task']}"
            self.task_listbox.insert(tk.END, display)

    def mark_completed(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]['completed'] = not self.tasks[index]['completed']
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

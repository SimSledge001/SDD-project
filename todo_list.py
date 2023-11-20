import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")

        self.tasks_by_date = {}

        # Create GUI elements
        self.date_label = tk.Label(root, text="Enter Date (YYYY-MM-DD):")
        self.date_label.grid(row=0, column=0, padx=10, pady=10)

        self.date_entry = tk.Entry(root, width=15)
        self.date_entry.grid(row=0, column=1, padx=10, pady=10)

        self.task_label = tk.Label(root, text="Enter Task:")
        self.task_label.grid(row=1, column=0, padx=10, pady=10)

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        exit_button = tk.Button(root, text="Exit", command=root.destroy)
        exit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        date = self.date_entry.get()
        task = self.task_entry.get()

        if not date or not task:
            messagebox.showwarning("Warning", "Please enter both date and task.")
            return

        if date in self.tasks_by_date:
            self.tasks_by_date[date].append(task)
        else:
            self.tasks_by_date[date] = [task]

        self.update_task_listbox()
        self.date_entry.delete(0, tk.END)
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        date = self.date_entry.get()

        if date in self.tasks_by_date:
            selected_task_index = self.task_listbox.curselection()

            if selected_task_index:
                task_index = selected_task_index[0]
                del self.tasks_by_date[date][task_index]
                self.update_task_listbox()
            else:
                messagebox.showwarning("Warning", "Please select a task to delete.")
        else:
            messagebox.showwarning("Warning", "No tasks for the selected date.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for date, tasks in self.tasks_by_date.items():
            self.task_listbox.insert(tk.END, f"{date}: {', '.join(tasks)}")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox
import json
import os
FILE_NAME = "tasks.json"
# ---------------- Load Tasks ----------------
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []
# ---------------- Save Tasks ----------------
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)
# ---------------- Refresh List ----------------
def refresh_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        if task["completed"]:
            task_list.insert(tk.END, "✔ " + task["task"])
        else:
            task_list.insert(tk.END, "✘ " + task["task"])
# ---------------- Add Task ----------------
def add_task():
    text = task_entry.get().strip()
    if text == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return
    tasks.append({
        "task": text,
        "completed": False
    })
    save_tasks()
    refresh_list()
    task_entry.delete(0, tk.END)
# ---------------- Main Window ----------------
window = tk.Tk()
window.title("To-Do List Application")
window.geometry("500x500")
window.config(bg="#F5F5F5")
tasks = load_tasks()
# ---------------- Heading ----------------
title = tk.Label(
    window,
    text="TO-DO LIST",
    font=("Arial", 20, "bold"),
    bg="#F5F5F5",
    fg="blue"
)
title.pack(pady=15)
# ---------------- Entry ----------------
task_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=30
)
task_entry.pack(pady=10)
# ---------------- Add Button ----------------
add_button = tk.Button(
    window,
    text="Add Task",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=add_task
)
add_button.pack(pady=10)
# ---------------- Listbox ----------------
task_list = tk.Listbox(
    window,
    width=45,
    height=12,
    font=("Arial", 12)
)
task_list.pack(pady=15)
refresh_list()
# ---------------- Complete Task ----------------
def complete_task():
    selected = task_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task.")
        return
    index = selected[0]
    if tasks[index]["completed"]:
        messagebox.showinfo("Info", "This task is already completed.")
    else:
        tasks[index]["completed"] = True
        save_tasks()
        refresh_list()
        messagebox.showinfo("Success", "Task marked as completed.")
# ---------------- Delete Task ----------------
def delete_task():
    selected = task_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task.")
        return
    index = selected[0]
    deleted = tasks.pop(index)
    save_tasks()
    refresh_list()
    messagebox.showinfo("Deleted", f"{deleted['task']} deleted successfully.")
# ---------------- Clear All Tasks ----------------
def clear_tasks():
    if not tasks:
        messagebox.showinfo("Info", "Task list is already empty.")
        return
    answer = messagebox.askyesno(
        "Confirmation",
        "Do you really want to delete all tasks?"
    )
    if answer:
        tasks.clear()
        save_tasks()
        refresh_list()
        messagebox.showinfo("Success", "All tasks deleted.")
button_frame = tk.Frame(window, bg="#F5F5F5")
button_frame.pack(pady=10)
complete_button = tk.Button(
    button_frame,
    text="Complete",
    bg="blue",
    fg="white",
    width=12,
    command=complete_task
)
complete_button.grid(row=0, column=0, padx=5)
delete_button = tk.Button(
    button_frame,
    text="Delete",
    bg="red",
    fg="white",
    width=12,
    command=delete_task
)
delete_button.grid(row=0, column=1, padx=5)
clear_button = tk.Button(
    button_frame,
    text="Clear All",
    bg="orange",
    fg="white",
    width=12,
    command=clear_tasks
)
clear_button.grid(row=0, column=2, padx=5)
window.mainloop()
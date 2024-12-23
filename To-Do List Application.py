import json
from datetime import datetime


class Task:
    def __init__(self, title, category, priority, due_date):
        self.title = title
        self.category = category
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} ({self.category}, Priority: {self.priority}, Due: {self.due_date})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def update_task(self, title, **kwargs):
        for task in self.tasks:
            if task.title == title:
                task.title = kwargs.get("title", task.title)
                task.category = kwargs.get("category", task.category)
                task.priority = kwargs.get("priority", task.priority)
                task.due_date = kwargs.get("due_date", task.due_date)

    def display_tasks(self):
        for task in sorted(self.tasks, key=lambda t: (t.priority, t.due_date)):
            print(task)

    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                tasks = json.load(file)
                self.tasks = [Task(**task) for task in tasks]
        except FileNotFoundError:
            pass


# start the app
todo = ToDoList()
todo.load_from_file()
todo.add_task(Task("Submit project", "Work", 1, "2024-12-25"))
todo.add_task(Task("Buy groceries", "Personal", 3, "2024-12-23"))
todo.display_tasks()
todo.save_to_file()

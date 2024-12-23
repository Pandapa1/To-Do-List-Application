import json
from datetime import datetime

class Task:
    def __init__(self, title, category, priority, due_date):
        self.title, self.category, self.priority, self.due_date = title, category, priority, due_date
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} ({self.category}, Priority: {self.priority}, Due: {self.due_date})"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task): self.tasks.append(task)

    def delete_task(self, title): self.tasks = [t for t in self.tasks if t.title != title]

    def update_task(self, title, **kwargs):
        for t in self.tasks:
            if t.title == title:
                t.title, t.category, t.priority, t.due_date = (
                    kwargs.get("title", t.title),
                    kwargs.get("category", t.category),
                    kwargs.get("priority", t.priority),
                    kwargs.get("due_date", t.due_date),
                )

    def display_tasks(self):
        for task in sorted(self.tasks, key=lambda t: (t.priority, t.due_date)): print(task)

    def save(self, filename="tasks.json"):
        with open(filename, "w") as f: json.dump([t.__dict__ for t in self.tasks], f)

    def load(self, filename="tasks.json"):
        try: self.tasks = [Task(**t) for t in json.load(open(filename))]
        except FileNotFoundError: pass

todo = ToDoList()
todo.load()
todo.add_task(Task("Submit project", "Work", 1, "2024-12-25"))
todo.add_task(Task("Buy groceries", "Personal", 3, "2024-12-23"))
todo.display_tasks()
todo.save()

# I hope you like my code. You'll need to install packages  if you don't have the required imports (os, abc, enum, datetime, json) some comes pre installed in python3 (pip install) so. I prefer u use (codesandbox.io || replit.com) if you don't have python or pip install on your device.
# This code was hand written.
# 
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional, Dict
from datetime import datetime
import json
import os


class Task_properties_(Enum):
    """Enum for task priority levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Task:
    """Class representing a single task"""

    def __init__(self,
                 title: str,
                 description: str,
                 priority: Task_properties_ = Task_properties_.MEDIUM):
        self.id = None
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()
        self.completed_at = None

    def mark_completed(self):
        """Mark the task as completed"""
        self.completed = True
        self.completed_at = datetime.now()

    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization"""
        return {
            "id":
            self.id,
            "title":
            self.title,
            "description":
            self.description,
            "priority":
            self.priority.name,
            "completed":
            self.completed,
            "created_at":
            self.created_at.isoformat(),
            "completed_at":
            self.completed_at.isoformat() if self.completed_at else None
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create a task from a dictionary"""
        task = cls(title=data["title"],
                   description=data["description"],
                   priority=Task_properties_[data["priority"]])
        task.id = data["id"]
        task.completed = data["completed"]
        task.created_at = datetime.fromisoformat(data["created_at"])
        task.completed_at = datetime.fromisoformat(
            data["completed_at"]) if data["completed_at"] else None
        return task


class ITaskManager(ABC):
    """Interface for task management operations"""

    @abstractmethod
    def add_task(self, task: Task) -> int:
        """Add a task and return its ID"""
        pass

    @abstractmethod
    def mark_completed(self, task_id: int) -> bool:
        """Mark a task as completed and return success status"""
        pass

    @abstractmethod
    def remove_task(self, task_id: int) -> bool:
        """Remove a task and return success status"""
        pass

    @abstractmethod
    def list_tasks(self,
                   completed_filter: Optional[bool] = None) -> List[Task]:
        """List all tasks with optional filtering by completion status"""
        pass

    @abstractmethod
    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID"""
        pass


class TaskManager(ITaskManager):
    """Implementation of the task manager interface"""

    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, task: Task) -> int:
        """Add a task and return its ID"""
        task.id = self.next_id
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task.id

    def mark_completed(self, task_id: int) -> bool:
        """Mark a task as completed and return success status"""
        task = self.get_task(task_id)
        if task:
            task.mark_completed()
            return True
        return False

    def remove_task(self, task_id: int) -> bool:
        """Remove a task and return success status"""
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def list_tasks(self,
                   completed_filter: Optional[bool] = None) -> List[Task]:
        """List all tasks with optional filtering by completion status"""
        tasks = list(self.tasks.values())
        if completed_filter is not None:
            tasks = [
                task for task in tasks if task.completed == completed_filter
            ]
        return tasks

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID"""
        return self.tasks.get(task_id)


class TaskPrinter:
    """Class responsible for displaying tasks (SRP)"""

    @staticmethod
    def print_task(task: Task):
        """Print a single task"""
        status = "✓" if task.completed else "□"
        priority_symbols = {
            Task_properties_.LOW: "⬇",
            Task_properties_.MEDIUM: "⬆",
            Task_properties_.HIGH: "⬆⬆"
        }
        print(
            f"[{task.id}] {status} {priority_symbols[task.priority]} {task.title}"
        )
        print(f"    {task.description}")
        print(f"    Created: {task.created_at.strftime('%Y-%m-%d %H:%M')}")
        if task.completed:
            print(
                f"    Completed: {task.completed_at.strftime('%Y-%m-%d %H:%M')}"
            )
        print()

    @staticmethod
    def print_task_list(tasks: List[Task]):
        """Print a list of tasks"""
        if not tasks:
            print("No tasks found.")
            return

        print(f"Found {len(tasks)} tasks:")
        print("=" * 40)
        for task in tasks:
            TaskPrinter.print_task(task)


class PrioritySorter:
    """Class responsible for sorting tasks by priority (OCP)"""

    @staticmethod
    def sort_by_priority(tasks: List[Task],
                         ascending: bool = False) -> List[Task]:
        """Sort tasks by priority"""
        return sorted(tasks,
                      key=lambda task: task.priority.value,
                      reverse=not ascending)


class IStorageManager(ABC):
    """Interface for task storage operations"""

    @abstractmethod
    def save_tasks(self, tasks: Dict[int, Task]) -> bool:
        """Save tasks to storage"""
        pass

    @abstractmethod
    def load_tasks(self) -> Dict[int, Task]:
        """Load tasks from storage"""
        pass


class FileStorageManager(IStorageManager):
    """Implementation of storage manager using file system"""

    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = file_path

    def save_tasks(self, tasks: Dict[int, Task]) -> bool:
        """Save tasks to a JSON file"""
        try:
            tasks_data = {
                task_id: task.to_dict()
                for task_id, task in tasks.items()
            }
            with open(self.file_path, 'w') as f:
                json.dump(tasks_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False

    def load_tasks(self) -> Dict[int, Task]:
        """Load tasks from a JSON file"""
        if not os.path.exists(self.file_path):
            return {}

        try:
            with open(self.file_path, 'r') as f:
                tasks_data = json.load(f)

            tasks = {}
            for task_id, task_dict in tasks_data.items():
                tasks[int(task_id)] = Task.from_dict(task_dict)

            return tasks
        except Exception as e:
            print(f"Error loading tasks: {e}")
            return {}


class PersistentTaskManager(TaskManager):
    """Task manager with persistence capabilities"""

    def __init__(self, storage_manager: IStorageManager):
        super().__init__()
        self.storage_manager = storage_manager
        self.load()

    def load(self):
        """Load tasks from storage"""
        self.tasks = self.storage_manager.load_tasks()
        if self.tasks:
            self.next_id = max(self.tasks.keys()) + 1
        else:
            self.next_id = 1

    def save(self):
        """Save tasks to storage"""
        return self.storage_manager.save_tasks(self.tasks)

    def add_task(self, task: Task) -> int:
        """Add a task, save, and return its ID"""
        task_id = super().add_task(task)
        self.save()
        return task_id

    def mark_completed(self, task_id: int) -> bool:
        """Mark a task as completed, save, and return success status"""
        result = super().mark_completed(task_id)
        if result:
            self.save()
        return result

    def remove_task(self, task_id: int) -> bool:
        """Remove a task, save, and return success status"""
        result = super().remove_task(task_id)
        if result:
            self.save()
        return result


class ToDoApp:
    """Main application class"""

    def __init__(self, task_manager: ITaskManager):
        self.task_manager = task_manager
        self.printer = TaskPrinter()
        self.sorter = PrioritySorter()

    def run(self):
        """Run the application"""
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.mark_task_completed()
            elif choice == '3':
                self.list_all_tasks()
            elif choice == '4':
                self.list_pending_tasks()
            elif choice == '5':
                self.list_completed_tasks()
            elif choice == '6':
                self.remove_task()
            elif choice == '7':
                self.sort_tasks()
            elif choice == '0':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        """Display the main menu"""
        print("\n===== To-Do List Manager =====")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. List All Tasks")
        print("4. List Pending Tasks")
        print("5. List Completed Tasks")
        print("6. Remove Task")
        print("7. Sort Tasks by Priority")
        print("0. Exit")

    def add_task(self):
        """Add a new task"""
        title = input("Enter task title: ")
        description = input("Enter task description: ")

        print("Select priority level:")
        print("1. Low")
        print("2. Medium")
        print("3. High")

        try:
            priority_choice = int(input("Enter your choice (1-3): "))
            priority = Task_properties_(priority_choice)
        except (ValueError, IndexError):
            print("Invalid choice. Setting priority to Medium.")
            priority = Task_properties_.MEDIUM

        task = Task(title, description, priority)
        task_id = self.task_manager.add_task(task)
        print(f"Task added with ID: {task_id}")

    def mark_task_completed(self):
        """Mark a task as completed"""
        task_id = int(input("Enter task ID to mark as completed: "))
        if self.task_manager.mark_completed(task_id):
            print(f"Task {task_id} marked as completed.")
        else:
            print(f"Task {task_id} not found.")

    def list_all_tasks(self):
        """List all tasks"""
        tasks = self.task_manager.list_tasks()
        self.printer.print_task_list(tasks)

    def list_pending_tasks(self):
        """List pending tasks"""
        tasks = self.task_manager.list_tasks(completed_filter=False)
        self.printer.print_task_list(tasks)

    def list_completed_tasks(self):
        """List completed tasks"""
        tasks = self.task_manager.list_tasks(completed_filter=True)
        self.printer.print_task_list(tasks)

    def remove_task(self):
        """Remove a task"""
        task_id = int(input("Enter task ID to remove: "))
        if self.task_manager.remove_task(task_id):
            print(f"Task {task_id} removed.")
        else:
            print(f"Task {task_id} not found.")

    def sort_tasks(self):
        """Sort and display tasks by priority"""
        tasks = self.task_manager.list_tasks()
        print("\n1. Sort by highest priority first")
        print("2. Sort by lowest priority first")
        choice = input("Enter your choice: ")

        ascending = choice == '2'
        sorted_tasks = self.sorter.sort_by_priority(tasks, ascending)
        self.printer.print_task_list(sorted_tasks)


if __name__ == "__main__":
    storage_manager = FileStorageManager()
    task_manager = PersistentTaskManager(storage_manager)

    app = ToDoApp(task_manager)
    app.run()
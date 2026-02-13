import typer
from typing import Optional
from focuscli import tasks
from focuscli import timer as timer_module

app = typer.Typer(
    help="FocusCLI - Stay productive without leaving your terminal",
    add_completion=False
)

@app.command()
def add(task: str):
    """Add a new task to your list"""
    tasks.add_task(task)

@app.command()
def list():
    """Show all tasks"""
    tasks.list_tasks()

@app.command()
def complete(task_id: int):
    """Mark a task as complete"""
    tasks.complete_task(task_id)

@app.command()
def delete(task_id: int):
    """Remove a task from the list"""
    tasks.delete_task(task_id)

@app.command()
def timer(minutes: Optional[int] = typer.Argument(25)):
    """Start a focus timer (default: 25 minutes)"""
    timer_module.start_timer(minutes)

def main():
    app()

if __name__ == "__main__":
    main()

from rich.console import Console
from rich.table import Table
from focuscli.storage import TaskStorage

console = Console()
storage = TaskStorage()

def add_task(description: str):
    task = storage.add_task(description)
    console.print(f"✓ Task added: [bold cyan]{description}[/bold cyan] (ID: {task['id']})")

def list_tasks():
    tasks = storage.get_all_tasks()
    
    if not tasks:
        console.print("[yellow]No tasks yet. Add one with 'focuscli add <task>'[/yellow]")
        return
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Task", min_width=20)
    table.add_column("Status", justify="center")
    
    for task in tasks:
        status = "[green]✓ Done[/green]" if task['completed'] else "[yellow]○ Pending[/yellow]"
        style = "dim" if task['completed'] else ""
        
        table.add_row(
            str(task['id']),
            task['description'],
            status,
            style=style
        )
    
    console.print(table)

def complete_task(task_id: int):
    if storage.complete_task(task_id):
        console.print(f"[green]✓ Task {task_id} marked as complete![/green]")
    else:
        console.print(f"[red]Task {task_id} not found[/red]")

def delete_task(task_id: int):
    if storage.delete_task(task_id):
        console.print(f"[red]✗ Task {task_id} deleted[/red]")
    else:
        console.print(f"[red]Task {task_id} not found[/red]")

import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeRemainingColumn

console = Console()

def start_timer(minutes: int):
    total_seconds = minutes * 60
    
    console.print(f"\n[bold green]🍅 Starting {minutes}-minute focus session![/bold green]\n")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeRemainingColumn(),
        console=console
    ) as progress:
        
        task = progress.add_task("[cyan]Focus time", total=total_seconds)
        
        try:
            for _ in range(total_seconds):
                time.sleep(1)
                progress.update(task, advance=1)
            
            console.print("\n[bold green]🎉 Session complete! Great work![/bold green]\n")
            
        except KeyboardInterrupt:
            console.print("\n[yellow]⏸ Timer paused. Take a break![/yellow]\n")

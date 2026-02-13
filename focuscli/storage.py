import json
import os
from pathlib import Path
from typing import List, Dict

class TaskStorage:
    def __init__(self, filename: str = "tasks.json"):
        self.data_dir = Path.home() / ".focuscli"
        self.data_dir.mkdir(exist_ok=True)
        self.filepath = self.data_dir / filename
        
        if not self.filepath.exists():
            self._save([])
    
    def load(self) -> List[Dict]:
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save(self, tasks: List[Dict]):
        with open(self.filepath, 'w') as f:
            json.dump(tasks, f, indent=2)
    
    def add_task(self, description: str) -> Dict:
        tasks = self.load()
        task_id = max([t['id'] for t in tasks], default=0) + 1
        
        new_task = {
            'id': task_id,
            'description': description,
            'completed': False
        }
        
        tasks.append(new_task)
        self._save(tasks)
        return new_task
    
    def get_all_tasks(self) -> List[Dict]:
        return self.load()
    
    def complete_task(self, task_id: int) -> bool:
        tasks = self.load()
        
        for task in tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self._save(tasks)
                return True
        
        return False
    
    def delete_task(self, task_id: int) -> bool:
        tasks = self.load()
        filtered = [t for t in tasks if t['id'] != task_id]
        
        if len(filtered) < len(tasks):
            self._save(filtered)
            return True
        
        return False

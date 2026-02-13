# 🎯 FocusCLI

[![PyPI version](https://badge.fury.io/py/focuscli.svg)](https://badge.fury.io/py/focuscli)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A minimal productivity tool for developers who want to manage tasks and stay focused without leaving the terminal.

## ✨ Features

- **Task Management**: Add, list, complete, and delete tasks with a clean interface
- **Pomodoro Timer**: Built-in focus timer with live progress tracking
- **Beautiful UI**: Powered by Rich library for colorful tables and progress bars
- **Simple Storage**: Tasks saved locally in JSON format
- **Zero Config**: Works right out of the box

## 🚀 Installation

### Quick Install (Recommended)

Install directly from PyPI:

```bash
pip install focuscli
```

### From Source

Clone the repository and install:

```bash
git clone https://github.com/eneswritescode/focuscli.git
cd focuscli
pip install -e .
```

### Requirements

- Python 3.7 or higher
- Dependencies will be installed automatically

## 🎬 Quick Start

```bash
# Install
pip install focuscli

# Add some tasks
focuscli add "Review pull requests"
focuscli add "Write documentation"
focuscli add "Fix bug in login"

# See your tasks
focuscli list

# Complete a task
focuscli complete 1

# Start a 25-minute focus session
focuscli timer
```

## 📖 Usage

### Add a task

```bash
focuscli add "Write documentation"
focuscli add "Fix bug in login page"
```

### List all tasks

```bash
focuscli list
```

Output example:
```
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ ID     ┃ Task                 ┃  Status   ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ 1      │ Write documentation  │ ○ Pending │
│ 2      │ Fix bug in login page│ ○ Pending │
└────────┴──────────────────────┴───────────┘
```

### Complete a task

```bash
focuscli complete 1
```

### Delete a task

```bash
focuscli delete 2
```

### Start a focus timer

```bash
# Default 25-minute session
focuscli timer

# Custom duration (in minutes)
focuscli timer 45
```

**Windows Note:** If `focuscli` command is not found after installation, you may need to add Python Scripts to your PATH or use:
```bash
python -m focuscli.main <command>
```

## 🛠️ Development

### Setup development environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run locally

```bash
python -m focuscli.main add "Test task"
python -m focuscli.main list
```

## 📂 Project Structure

```
focuscli/
├── focuscli/
│   ├── __init__.py
│   ├── main.py      # CLI entry point
│   ├── tasks.py     # Task management logic
│   ├── timer.py     # Pomodoro timer
│   └── storage.py   # JSON file handling
├── requirements.txt
├── setup.py
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 💡 Ideas for Future Features

- Task priorities and tags
- Weekly/monthly reports
- Export tasks to different formats
- Break reminders after focus sessions
- Integration with calendar apps

## 📝 License

MIT License - feel free to use this project however you want.

## � Links

- **PyPI**: https://pypi.org/project/focuscli/
- **GitHub**: https://github.com/eneswritescode/focuscli
- **Issues**: https://github.com/eneswritescode/focuscli/issues

## 🙏 Acknowledgments

Built with:
- [Typer](https://typer.tiangolo.com/) - Modern CLI framework
- [Rich](https://rich.readthedocs.io/) - Beautiful terminal formatting

---

Made with ☕ by developers, for developers

**Star this repo if you find it helpful!** ⭐

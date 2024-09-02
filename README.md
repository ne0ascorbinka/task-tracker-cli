# task-tracker-cli

**Task tracker CLI** is a simple command-line interface (CLI) tool for managing tasks, which is implementation of this [Roadmap Project](https://roadmap.sh/projects/task-tracker). With Task CLI, you can add, update, delete, and list tasks, as well as mark them as in-progress or done.

## Features

- **Add a New Task**: Easily add tasks with a description.
- **Update a Task**: Modify the description of an existing task by its ID.
- **Delete a Task**: Remove a task from the list using its ID.
- **Mark Task as In-Progress**: Set the status of a task to "in-progress".
- **Mark Task as Done**: Set the status of a task to "done".
- **List Tasks**: View all tasks or filter them based on their status.

## Installation

To install Task tracker CLI, you need Python and pip. If you don't have Python installed, [install Python](https://www.python.org/downloads/). You can install the CLI using the following steps:

1. Clone the repository or download the source code.
2. Navigate to the project directory containing the `setup.py` file.
3. Run the following command to install the CLI:

```bash
pip install .
```

This will install the CLI and make the `task-cli` command available globally on your system.

## Usage

After installing, you can use the `task-cli` command to manage your tasks. Below is a guide to the available commands and their usage:

### General Help

To see the general help message, run:

```bash
task-cli -h
```

### Commands

- **Add a Task**

  To add a new task, use the `add` command:

  ```bash
  task-cli add "Your task description here"
  ```

- **Update a Task**

  To update an existing task by its ID, use the `update` command:

  ```bash
  task-cli update <task_id> "Updated task description"
  ```

- **Delete a Task**

  To delete a task by its ID, use the `delete` command:

  ```bash
  task-cli delete <task_id>
  ```

- **Mark a Task as In-Progress**

  To mark a task as in-progress, use the `mark-in-progress` command:

  ```bash
  task-cli mark-in-progress <task_id>
  ```

- **Mark a Task as Done**

  To mark a task as done, use the `mark-done` command:

  ```bash
  task-cli mark-done <task_id>
  ```

- **List Tasks**

  To list all tasks, use the `list` command:

  ```bash
  task-cli list
  ```

  You can also filter tasks by status using optional flags:

  ```bash
  task-cli list --filter in-progress
  task-cli list --filter done
  ```

### Example

Here's an example of how you might use Task CLI:

```bash
task-cli add "Write the report"
task-cli list
task-cli update 1 "Write the annual report"
task-cli mark-in-progress 1
task-cli mark-done 1
task-cli delete 1
```

## Uninstallation

If you need to uninstall Task CLI, you can do so with pip:

```bash
pip uninstall task-cli
```


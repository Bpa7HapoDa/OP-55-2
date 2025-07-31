CREATE_TABLE_task = """
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    task TEXT NOT NULL,
    create_time TEXT NOT NULL
    )
"""

INSERT_TASK = """
    INSERT INTO tasks (task, create_time) VALUES (?, ?)
"""

SELECT_TASKS = "SELECT id, task, create_time FROM tasks"

UPDATE_TASK = "UPDATE tasks SET task = ? WHERE id = ?"

DELETE_TASK = "DELETE FROM tasks WHERE id = ?"
CREATE_TABLE_task = """
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    task TEXT NOT NULL,
    create_time TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'in_progress'
    )
"""

INSERT_TASK = """
    INSERT INTO tasks (task, create_time, status) VALUES (?, ?, 'in_progress')
"""

SELECT_TASKS = "SELECT id, task, create_time, status FROM tasks"
SELECT_ACTIVE_TASKS = "SELECT id, task, create_time, status FROM tasks WHERE status = 'in_progress'"

UPDATE_TASK = "UPDATE tasks SET task = ? WHERE id = ?"
UPDATE_STATUS = "UPDATE tasks SET status = ? WHERE id = ?"

DELETE_TASK = "DELETE FROM tasks WHERE id = ?"
DELETE_COMPLETED = "DELETE FROM tasks WHERE status = 'completed'"
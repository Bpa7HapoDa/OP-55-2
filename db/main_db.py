import sqlite3
from db import queries
from config import db_path
from datetime import datetime

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_task)
    print('База данных подключена!')
    conn.commit()
    conn.close()

def get_tasks(active_only=False):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if active_only:
        cursor.execute(queries.SELECT_ACTIVE_TASKS)
    else:
        cursor.execute(queries.SELECT_TASKS)
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def add_task(task):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(queries.INSERT_TASK, (task, create_time))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

def update_task(task_id, new_task):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_TASK, (new_task, task_id))
    conn.commit()
    conn.close()

def update_status(task_id, status):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_STATUS, (status, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK, (task_id,))
    conn.commit()
    conn.close()
    
def delete_completed_tasks():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_COMPLETED)
    conn.commit()
    conn.close()
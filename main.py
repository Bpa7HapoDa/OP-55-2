import flet as ft 
from db import main_db
from datetime import datetime

def main(page: ft.Page):
    page.title = 'ToDo App'
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=10)
    is_active_only = False

    def load_task():
        task_list.controls.clear()
        nonlocal is_active_only
        for task_id, task_text, create_time, status in main_db.get_tasks(active_only=is_active_only):
            task_list.controls.append(create_task_row(task_id, task_text, create_time, status))
        page.update()
    
    def create_task_row(task_id, task_text, create_time, status):
        
        def toggle_status(e):
            new_status = 'completed' if e.control.value else 'in_progress'
            main_db.update_status(task_id, new_status)
            load_task()

        task_field = ft.TextField(value=task_text, read_only=True)
        checkbox = ft.Checkbox(value=(status == 'completed'), on_change=toggle_status)

        def enadle_edit(e):
            task_field.read_only = False
            task_field.update()

        def save_task(e):
            main_db.update_task(task_id, task_field.value)
            task_field.read_only = True
            page.update()
        
        return ft.Row([
            checkbox,
            task_field,
            ft.Text(value=create_time, size=12, color=ft.Colors.GREY_500),
            ft.IconButton(ft.Icons.EDIT, on_click=enadle_edit, tooltip='Редактировать', icon_color=ft.Colors.ORANGE),
            ft.IconButton(ft.Icons.SAVE_ALT_ROUNDED, tooltip='Сохранить',
                          on_click=save_task, 
                          icon_color=ft.Colors.GREEN),
            ft.IconButton(ft.Icons.DELETE, tooltip='Удалить', 
                          on_click=lambda e: delete_task(task_id),
                          icon_color=ft.Colors.RED)
        ], alignment=ft.MainAxisAlignment.START)
    
    def add_task(e):
        if not task_input.value:
            return
        
        if add_button.disabled:
            return
        
        task = task_input.value
        main_db.add_task(task)
        load_task() 
        task_input.value = ""
        task_input.error_text = None
        page.update()
    
    def delete_task(task_id):
        main_db.delete_task(task_id)
        load_task()

    def clear_completed(e):
        main_db.delete_completed_tasks()
        load_task()

    def filter_tasks(e):
        nonlocal is_active_only
        is_active_only = e.control.text == 'В работе'
        load_task()

    def max_length(e):
        if len(e.control.value) > 100:
            e.control.error_text = "Длина задачи не может превышать 100 символов"
            add_button.disabled = True
        else:
            e.control.error_text = None
            add_button.disabled = False
        page.update()

    task_input = ft.TextField(label='Введите задачу', on_change=max_length)
    add_button = ft.TextButton("Добавить", on_click=add_task)
    
    filter_buttons = ft.Row([
        ft.TextButton("Все", on_click=filter_tasks),
        ft.TextButton("В работе", on_click=filter_tasks),
        ft.TextButton("Очистить выполненные", on_click=clear_completed, style=ft.ButtonStyle(color=ft.Colors.RED))
    ], alignment=ft.MainAxisAlignment.CENTER)

    content = ft.Column([
        ft.Row([task_input, add_button], 
               alignment=ft.MainAxisAlignment.SPACE_EVENLY),
        filter_buttons,
        task_list
    ])

    background_image = ft.Image(
        src='/home/Admin1/OP-55-2/media/Image.png',
        fit=ft.ImageFit.FILL,
        width=page.width,
        height=page.height
    )

    background = ft.Stack(controls=[background_image, content]) 

    def on_resize(e):
        background_image.width = page.width
        background_image.height = page.height
        page.update()

    page.add(background)
    page.on_resize = on_resize

    load_task()

if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)
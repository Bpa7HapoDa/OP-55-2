import flet as ft 
from db import main_db

def main(page: ft.Page):
    page.title = 'ToDo App'
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=10)

    def load_task():
        task_list.controls.clear()
        for task_id, task_text, create_time in main_db.get_tasks():
            task_list.controls.append(create_task_row(task_id, task_text, create_time))

        page.update()
    
    def create_task_row(task_id, task_text, create_time):
        task_field = ft.TextField(value=task_text, read_only=True, expand=True)

        def enadle_edit(e):
            task_field.read_only = False
            task_field.update()

        def save_task(e):
            main_db.update_task(task_id, task_field.value)
            task_field.read_only = True
            page.update()
        
        return ft.Row([
            task_field,
            ft.Text(value=create_time, size=12, color=ft.Colors.GREY_500), # Отображаем дату
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
        
        if task_input.value:
            task = task_input.value
            task_id = main_db.add_task(task)
            load_task() 
            task_input.value = ""
            page.update()
    
    def delete_task(task_id):
        main_db.delete_task(task_id)
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

    content = ft.Column([
        ft.Row([task_input, add_button], 
               alignment=ft.MainAxisAlignment.SPACE_EVENLY),
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
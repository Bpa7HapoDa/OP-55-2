import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    # page.add(ft.Text("Hello world"))
    page.title = 'Мое первое приложение на Flet'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Привет, мир!")

    greeting_history = []
    history_text = ft.Text("История приветствий:")

    def on_button_click(_):
        name = name_input.value.strip()
        current_hour = datetime.datetime.now().hour

        if name:
            if 6 <= current_hour < 12:
                greeting_text.value = f"Доброе утро, {name}!"
            elif 12 <= current_hour < 18:
                greeting_text.value = f"Добрый день, {name}!"
            elif 18 <= current_hour < 24:
                greeting_text.value = f"Добрый вечер, {name}!"
            else:  
                greeting_text.value = f"Доброй ночи, {name}!"
            # greeting_text.value = f"Привет, {name}!"
            greet_button.text = "Отправить еще раз"
            name_input.value = ""
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f'{timestamp} - {name}')
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Пожалуйте, введите имя!" 

        # print(greeting_text.value)
        page.update()
    
    def clear_history(_):
        greeting_history.clear()
        print(f"История приветствий очищена. {greeting_history}")
        history_text.value = "История приветствий:"
        page.update()

    clear_button = ft.IconButton(icon_color=ft.Colors.GREEN, icon=ft.Icons.DELETE_FOREVER, tooltip="Очистить историю", on_click=clear_history)

    name_input = ft.TextField(label="Введите имя:", on_submit=on_button_click)
    greet_button = ft.ElevatedButton("Отправить", on_click=on_button_click, icon=ft.Icons.SEND)
    greet_button_1 = ft.TextButton("Отправить", on_click=on_button_click, icon=ft.Icons.SEND)

    page.add(greeting_text, name_input, greet_button, greet_button_1, clear_button, history_text)


ft.app(target=main, view=ft.WEB_BROWSER)
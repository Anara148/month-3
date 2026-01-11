import flet as ft
from datetime import datetime 

def main (page: ft.Page):
    page.title = "Мое первое приложение!"
    page. theme_mode = ft.ThemeMode. DARK

    greeting_history = []

    greeting_text = ft.Text('История приветствий:')
  
    text_hello = ft.Text(value='Hello world')

    def on_button_click(_):
        name = name_input.value.strip()
        print (name)

        if name:
            greeting_history.append(name)
            greeting_text.value = 'История приветствий:\n' + "\n".join(greeting_history)
            if len (name) < 3:
                text_hello.value = 'Имя слишком короткое'
                text_hello. color = ft.Colors.RED
                name_input.value = None
            elif len(name) >= 20:
                text_hello.value = 'Имя слишком длинное'
                text_hello.color = ft.Colors. RED
                name_input.value = None

            else:
                now = datetime.now()
                formatted_time = now.strftime("%Y-%m-%d / %H:%M:%S")
               

                print("Добавлено:", name)
                print("История:", greeting_history)

                text_hello.color =  None
                text_hello.value = f"{formatted_time} - Привет {name}!"
                name_input.value = None
        else:
            text_hello.value = 'Введите корректное имя'
            text_hello.color = ft.Colors.RED



    def clear_history(_):
        greeting_history.clear()
        print("История очищена!")
        greeting_text.value = 'История приветствий:'


    def sort_history(_):
        if greeting_history:
            greeting_history.sort(key=str.lower)
            print("История после сортировки:")
            for name in greeting_history:
                print(name)

            greeting_text.value = 'История приветствий:\n' + "\n".join(greeting_history)
        else:
            text_hello.value = 'История пуста'
            text_hello. color = ft.Colors.RED


    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons. SEND, on_click=on_button_click)

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    sort_button = ft.ElevatedButton("Сортировать по алфавиту", on_click=sort_history)

    name_input = ft.TextField(label='Введите имя', max_length=20, on_submit=on_button_click, expand=True)

    text_row = ft.Row([text_hello], alignment=ft.MainAxisAlignment.CENTER)

    main_object = ft.Row([name_input, elevated_button, clear_button])



    page.add(text_row, main_object,sort_button, greeting_text)

ft. app(target=main)


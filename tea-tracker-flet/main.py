import flet as ft

color = {
    'green_main': '#318653',
    'green_light': '#71BD85',
    'orange_light': '#FAD074',
    'orange': '#FFC634',
    'light': '#FFC634',
    'black': '#272726'
}

def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    page.fonts = {
    }
    page.window_width = 390
    page.window_height = 844
    page.bgcolor = color['black']
    page.update()


ft.app(main)

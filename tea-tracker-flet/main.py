import flet as ft

from components.app_bar import AppBar
from components.bottom_appbar import BottomAppbar
from scales.main import start_brew
from screens.main_screen import MainScreen
from styling.styles import Font, Color


def main(page: ft.Page):
    page.fonts = {font: font for font in Font}
    page.add(
        ft.SafeArea(
            content=ft.Pagelet(
                content=MainScreen()
            )
        )
    )

    page.appbar = AppBar()
    page.bottom_appbar = BottomAppbar()

    page.window.width = 390
    page.window.height = 844
    page.padding = ft.padding.all(0)
    page.bgcolor = Color.BLACK
    start_brew(page=page)
    page.update()


ft.app(main)

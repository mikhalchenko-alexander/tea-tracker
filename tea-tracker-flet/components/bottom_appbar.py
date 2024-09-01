import flet as ft

from components.app_bar_button import AppBarButton
from styling.styles import Color


class BottomAppbar(ft.BottomAppBar):
    def __init__(self):
        super().__init__()
        self.bgcolor = Color.TRANSPARENT
        self.content = ft.Row(
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        AppBarButton("icons/stop.svg"),
                        AppBarButton("icons/tea.svg")
                    ]
                ),
                AppBarButton("icons/update.svg", "+5 sec")
            ]
        )

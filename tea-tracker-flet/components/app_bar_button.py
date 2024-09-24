import flet as ft
from flet_core import MainAxisAlignment

from styling.styles import Color


class AppBarButton(ft.Container):

    def __init__(self, icon: ft.Control | None, label: str | None, on_click: ft.OptionalEventCallable = None, **kwargs):
        super().__init__(**kwargs)
        self.expand = 1
        self.height = 100

        if icon is not None and label is not None:
            content = ft.Row(
                controls=[
                    icon,
                    ft.Text(
                        label,
                        style=ft.TextStyle(color=Color.LIGHT)
                    )
                ],
                alignment=MainAxisAlignment.CENTER
            )
        elif icon is not None:
            content = icon
        else:
            content = ft.Text(
                label,
                style=ft.TextStyle(color=Color.LIGHT, size=26)
            )

        self.content = ft.FilledButton(
            content=content,
            style=ft.ButtonStyle(
                side=ft.BorderSide(width=2, color=Color.GREEN_MAIN),
                shape=ft.RoundedRectangleBorder(radius=16),
                bgcolor=Color.GREEN_MAIN if label else Color.TRANSPARENT,
                padding=0
            ),
            on_click=on_click
        )

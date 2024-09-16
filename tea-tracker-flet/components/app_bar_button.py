import flet as ft
from flet_core import MainAxisAlignment

from ..styling.styles import Color


class AppBarButton(ft.Container):

    def __init__(self, icon: str, label: str = "", **kwargs):
        super().__init__(**kwargs)
        self.expand = 1
        self.height = 100
        icon = ft.Image(icon, color=Color.LIGHT, color_blend_mode=ft.BlendMode.DST)
        content = icon if not label else ft.Row(
            controls=[
                icon,
                ft.Text(
                    label,
                    style=ft.TextStyle(color=Color.LIGHT)
                )
            ],
            alignment=MainAxisAlignment.CENTER
        )
        self.content = ft.FilledButton(
            content=content,
            style=ft.ButtonStyle(
                side=ft.BorderSide(width=2, color=Color.GREEN_MAIN),
                shape=ft.RoundedRectangleBorder(radius=16),
                bgcolor=Color.GREEN_MAIN if label else Color.TRANSPARENT
            )
        )

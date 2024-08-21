import flet as ft
from flet_core import MainAxisAlignment

from styling.styles import Color, Font


class StatusIcon(ft.Container):
    def __init__(self, src: str, label: str, color: Color, show_border: bool = True):
        super().__init__()
        self.content=ft.Row(
            controls=[
                ft.Image(
                    src=src,
                    color=color
                ),
                ft.Text(
                    label,
                    color=color,
                    font_family=Font.INKNUT_ANTIQUA_LIGHT,
                    size=14,
                )
            ],
            spacing=4,
            width=90,
            alignment=MainAxisAlignment.CENTER
        )
        if show_border:
            self.border = ft.Border(
                right=ft.BorderSide(width=1, color=Color.ORANGE_LIGHT_TRANSPARENT)
            )

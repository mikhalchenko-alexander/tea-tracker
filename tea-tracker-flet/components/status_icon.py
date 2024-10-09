import flet as ft
from flet_core import MainAxisAlignment
from mopyx import render

from styling.styles import Color, Font


class StatusIcon(ft.Container):
    def __init__(self, src: str, label: str, color: Color, show_border: bool = True):
        super().__init__()
        self.src = src
        self.label = label
        self.color = color
        self.content = self.render_status_icon()
        if show_border:
            self.border = ft.Border(
                right=ft.BorderSide(width=1, color=Color.ORANGE_LIGHT_TRANSPARENT)
            )

    @render
    def render_status_icon(self):
        return ft.Row(
            controls=[
                ft.Image(
                    src=self.src,
                    color=self.color
                ),
                ft.Text(
                    self.label,
                    color=self.color,
                    font_family=Font.INKNUT_ANTIQUA_LIGHT,
                    size=14,
                )
            ],
            spacing=4,
            width=90,
            alignment=MainAxisAlignment.CENTER
        )

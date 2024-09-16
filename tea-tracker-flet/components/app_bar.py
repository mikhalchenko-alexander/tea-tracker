import flet as ft

from ..styling.styles import Color, Font


class AppBar(ft.AppBar):
    def __init__(self):
        super().__init__()
        self.bgcolor = Color.BLACK
        self.center_title = True
        self.leading = ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS,
            icon_color=Color.ORANGE_LIGHT
        )
        self.title = ft.Text(
            value="New set",
            color=Color.ORANGE_LIGHT,
            font_family=Font.INKNUT_ANTIQUA,
            size=20
        )
        self.actions = [
            ft.PopupMenuButton(
                items=[],
                icon_color=Color.ORANGE_LIGHT,
                icon=ft.icons.MORE_VERT
            )
        ]

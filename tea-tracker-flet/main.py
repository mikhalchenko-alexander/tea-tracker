import flet as ft

from styling.styles import Font, Color
from components.status_bar import StatusBar


def main(page: ft.Page):
    page.fonts = {font: font for font in Font}
    page.add(
        ft.SafeArea(
            ft.Pagelet(
                appbar=ft.AppBar(
                    bgcolor=Color.BLACK,
                    center_title=True,
                    leading=ft.IconButton(
                        icon=ft.icons.ARROW_BACK_IOS,
                        icon_color=Color.ORANGE_LIGHT
                    ),
                    title=ft.Text(
                        value="New set",
                        color=Color.ORANGE_LIGHT,
                        font_family=Font.INKNUT_ANTIQUA,
                        size=20
                    ),
                    actions=[
                        ft.PopupMenuButton(
                            items=[],
                            icon_color=Color.ORANGE_LIGHT,
                            icon=ft.icons.MORE_VERT
                        )
                    ],
                ),
                content=StatusBar()
            )))
    page.window.width = 390
    page.window.height = 844
    page.bgcolor = Color.BLACK
    page.update()


ft.app(main)

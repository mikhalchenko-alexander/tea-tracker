import flet as ft
from flet_core import CrossAxisAlignment, MainAxisAlignment

from components.brews import Brews
from components.timer import Timer
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
                content=ft.Column(
                    controls=[
                        StatusBar(),
                        ft.Container(height=30),
                        ft.ResponsiveRow(
                            controls=[
                                ft.Column(
                                    col=3,
                                    controls=[Brews(current_brew=3, total_ml=423)]
                                ),
                                ft.Column(
                                    col=9,
                                    controls=[
                                        ft.Container(height=40),
                                        Timer(6, 10, 105)
                                    ]
                                )
                            ]
                        )
                    ]
                )
            )))
    page.window.width = 390
    page.window.height = 844
    page.bgcolor = Color.BLACK
    page.update()


ft.app(main)

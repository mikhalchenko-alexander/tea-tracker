import flet as ft
from flet_core import ImageFit

from components.brews import Brews
from components.status_bar import StatusBar
from components.timer import Timer
from styling.styles import Font, Color


def main(page: ft.Page):
    page.fonts = {font: font for font in Font}
    page.add(
        ft.SafeArea(
            content=ft.Pagelet(
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
                        ft.Stack(
                            controls=[
                                ft.Image(
                                    top=215,
                                    left=-30,
                                    width=450,
                                    fit=ImageFit.FIT_WIDTH,
                                    src="images/cup.png"
                                ),
                                ft.ResponsiveRow(
                                    height=800,
                                    columns=12,
                                    controls=[
                                        ft.Column(
                                            col=3,
                                            controls=[Brews(current_brew=3, total_ml=423)]
                                        ),
                                        ft.Column(
                                            col=9,
                                            controls=[
                                                ft.Container(height=35),
                                                ft.Container(
                                                    content=Timer(6, 10, 105),
                                                    padding=ft.padding.only(left=7)
                                                )

                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                )
            )))
    page.window.width = 390
    page.window.height = 844
    page.padding=ft.padding.all(0)
    page.bgcolor = Color.BLACK
    page.update()


ft.app(main)

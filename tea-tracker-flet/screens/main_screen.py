import flet as ft
from flet_core import ImageFit

from components.brews import Brews
from components.status_bar import StatusBar
from components.timer import Timer


class MainScreen(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
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
            )
        ]

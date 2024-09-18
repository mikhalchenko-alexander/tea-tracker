import asyncio

import flet as ft
from flet_core import ImageFit

from components.brews import Brews
from components.status_bar import StatusBar
from components.timer import Timer
from state.timer.timer_state import timer_model


class MainScreen(ft.Column):
    def __init__(self, page):
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
        self.model = timer_model

        page.run_task(self.update_current_time)

    async def update_current_time(self):
        await asyncio.sleep(1)
        self.model.current_time += 1
        self.page.update()
        if self.model.current_time < 10:
            await self.update_current_time()

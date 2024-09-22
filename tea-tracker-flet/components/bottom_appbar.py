import asyncio

import flet as ft
from mopyx import render

from components.app_bar_button import AppBarButton
from state.timer.timer_state import timer_model
from styling.styles import Color


class BottomAppbar(ft.BottomAppBar):
    def __init__(self):
        super().__init__()
        self.bgcolor = Color.TRANSPARENT
        self.bottom_appbar_render()

    @render
    def bottom_appbar_render(self):
        self.content = ft.Row(
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        AppBarButton(
                            ft.Icon(ft.icons.PLAY_ARROW if not timer_model.is_ticking else ft.icons.PAUSE),
                            self.start_timer if not timer_model.is_ticking else self.stop_timer,
                        ),
                        AppBarButton(ft.Image("icons/tea.svg", color=Color.LIGHT, color_blend_mode=ft.BlendMode.DST))
                    ]
                ),
                AppBarButton(ft.Image("icons/update.svg", color=Color.LIGHT, color_blend_mode=ft.BlendMode.DST),
                             label="+5 sec")
            ]
        )

    def start_timer(self, evt: ft.ControlEvent):
        timer_model.current_time = 10
        timer_model.is_ticking = True
        self.page.update()
        self.page.run_task(self.update_current_time)

    def stop_timer(self, evt: ft.ControlEvent):
        timer_model.is_ticking = False
        self.page.update()

    async def update_current_time(self):
        while timer_model.is_ticking:
            await asyncio.sleep(1)
            timer_model.current_time -= 1
            timer_model.total_brew_time += 1
            self.page.update()

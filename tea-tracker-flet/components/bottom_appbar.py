import asyncio

import flet as ft
from flet_core import MainAxisAlignment, CrossAxisAlignment, ButtonStyle
from mopyx import render

from components.app_bar_button import AppBarButton
from scales.main import stop_brew, start_brew
from state.brew_state import brew_model
from state.scale_state import scales_model
from state.timer_state import timer_model
from styling.styles import Color, Font


class BottomAppbar(ft.BottomAppBar):
    def __init__(self):
        super().__init__()
        self.bgcolor = Color.TRANSPARENT
        self.bottom_appbar_render()

    @render
    def bottom_appbar_render(self):
        brew_can_start = scales_model.cup_present and scales_model.tea_present and scales_model.water_present
        self.content = ft.Row(
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        AppBarButton(
                            icon=ft.Icon(ft.icons.PLAY_ARROW if not timer_model.is_ticking else ft.icons.PAUSE),
                            label=None,
                            on_click=self.start_timer if not timer_model.is_ticking else self.stop_timer,
                            disabled=not brew_can_start
                        ),
                        AppBarButton(
                            icon=ft.Image("icons/tea.svg", color=Color.LIGHT, color_blend_mode=ft.BlendMode.DST),
                            label=None,
                            on_click=self.new_set
                        )
                    ]
                ),
                ft.Container(
                    expand=True,
                    bgcolor=Color.GREEN_MAIN,
                    border_radius=ft.border_radius.all(16),
                    padding=ft.padding.symmetric(5, 0),
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            AppBarButton(
                                disabled=timer_model.brew_time <= 5,
                                icon=None,
                                label="-",
                                on_click=self.decrease_brew_time),
                            ft.Container(
                                border=ft.border.symmetric(None, ft.BorderSide(2, Color.LIGHT_TRANSPARENT)),
                                padding=ft.padding.symmetric(0, 10),
                                content=ft.Column(
                                    spacing=0,
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Image("icons/update.svg", color=Color.LIGHT,
                                                 color_blend_mode=ft.BlendMode.DST),
                                        ft.Text(
                                            "5 sec",
                                            style=ft.TextStyle(color=Color.LIGHT)
                                        )
                                    ]
                                ),
                            ),
                            AppBarButton(
                                icon=None,
                                label="+",
                                on_click=self.increase_brew_time)
                        ]
                    )
                )
            ]
        )

    def start_timer(self, evt: ft.ControlEvent):
        timer_model.current_time = timer_model.brew_time
        timer_model.is_ticking = True
        brew_model.current_brew += 1
        self.page.update()
        self.page.run_task(self.update_current_time)

    def stop_timer(self, evt: ft.ControlEvent):
        timer_model.is_ticking = False
        stop_brew(page=self.page)
        self.page.update()

    async def update_current_time(self):
        while timer_model.is_ticking:
            await asyncio.sleep(1)
            timer_model.current_time -= 1
            timer_model.total_brew_time += 1
            self.page.update()

    def increase_brew_time(self, evt: ft.ControlEvent):
        timer_model.brew_time += 5
        self.page.update()

    def decrease_brew_time(self, evt: ft.ControlEvent):
        if timer_model.brew_time > 5:
            timer_model.brew_time -= 5
            self.page.update()

    def create_new_set_modal(self):
        new_set_modal = ft.AlertDialog(
            modal=False,
            bgcolor=Color.BLACK,
            content=ft.Text(
                "Do you want to start a new set?",
                color=Color.LIGHT,
                font_family=Font.INKNUT_ANTIQUA_LIGHT,
                size=14,
            ),
            actions=[
                ft.TextButton(
                    content=ft.Text(
                        "Yes",
                        color=Color.LIGHT,
                        font_family=Font.INKNUT_ANTIQUA_LIGHT,
                        size=14,
                    ),
                    on_click=lambda e: self.start_new_set(new_set_modal),
                    style=ButtonStyle(
                        side=ft.BorderSide(2, Color.GREEN_MAIN),
                        shape=ft.RoundedRectangleBorder(5),
                        color=Color.LIGHT
                    )
                ),
                ft.TextButton(
                    content=ft.Text(
                        "No",
                        color=Color.LIGHT,
                        font_family=Font.INKNUT_ANTIQUA_LIGHT,
                        size=14,
                    ),
                    on_click=lambda e: self.page.close(new_set_modal),
                    style=ButtonStyle(
                        side=ft.BorderSide(2, Color.GREEN_MAIN),
                        shape=ft.RoundedRectangleBorder(5),
                        color=Color.LIGHT,
                        bgcolor=Color.GREEN_MAIN
                    )
                )
            ]
        )
        return new_set_modal

    def new_set(self, evt: ft.ControlEvent):
        self.page.open(self.create_new_set_modal())

    def start_new_set(self, new_set_modal: ft.AlertDialog):
        brew_model.current_brew = 0
        brew_model.total_ml = 0
        timer_model.brew_time = 10
        timer_model.is_ticking = False
        timer_model.current_time = 0
        timer_model.total_brew_time = 0
        scales_model.reset()
        self.page.close(new_set_modal)
        self.page.update()
        start_brew(page=self.page)

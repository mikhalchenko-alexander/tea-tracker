import flet as ft
from flet_core import StrokeCap, TextAlign, padding, Border, \
    BorderSide, Container
from mopyx import render

from state.timer.timer_state import timer_model
from styling.styles import Color, Font

SIZE = 170


class TextContainer(Container):
    def __init__(self, top: int, text: str, color: Color, font_family: Font, size: int, underline: bool = True):
        super().__init__()
        self.left = 43
        self.width = 85
        self.top = top
        self.content = ft.Text(
            text,
            color=color,
            text_align=TextAlign.CENTER,
            font_family=font_family,
            size=size
        )
        self.padding = padding.only(bottom=10)

        if underline:
            self.border = Border(
                bottom=BorderSide(1, color=Color.LIGHT)
            )


def format_seconds(seconds):
    sign = "-" if seconds < 0 else ""

    abs_seconds = abs(seconds)

    hours = abs_seconds // 3600
    minutes = (abs_seconds % 3600) // 60
    secs = abs_seconds % 60

    if hours > 0:
        return f"{sign}{hours:02}:{minutes:02}:{secs:02}"
    else:
        return f"{sign}{minutes:02}:{secs:02}"


class Timer(ft.Container):

    def __init__(self, current_brew_time: float, current_brew_time_total_brew_time: float):
        super().__init__()
        self.current_brew_time = current_brew_time
        self.current_brew_time_total_brew_timee = current_brew_time_total_brew_time
        self.timer_render()

    @render
    def timer_render(self):
        self.content = ft.Stack(
            controls=[
                ft.ProgressRing(
                    bgcolor=Color.LIGHT_TRANSPARENT if timer_model.current_time >= 0 else Color.RED,
                    value=0,
                    stroke_width=20,
                    width=SIZE,
                    height=SIZE
                ),
                ft.ProgressRing(
                    bgcolor=Color.TRANSPARENT,
                    color=Color.ORANGE,
                    stroke_cap=StrokeCap.ROUND,
                    value=timer_model.current_time / timer_model.brew_time,
                    stroke_width=14,
                    width=SIZE,
                    height=SIZE,
                    scale=ft.Scale(scale_x=-1)
                ),
                TextContainer(
                    top=30,
                    text=format_seconds(timer_model.current_time),
                    color=Color.ORANGE,
                    font_family=Font.INKNUT_ANTIQUA_BOLD,
                    size=21
                ),
                TextContainer(
                    top=80,
                    text=format_seconds(timer_model.brew_time),
                    color=Color.LIGHT,
                    font_family=Font.INKNUT_ANTIQUA,
                    size=14
                ),
                TextContainer(
                    top=115,
                    text=format_seconds(timer_model.total_brew_time),
                    color=Color.LIGHT,
                    font_family=Font.INKNUT_ANTIQUA,
                    size=14,
                    underline=False
                )

            ]
        )

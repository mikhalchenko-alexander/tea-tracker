import flet as ft
from flet_core import StrokeCap, TextAlign, padding, Border, \
    BorderSide, Container

from ..styling.styles import Color, Font

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


class Timer(ft.Container):
    def __init__(self, current_time: float, current_brew_time: float, total_brew_time: float):
        super().__init__()
        self.content = ft.Stack(
            controls=[
                ft.ProgressRing(
                    bgcolor=Color.LIGHT_TRANSPARENT,
                    value=0,
                    stroke_width=20,
                    width=SIZE,
                    height=SIZE
                ),
                ft.ProgressRing(
                    bgcolor=Color.TRANSPARENT,
                    color=Color.ORANGE,
                    stroke_cap=StrokeCap.ROUND,
                    value=1 - current_time / current_brew_time,
                    stroke_width=14,
                    width=SIZE,
                    height=SIZE,
                    scale=ft.Scale(scale_x=-1)
                ),
                TextContainer(
                    top=30,
                    text="00:06",
                    color=Color.ORANGE,
                    font_family=Font.INKNUT_ANTIQUA_BOLD,
                    size=24
                ),
                TextContainer(
                    top=80,
                    text="00:10",
                    color=Color.LIGHT,
                    font_family=Font.INKNUT_ANTIQUA,
                    size=14
                ),
                TextContainer(
                    top=115,
                    text="01:45",
                    color=Color.LIGHT,
                    font_family=Font.INKNUT_ANTIQUA,
                    size=14,
                    underline=False
                )

            ]
        )

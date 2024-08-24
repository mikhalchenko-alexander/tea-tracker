import flet as ft
from flet_core import Alignment, StrokeCap, TextAlign, padding, Border, \
    BorderSide, Container

from styling.styles import Color, Font

SIZE = 195

class TextContainer(Container):
    def __init__(self, top: int, text: str, color: Color, font_family: Font, size: int, underline: bool = True):
        super().__init__()
        self.left = 55
        self.width=85
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
                bottom=BorderSide(2, color=Color.LIGHT)
            )

class Timer(ft.Container):
    def __init__(self, currentTime: float, currentBrewTime: float, totalBrewTime: float):
        super().__init__()
        self.alignment = Alignment(0, 0)
        self.content = ft.Stack(
            controls=[
                ft.ProgressRing(
                    bgcolor=Color.LIGHT_TRANSPARENT,
                    color=Color.ORANGE,
                    stroke_cap=StrokeCap.ROUND,
                    value=1 - currentTime / currentBrewTime,
                    stroke_width=22,
                    width=SIZE,
                    height=SIZE,
                    scale=ft.Scale(scale_x=-1)
                ),
                TextContainer(
                    top=40,
                    text="00:06",
                    color=Color.ORANGE,
                    font_family=Font.INKNUT_ANTIQUA_BOLD,
                    size=24
                ),
                TextContainer(
                    top=90,
                    text="00:10",
                    color=Color.LIGHT,
                    font_family=Font.INKNUT_ANTIQUA,
                    size=14
                ),
                TextContainer(
                    top=130,
                    text="01:45",
                    color=Color.LIGHT,
                    font_family=Font.INKNUT_ANTIQUA,
                    size=14,
                    underline=False
                )

            ]
        )

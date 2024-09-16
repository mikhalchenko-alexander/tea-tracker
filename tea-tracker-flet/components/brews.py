import flet as ft
from flet_core import CrossAxisAlignment, MainAxisAlignment

from ..styling.styles import Color, Font

max_brew = 12


class Brews(ft.Column):
    def __init__(self, current_brew: int, total_ml: int, **kwargs):
        super(Brews, self).__init__(**kwargs)
        self.current_brew = current_brew
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.spacing = 7
        self.controls = [
                            ft.Row(
                                spacing=3,
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        str(current_brew),
                                        color=Color.ORANGE,
                                        font_family=Font.INKNUT_ANTIQUA,
                                        size=16
                                    ),
                                    ft.Text(
                                        f"/{max_brew}",
                                        color=Color.LIGHT,
                                        font_family=Font.INKNUT_ANTIQUA,
                                        size=16
                                    ),
                                ]
                            )
                        ] + [ft.Image(
            src="icons/water.svg",
            color=self.get_water_color(brew),
            width=31
        ) for brew in range(1, max_brew + 1)] + [
                            ft.Text(
                                f"{total_ml} ml",
                                color=Color.ORANGE_LIGHT,
                                font_family=Font.INKNUT_ANTIQUA,
                                size=16
                            ),
                        ]

    def get_water_color(self, brew):
        if brew < self.current_brew:
            return Color.ORANGE_LIGHT
        elif brew > self.current_brew:
            return Color.LIGHT_TRANSPARENT
        else:
            return Color.ORANGE

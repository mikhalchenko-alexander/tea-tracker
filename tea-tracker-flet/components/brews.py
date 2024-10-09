import flet as ft
from flet_core import CrossAxisAlignment, MainAxisAlignment
from mopyx import render

from state.brew_state import brew_model
from styling.styles import Color, Font

max_brew = 12


def get_water_color(brew):
    if brew < brew_model.current_brew:
        return Color.ORANGE_LIGHT
    elif brew > brew_model.current_brew:
        return Color.LIGHT_TRANSPARENT
    else:
        return Color.ORANGE


class Brews(ft.Column):
    def __init__(self, current_brew: int, total_ml: int, **kwargs):
        super(Brews, self).__init__(**kwargs)
        self.brews_render()

    @render
    def brews_render(self):
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.spacing = 7
        self.controls = [
                            ft.Row(
                                spacing=3,
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        str(brew_model.current_brew),
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
            color=get_water_color(brew),
            width=31
        ) for brew in range(1, max_brew + 1)] + [
                            ft.Text(
                                f"{brew_model.total_ml} ml",
                                color=Color.ORANGE_LIGHT,
                                font_family=Font.INKNUT_ANTIQUA,
                                size=16
                            ),
                        ]

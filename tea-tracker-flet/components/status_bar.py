from typing import Optional, Union, Any

import flet as ft
from flet_core import Ref, OptionalNumber, MainAxisAlignment
from flet_core.types import ResponsiveNumber
from mopyx import render

from components.status_icon import StatusIcon
from state.scale_state import scales_model
from styling.styles import Color


class StatusBar(ft.Container):

    def __init__(self, ref: Optional[Ref] = None, expand: Union[None, bool, int] = None,
                 expand_loose: Optional[bool] = None, col: Optional[ResponsiveNumber] = None,
                 opacity: OptionalNumber = None, tooltip: Optional[str] = None, visible: Optional[bool] = None,
                 disabled: Optional[bool] = None, data: Any = None, rtl: Optional[bool] = None) -> None:
        super().__init__(ref, expand, expand_loose, col, opacity, tooltip, visible, disabled, data, rtl)
        self.border=ft.Border(
            top=ft.BorderSide(width=1, color=Color.ORANGE_LIGHT_TRANSPARENT),
            bottom=ft.BorderSide(width=1, color=Color.ORANGE_LIGHT_TRANSPARENT),
        )
        self.height=56
        self.render_indicators()

    @render
    def render_indicators(self):
        self.content=ft.Row(
            controls=[
                StatusIcon(src="icons/cup.svg", label=f"{scales_model.cup_weight} g",
                           color=(Color.ORANGE_LIGHT if scales_model.cup_present else Color.ORANGE_LIGHT_TRANSPARENT)),
                StatusIcon(src="icons/leaf.svg", label=f"{scales_model.tea_weight} g",
                           color=(Color.ORANGE_LIGHT if scales_model.tea_present else Color.ORANGE_LIGHT_TRANSPARENT)),
                StatusIcon(src="icons/water.svg", label=f"{scales_model.water_weight} ml", color=(
                    Color.ORANGE_LIGHT if scales_model.water_present else Color.ORANGE_LIGHT_TRANSPARENT)),
                StatusIcon(src="icons/lid.svg", label=f"{scales_model.lid_weight} g",
                           color=(Color.ORANGE_LIGHT if scales_model.lid_present else Color.ORANGE_LIGHT_TRANSPARENT),
                           show_border=False)
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN
        )

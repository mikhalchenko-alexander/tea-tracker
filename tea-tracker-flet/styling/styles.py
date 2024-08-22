from enum import StrEnum


class Color(StrEnum):
    GREEN_MAIN = "#318653",
    GREEN_LIGHT = "#71BD85",
    ORANGE_LIGHT = "#FAD074",
    ORANGE_LIGHT_TRANSPARENT = "#99FAD074",
    ORANGE = "#FFC634",
    LIGHT = "#FFF0E1",
    LIGHT_TRANSPARENT = "#4CFFF0E1",
    BLACK = "#272726"


class Font(StrEnum):
    INKNUT_ANTIQUA = "fonts/InknutAntiqua-Regular.ttf"
    INKNUT_ANTIQUA_BOLD = "fonts/InknutAntiqua-Bold.ttf"
    INKNUT_ANTIQUA_LIGHT = "fonts/InknutAntiqua-Light.ttf"

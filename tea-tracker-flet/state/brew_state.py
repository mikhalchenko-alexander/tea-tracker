from mopyx import model


@model
class BrewModel:
    def __init__(self):
        self.current_brew = 0
        self.total_ml = 0


brew_model = BrewModel()

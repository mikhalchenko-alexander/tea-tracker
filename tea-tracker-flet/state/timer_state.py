from mopyx import model


@model
class TimerModel:
    def __init__(self):
        self.current_time = 0
        self.brew_time = 10
        self.total_brew_time = 0
        self.is_ticking = False


timer_model = TimerModel()

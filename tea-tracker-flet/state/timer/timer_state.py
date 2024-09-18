from mopyx import model


@model
class TimerModel:
    def __init__(self):
        self.current_time = 0


timer_model = TimerModel()

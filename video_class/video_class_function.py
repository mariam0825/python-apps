class video_class(object):

    def __init__(self, title: str,duration :float,playback_position: float) -> None:
        self.title = title
        self.duration = duration
        self.playback_position = playback_position

    def play(self, title: str, playback_position: float):
        if playback_position < 0:
            raise ValueError("The video have not been played yet")
        else:
            self.playback_position = playback_position
            self.title = title

    def advance(self, minutes : float):
        self.playback_position += minutes

        if self.playback_position > self.duration:
            self.playback_position = self.duration

    def is_finished(self):
        return self.playback_position == self.duration

    def restart(self):
        self.playback_position = 0

    def time_remaining(self):
        return self.duration - self.playback_position
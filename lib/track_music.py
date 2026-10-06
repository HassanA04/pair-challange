class Track_Music():
    def __init__(self):
        self.music_list = []

    def add_track(self, track):
        if len(track) == 0:
            raise ValueError("Can't input empty string")


    def view_music_list(self):
        return self.music_list

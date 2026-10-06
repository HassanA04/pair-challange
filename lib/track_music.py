class Track_Music():
    def __init__(self):
        self.music_list = []

    def add_track(self, track):
        if not isinstance(track, str):
            raise TypeError("Can only input strings")

        if len(track) == 0:
            raise ValueError("Can't input empty string")


        self.music_list.append(track)


    def view_music_list(self):
        return self.music_list

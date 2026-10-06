As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


example:

class Track_Music():
    def __init__(self):
        self.music_list = []

    def add_track(self, track):
        adds track to list

    def view_music_list():
        view the whole list of music



def test_view_music():
    -> returns list of music

def test_add_valid_track():
    -> adds track to list
    -> to check call view music

def test_add_invalid_track():
    -> excpetion check for value error and type error
    
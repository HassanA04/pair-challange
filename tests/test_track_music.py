import pytest
from lib.track_music import *

def test_view_music():
    music_tracker = Track_Music()
    assert music_tracker.view_music_list() == []

def test_add_invalid_track_for_empty_str():
    music_tracker = Track_Music()
    with pytest.raises(ValueError, match="Can't input empty string"):
        music_tracker.add_track("")
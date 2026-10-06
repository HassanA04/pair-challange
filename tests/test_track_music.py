import pytest
from lib.track_music import *

def test_view_music():
    music_tracker = Track_Music()
    assert music_tracker.view_music_list() == []

def test_add_invalid_track_for_empty_str():
    music_tracker = Track_Music()
    with pytest.raises(ValueError, match="Can't input empty string"):
        music_tracker.add_track("")


def test_add_valid_track():
    music_tracker = Track_Music()
    music_tracker.add_track("Thriller")
    assert music_tracker.view_music_list() == ["Thriller"]


def test_add_track_for_invalid_type():
    music_tracker = Track_Music()
    with pytest.raises(TypeError, match="Can only input strings"):
        music_tracker.add_track(1)

    with pytest.raises(TypeError, match="Can only input strings"):
            music_tracker.add_track(1.5)
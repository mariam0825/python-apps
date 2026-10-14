import unittest
from video_class_function import *

class videoClassTest(unittest.TestCase):
    def test_that_video_can_be_created(self):
        video = video_class("Spiderman", 2000, 60)
        self.assertEqual(video.duration, 2000)
        self.assertEqual(video.title, "Spiderman")
        self.assertEqual(video.playback_position,  60)

    def test_that_video_is_now_playing(self):
        video = video_class("Spiderman", 2000, 60)

        self.assertEqual(video. title, "Spiderman")
        self.assertEqual(video.playback_position, 60)

    def test_that_video_can_advance(self):
        video = video_class("Spiderman", 2000, 60)
        video.advance(100)
        self.assertEqual(video.playback_position, 160)

    def test_that_video_does_not_go_past_duration(self):
        video = video_class("Spiderman", 2000, 60)
        video.advance(3000)
        self.assertEqual(video.playback_position, 2000)

    def test_that_video_is_finished(self):
        video = video_class("Spiderman", 2000, 2000)
        self.assertTrue(video.is_finished())

    def test_that_video_can_restart(self):
        video = video_class("Spiderman", 2000, 500)
        video.restart()
        self.assertEqual(video.playback_position, 0)

    def test_time_remaining(self):
        video = video_class("Spiderman", 2000, 60)

        self.assertEqual(video.time_remaining(), 1940)
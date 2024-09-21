
class VideoConverter:
    def __init__(self):
        self.url = ""
        self.audio_segment_len = 0
        self.src_video_title = ""
        self.src_video_len = (0, 0, 0)  # (hr, min, sec)
        self.num_segments = 0

        
    def load_video(self, url, audio_segment_len, num_segment):
        """
        Take URL and load it into memory.
        """
        pass
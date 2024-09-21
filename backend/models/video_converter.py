import os
from pytube import YouTube
from pydub import AudioSegment
from io import BytesIO
from utils.custom_logger import CustomLogger
from constants.constants import MAX_AUDIO_LENGTH_SECS

# Defined constants
LOGGER = CustomLogger(__name__, level=10).get_logger()


class VideoConverter:
    def __init__(self):
        self.url = ""
        self.audio_segment_len = 0
        self.src_video_title = ""
        self.src_video_len = (0, 0, 0)  # (hr, min, sec)
        self.num_segments = 0
        # self.full_audio = None

        
    def process_video_url(self, url, audio_segment_len):
        """
        Take URL and load it into memory.
        """
        # Update all video meta
        self.url = url
        self.audio_segment_len = audio_segment_len

        # Download video and process it
        try:
            yt_video = YouTube(url)
            self.src_video_title = yt_video.title
            LOGGER.debug(f'Successfully downloaded Youtube video from URL: {self.url}')

            total_video_len = yt_video.length
            hr, rem = divmod(total_video_len, 3600)
            min, sec = divmod(rem, 60)
            self.src_video_len = (hr, min, sec)
            LOGGER.info(f'YouTube video title: {self.src_video_title} Length: {self.src_video_len}')

            # Extract Only audio and load into memory
            audio_stream = yt_video.streams.filter(only_audio=True).first()
            audio_file = BytesIO()
            audio_stream.stream_to_buffer(audio_file)

            # Save audio to file
            audio_file.seek(0)
            audio = AudioSegment.from_file(audio_file, format="mp4")
            LOGGER.info(f'Successfully converted video {self.url} to audio')

            return audio[:MAX_AUDIO_LENGTH_SECS * 1000]

        except Exception as ex:
            LOGGER.error(f'Failed to process YouTube URL {url}: {ex}')


    def split_audio_into_segments(self, audio):
        """
        Split processed audio into segments.
        """
        max_segments = MAX_AUDIO_LENGTH_SECS // self.audio_segment_len
        segments = []
        segment_duration_ms = self.audio_segment_len * 1000

        # iterage through entire audio range and spilt into segments
        for i in range(0, len(audio), segment_duration_ms):
            segments.append(audio[i:i + segment_duration_ms])
        
        self.num_segments = min(len(segments), max_segments)
        LOGGER.info(f'{self.src_video_title} is cut into {self.num_segments} segments.')

        return segments







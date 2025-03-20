import os
from pytube import YouTube
from pydub import AudioSegment
from io import BytesIO
from utils.custom_logger import CustomLogger
from constants.constants import MAX_AUDIO_SEGMENT_COUNT, MAX_AUDIO_SEGMENT_LENGTH_SECS, AUDIO_SEGMENT_FILE


# Defined constants
LOGGER = CustomLogger(__name__, level=10).get_logger()


class VideoConverter:
    def __init__(self):
        self.url = "some_url"
        self.src_video_title = "some_title"
        self.src_video_len = (0, 0, 0)  # (hr, min, sec)
        self.local_audio_dir = "/tmp/"
        self.audio_file_names = []
        self.project_id = "id1234"

        
    def process_video_url(self, url, project_id, destination_dir):
        """
        Take URL and load it into memory.
        """
        # Update all video meta
        self.url = url
        self.local_audio_dir = destination_dir

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
            yt_audio = AudioSegment.from_file(audio_file, format="mp4")
            LOGGER.info(f'Successfully converted video {self.url} to audio')

            # Split the audio into segments
            audio_segments = self.split_audio_into_segments(yt_audio)
            self._save_segments_to_wav(project_id=project_id, destination_dir=self.local_audio_dir)

            return {
                "url": self.url,
                "src_video_title": self.src_video_title,
                "src_video_length": self.src_video_len,
                "temp_audio_dir": self.local_audio_dir,
                "audio_segments": self.audio_file_names,
                "project_id": self.project_id
            }

        except Exception as ex:
            LOGGER.error(f'Failed to process YouTube URL {url}: {ex}')


    def _split_audio_into_segments(self, audio):
        """
        Split processed audio into segments.
        """
        max_audio_ms = min(MAX_AUDIO_SEGMENT_COUNT * MAX_AUDIO_SEGMENT_LENGTH_SECS * 1000, len(audio))
        # max_segments = MAX_SUPPORTED_AUDIO_LENGTH_SECS // AUDIO_SEGMENT_LENGTH_SECS
        segments = []
        segment_duration_ms = MAX_AUDIO_SEGMENT_LENGTH_SECS * 1000

        # Iterage through entire audio range and spilt into segments
        for i in range(0, len(audio), segment_duration_ms):
            try:
                segments.append(audio[i:i + segment_duration_ms])
            except:
                segments.append(audio[i:])
        
        # self.num_segments = min(len(segments), max_segments)
        LOGGER.info(f'{self.src_video_title} is cut into {len(segments)} segments.')

        return segments


    def _save_segments_to_wav(self, segments, project_id):
        """
        Save audio segments locally in /tmp.
        """
        # self.local_audio_dir = TEMP_AUDIO_DIR.format(project_id=project_id)
        if not os.path.exists(self.local_audio_dir):
            os.makedirs(self.local_audio_dir)
            LOGGER.info(f'Created temp dir for audio: {self.local_audio_dir}')

        for i, segment in enumerate(segments):
            fname = AUDIO_SEGMENT_FILE.format(project_id=project_id, part=i+1)
            fpath = os.path.join(self.local_audio_dir, fname)
            self.audio_file_names.append(fname)

            # Save the audio segment to file
            segment.export(fpath, format="wav")
            LOGGER.info(f'Saved {fname} audio segment to {fpath}')

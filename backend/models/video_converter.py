import os
from pytube import YouTube
from pydub import AudioSegment
from io import BytesIO
from utils.custom_logger import CustomLogger
from constants.constants import MAX_AUDIO_SEGMENT_COUNT, MAX_AUDIO_SEGMENT_LENGTH_SECS, AUDIO_SEGMENT_FILE


# Defined constants
LOGGER = CustomLogger(__name__, level=10).get_logger()


class VideoConverter:
    def __init__(self, url, project_id, destination_dir):
        self.url = url
        self.src_video_title = "some_title"
        self.src_video_len_secs = 0     # secs
        self.src_video_len_hours = (0, 0, 0)    # (hr, min, sec)
        self.local_audio_dir = destination_dir
        self.audio_file_names = []
        self.project_id = project_id

        # Initially process video url and update metadata
        yt_video = YouTube(self.url)
        self.src_video_title = yt_video.title
        self.audio_stream = yt_video.streams.filter(only_audio=True).first()
        LOGGER.debug(f'Successfully downloaded Youtube video from URL: {self.url}')

        self.src_video_len_secs = yt_video.length
        hr, rem = divmod(self.src_video_len_secs, 3600)
        min, sec = divmod(rem, 60)
        self.src_video_len = (hr, min, sec)
        LOGGER.info(f'YouTube video title: {self.src_video_title} Length: {self.src_video_len_hours}')

        # Calculate segments and build file names
        max_audio_segments  = min(MAX_AUDIO_SEGMENT_COUNT, self.src_video_len_secs//MAX_AUDIO_SEGMENT_LENGTH_SECS)
        for i in range(max_audio_segments):
            audio_file_name = AUDIO_SEGMENT_FILE.format(project_id=project_id, part=i+1)
            audio_file_path = os.path.join(self.local_audio_dir, audio_file_name)

            audio_segment_dict = {
                "audio_file_path": audio_file_path,
                "is_converted": False
            }
            self.audio_file_names.append(audio_segment_dict)
        
        processed_video_metadata = {
            "url": self.url,
            "src_video_title": self.src_video_title,
            "src_video_length": self.src_video_len_hours,
            "temp_audio_dir": self.local_audio_dir,
            "audio_segments": self.audio_file_names,
            "project_id": self.project_id
        }
        LOGGER.info(f"Successfully processed Youtube video metadata: {processed_video_metadata}")
        return processed_video_metadata


    def process_audio(self):
        """
        Take URL and load it into memory.
        """
        try:
            # Extract Only audio and load into memory
            # audio_stream = self.yt_video.streams.filter(only_audio=True).first()
            audio_file = BytesIO()
            self.audio_stream.stream_to_buffer(audio_file)

            # Save audio to file
            audio_file.seek(0)
            yt_audio = AudioSegment.from_file(audio_file, format="mp4")
            LOGGER.info(f'Successfully converted video {self.url} to audio')

            # Split the audio into segments
            audio_segments = self.split_audio_into_segments(yt_audio)
            self._save_segments_to_wav(project_id=self.project_id, destination_dir=self.local_audio_dir)

            return {
                "url": self.url,
                "src_video_title": self.src_video_title,
                "src_video_length": self.src_video_len_hours,
                "temp_audio_dir": self.local_audio_dir,
                "audio_segments": self.audio_file_names,
                "project_id": self.project_id
            }

        except Exception as ex:
            LOGGER.error(f'Failed to process YouTube URL {self.url}: {ex}')


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

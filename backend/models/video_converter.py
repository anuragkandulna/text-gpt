import os
import threading
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
            # Create audio directory
            if not os.path.exists(self.local_audio_dir):
                os.makedirs(self.local_audio_dir)
                LOGGER.info(f'Created temp dir for audio: {self.local_audio_dir}')

            # Extract Only audio and load into memory
            audio_file = BytesIO()
            self.audio_stream.stream_to_buffer(audio_file)
            audio_file.seek(0)

            # Split audio into segment and save
            i = 0
            for index, audio_dict in self.audio_file_names:
                try:
                    audio_part = self.audio_stream[i:i+MAX_AUDIO_SEGMENT_LENGTH_SECS]
                except:
                    audio_part = self.audio_stream[i:]
                finally:
                    file_path = audio_dict["audio_file_path"]
                    audio_part.export(file_path, format="wav")
                    self.audio_file_names[index]["is_converted"] = True
                    LOGGER.info(f'Saved audio segment {index} to {file_path}')
                    i = i + MAX_AUDIO_SEGMENT_LENGTH_SECS + 1
            
            return True

        except Exception as ex:
            LOGGER.error(f'Failed to process YouTube URL {self.url} to audio: {ex}')
            return False

    
    def process_audio_in_background(self):
        """
        Invoke thread to process audio in background.
        """
        thread = threading.Thread(target=self.process_audio)
        thread.start()


    def is_conversion_done(self, part):
        """
        Check if video conversion is completed and segmented audio file is created.
        """
        if not 0 <= part < len(self.audio_file_names):
            LOGGER.info("Invalid index.")
            return

        return  (os.path.exists(self.audio_file_names[part]["audio_file_path"]) and self.audio_file_names[part]["is_converted"])

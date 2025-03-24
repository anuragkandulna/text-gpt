import os
import threading
import speech_recognition as sr
from utils.custom_logger import CustomLogger
from constants.constants import TEMP_TRANSCRIPTION_DIR, TRANSCRIPT_SEGMENT_FILE


# Logger
LOGGER = CustomLogger(__name__, level=10).get_logger()


class AudioTranscriptionEngine:
    def __init__(self, audio_files, src_language, project_id, destination_dir):
        self.src_audio_files = audio_files
        self.src_language = src_language
        self.project_id = project_id
        self.local_transcript_dir = destination_dir
        self.transcript_files = []
        
        max_audio_files = len(self.src_audio_files)
        for i in range(max_audio_files):
            transcript_file_name = TRANSCRIPT_SEGMENT_FILE.format(project_id=self.project_id, part=i+1)
            transcript_file_path = os.path.join(self.local_transcript_dir, transcript_file_name)

            transcript_dict = {
                "transcript_file_path": transcript_file_path,
                "is_transcribed": False
            }
            self.transcript_files.append(transcript_dict)
        
        transcripts_metadata = {
            "project_id": self.project_id,
            "src_language": self.src_language,
            "temp_transcript_dir": self.local_transcript_dir,
            "src_audio_files": self.src_audio_files,
            "transcript_files": self.transcript_files
        }


    def transcribe_audio(self):
        """
        Transcribe source audio file using speech engine and store into /tmp/.
        """
        try:
            # Create audio directory
            if not os.path.exists(self.local_transcript_dir):
                os.makedirs(self.local_transcript_dir)
                LOGGER.info(f'Created temp dir for transcripts: {self.local_transcript_dir}')

            # Invoke transcriber:
            r = sr.Recognizer()

            for index, audio_dict in enumerate(self.src_audio_files):
                transcript_text = None
                audio_file = audio_dict["audio_file_path"]
                with sr.AudioFile(audio_file) as source:
                    stream = r.record(source)

                    try:
                        transcript_text = r.recognize_google(stream, language=self.src_language)
                    except Exception as ex:
                        LOGGER.error(f"Exception occurred when transcribing {audio_file}: {ex}")
                
                if not transcript_text:
                    transcript_file = self.transcript_files[index]["transcript_file_path"]
                    with open(transcript_file) as f:
                        f.write(transcript_text)
                    
                    self.transcript_files[index]["is_transcribed"] = True
                    LOGGER.info(f'Audio source {audio_file} transcribed to file {transcript_file} in language {self.src_language}')

        except Exception as ex:
            LOGGER.error(f"Failed to transcribe audio to text: {ex}")
            return False


    def transcribe_audio_in_background(self):
        """
        Start audio transcription one by one.
        """
        thread = threading.Thread(target=self.transcribe_audio)
        thread.start()


    def is_transcription_done(self, part):
        """
        Check if audio conversion is completed and transcript file is created.
        """
        if not 0 <= part < len(self.transcript_files):
            LOGGER.info("Invalid index.")
            return

        return  (os.path.exists(self.transcript_files[part]["transcript_file_path"]) and self.transcript_files[part]["is_transcribed"])

import os
import speech_recognition as sr
from utils.custom_logger import CustomLogger
from constants.constants import TEMP_TRANSCRIPTION_DIR, TRANSCRIPT_SEGMENT_FILE


# Logger
LOGGER = CustomLogger(__name__, level=10).get_logger()


class AudioTranscriptionEngine:

    def transcribe_audio(self, source_audio_file, source_language, project_id, part):
        """
        Transcribe source audio file using speech engine and store into /tmp/.
        """
        r = sr.Recognizer()
        text = ''

        with sr.AudioFile(source_audio_file) as source:
            stream = r.record(source)

            try:
                text = r.recognize_google(stream, language=source_language)
            except Exception as ex:
                LOGGER.error(f"Exception occurrec when transcribing {source_audio_file}: {ex}")
        
        # Write file to local path
        local_dest_dir = TEMP_TRANSCRIPTION_DIR.format(project_id=project_id)
        local_fname = TRANSCRIPT_SEGMENT_FILE.format(project_id=project_id, part=part)
        local_transcript_full_path = os.path.join(local_dest_dir, local_fname)
        with open(local_transcript_full_path) as f:
            f.write(text)
        
        LOGGER.info(f'Audio source {source_audio_file} transcribed to file {local_transcript_full_path}')
        return {
            "part": part,
            "source_audio_file": source_audio_file,
            "transcript_file_path": local_transcript_full_path,
            "transcript_file_name": local_fname,
            "data": text
        }

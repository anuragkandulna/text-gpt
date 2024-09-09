"""
Project data model.
"""

from datetime import datetime

class Project:
    def __init__(self):
        self.project_id = ""
        self.title = ""
        self.url = ""
        self.audio_segment_len = 0
        self.src_video_lang = ""
        self.src_video_title = ""
        self.src_video_len = (0, 0, 0)  # (hr, min, sec)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False
        self.translate_to_lang = ""
        self.num_segments = 0
        self.audio_dir = ""
        self.transcription_dir = ""
        self.translation_dir = ""
        self.summary_dir = ""
        self.seg_audio_files = []
        self.seg_transcript_files = []
        self.seg_translation_files = []
        self.seg_summary_files = []
        self.final_transcript_file = ""
        self.final_translation_file = ""
        self.final_summary_file = ""


    def create_project(self, title, url, audio_segment_len, src_video_lang):
        """
        Create a new project.
        """
        self.project_id = f"proj_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.title = title
        self.url = url
        self.audio_segment_len = audio_segment_len
        self.src_video_lang = src_video_lang
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.is_deleted = False

        # Initialize directories using project_id as root
        self.audio_dir = f"./{self.project_id}/audio/"
        self.transcription_dir = f"./{self.project_id}/transcriptions/"
        self.translation_dir = f"./{self.project_id}/translations/"
        self.summary_dir = f"./{self.project_id}/summaries/"

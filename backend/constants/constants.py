"""All project related constants."""

MAX_SUPPORTED_AUDIO_LENGTH_SECS = 240
AUDIO_SEGMENT_LENGTH_SECS = 10
TEMP_AUDIO_DIR = "/tmp/{project_id}/audio/"
TEMP_TRANSCRIPTION_DIR = "/tmp/{project_id}/transcription/"
TEMP_TRANSLATION_DIR = "/tmp/{project_id}/translation/"
TEMP_SUMMARY_DIR = "/tmp/{project_id}/translation/"
AUDIO_SEGMENT_FILE = "audio_{project_id}_segment_{part}.wav"
TRANSCRIPT_SEGMENT_FILE = "transcript_{project_id}_segment_{part}.txt"
TRANSLATION_SEGMENT_FILE = "translation_{project_id}_segment_{part}.txt"
SUMMARY_FILE = "summary_{project_id}.txt"


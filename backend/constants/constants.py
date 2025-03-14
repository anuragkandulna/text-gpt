"""All project related constants."""

### Project related constants
MAX_SUPPORTED_AUDIO_LENGTH_SECS = 2
AUDIO_SEGMENT_LENGTH_SECS = 5
TEMP_TEXTGPT_DIR = "/var/tmp/textgpt"
TEMP_AUDIO_DIR = f"{TEMP_TEXTGPT_DIR}/{project_id}/audio/"
TEMP_TRANSCRIPTION_DIR = f"{TEMP_TEXTGPT_DIR}/{project_id}/transcription/"
TEMP_TRANSLATION_DIR = f"{TEMP_TEXTGPT_DIR}/{project_id}/translation/"
TEMP_SUMMARY_DIR = f"{TEMP_TEXTGPT_DIR}/{project_id}/translation/"
AUDIO_SEGMENT_FILE = "audio_{project_id}_segment_{part}.wav"
TRANSCRIPT_SEGMENT_FILE = "transcript_{project_id}_segment_{part}.txt"
TRANSLATION_SEGMENT_FILE = "translation_{project_id}_segment_{part}.txt"
SUMMARY_FILE = "summary_{project_id}.txt"

### OpenAI related constants
MAX_TEMPERATURE = 0.7
MAX_TOKENS = 100


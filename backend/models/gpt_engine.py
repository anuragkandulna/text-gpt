import openai
import os
from variables import OPENAI_API_KEY
from utils.custom_logger import CustomLogger

# Logger
LOGGER = CustomLogger(__name__, level=10).get_logger()


class GPTEngine:
    def __init__(self, api_key=OPENAI_API_KEY):
        """
        Initialize OpenAI for text based operations.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    
    def translate_text(self, text, target_language):
        """
        Translate source text into target language.
        """
        if not text.strip():
            LOGGER.error("Empty text provided for translation.")
            return None
        
        
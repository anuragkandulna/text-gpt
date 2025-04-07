from openai import OpenAI
import os
from constants.config import OPENAI_API_KEY
from constants.prompts import TRANSLATE_PROMPT_1, SUMMARY_PROPMPT_1
from constants.constants import MAX_TEMPERATURE, MAX_TOKENS
from utils.custom_logger import CustomLogger

# Logger
LOGGER = CustomLogger(__name__, level=10).get_logger()
client = OpenAI(api_key = OPENAI_API_KEY)


class GPTEngine:    
    def __init__(self, project_id, transcript_files):
        self.project_id = project_id,
        self.transcript_files = transcript_files

        # Combine transcripts into single file
        transcript_input_text = ''
        for index, transcript_dict in self.transcript_files:
            pass


    def _translate_text(self, text, src_language, target_language):
        """
        Translate source text into target language.
        """
        if not text.strip():
            LOGGER.error("Empty text provided for translation.")
            return None
        
        prompt_t = TRANSLATE_PROMPT_1.format(src_language=src_language, target_language=target_language, text=text)

        try:
            response_t = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "user",
                    "content": prompt_t
                }],
                temperature=MAX_TEMPERATURE,
                max_tokens=MAX_TOKENS
            )

            LOGGER.debug(f"Translation prompt: {prompt_t}")
            LOGGER.debug(f"Translation response: {response_t}")
            translation = response_t.choices[0].message.content.strip()
            LOGGER.info(f"Translation successful: {translation}")
            return translation

        except Exception as ex:
            LOGGER.error(f"Error occurred when translation: {ex}")
            return None


    def _summarize_text(self, text):
        """
        Summarize text while preserving context.
        """
        if not text:
            LOGGER.error("Empty text provided for summarization.")
            return None
        
        prompt_s = SUMMARY_PROPMPT_1.format(text=text)

        try:
            response_s = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "user",
                    "content": prompt_s
                }],
                temperature=MAX_TEMPERATURE,
                max_tokens=MAX_TOKENS
            )

            LOGGER.debug(f"Summary prompt: {prompt_s}")
            LOGGER.debug(f"Summary response: {response_s}")
            summary = response_s.choices[0].message.content.strip()
            LOGGER.info(f"Summarization success: {summary}")
            return summary

        except Exception as ex:
            LOGGER.error(f"Error occurred when summarization: {ex}")
            return None


# if __name__ == "__main__":
#     obj = GPTEngine()

#     inp_text = "How are you?"
#     src = "English"
#     tgt = "Hindi"

#     opt_text = obj.translate_text(
#         text=inp_text,
#         src_language=src,
#         target_language=tgt
#     )

#     print(opt_text)
        
        
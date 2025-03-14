from openai import OpenAI
import os
from constants.config import OPENAI_API_KEY
from constants.prompts import TRANSLATE_PROMPT_1
from utils.custom_logger import CustomLogger

# Logger
LOGGER = CustomLogger(__name__, level=10).get_logger()
client = OpenAI(api_key = OPENAI_API_KEY)


class GPTEngine:    
    def translate_text(self, text, src_language, target_language):
        """
        Translate source text into target language.
        """
        if not text.strip():
            LOGGER.error("Empty text provided for translation.")
            return None
        
        prompt = TRANSLATE_PROMPT_1.format(src_language=src_language, target_language=target_language, text=text)

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "user",
                    "content": prompt
                }],
                temperature=0.7,
                max_tokens=100
            )

            translation = response.choices[0].message.content.strip()
            LOGGER.info(f"Translation successful: {translation}")
            return translation

        except Exception as ex:
            LOGGER.error(f"OpenAPI error: {ex}")
            return None


if __name__ == "__main__":
    obj = GPTEngine()

    inp_text = "How are you?"
    src = "English"
    tgt = "Hindi"

    opt_text = obj.translate_text(
        text=inp_text,
        src_language=src,
        target_language=tgt
    )

    print(opt_text)
        
        
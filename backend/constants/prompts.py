"""All prompts related to translation/summarization."""

TRANSLATE_PROMPT_1 = """Translate the following text from {src_language} to {target_language}: '{text}'"""
TRANSLATE_PROMPT_2 = """Provide a literal word-for-word translation of this sentence from {src_language} to {target_language}: '{text}'"""
TRANSLATE_PROMPT_3 = """Provide a natural, fluent translation of this text from {src_language} to {target_language}: '{text}'"""
TRANSLATE_PROMPT_4 = """Translate this paragraph from {src_language} to {target_language} while keeping the tone and meaning intact: '{text}'"""
TRANSLATE_PROMPT_5 = """Translate this technical/legal/medical text from {src_language} to {target_language} with precise terminology: '{text}'"""
TRANSLATE_PROMPT_6 = """Translate this text while preserving cultural nuances and idioms in {target_language}:  '{text}'"""
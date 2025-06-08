# translator.py

from googletrans import Translator

def translate_text(text, dest_lang="zh-TW"):
    translator = Translator()
    result = translator.translate(text, dest=dest_lang)
    return result.text

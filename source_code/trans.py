from googletrans import Translator

translator = Translator()

def translate(text, source='as', target='en'):
  """Translates text from source language to target language.

  Args:
    text: The text to translate.
    source: The source language code.
    target: The target language code.

  Returns:
    The translated text
  """

  translation = translator.translate(text, src=source, dest=target)
  return translation.text


# Translate a sentence from Assamese to English.
sentence = 'মই এখন কাম কৰি আছোঁ।'
translation = translate(sentence)

print(translation)
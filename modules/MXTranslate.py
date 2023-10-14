from mtranslate import translate
import time

def translate_text(text, target_language):
    try:
        translated = translate(text,target_language,"auto")
        return translated
    except Exception as e:
        print(f"Hata oluştu: {e}")
        time.sleep(60)
        return "Ceviri olmadığı durumda oluşacak bir hata mesajıdır"  # Hata durumunda belirtilen metin

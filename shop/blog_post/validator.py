import os
import tempfile
from django.core.exceptions import ValidationError


def video_time(value):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
        for chunk in value.chunks():
            temp_file.write(chunk)
        temp_file_path = temp_file.name
    try:
        size = os.path.getsize(temp_file_path)
        print(size)
        # if clip.duration > 20:  # Agar video 20 soniyadan uzun bo'lsa
        #     raise ValidationError("Video uzunligi 20 soniyadan oshmasligi kerak!")
    except Exception:
        raise ValidationError("Video faylini tekshirib bo‘lmadi!")
    finally:
        os.remove(temp_file_path)  # Faylni o‘chirish
    return value

from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import timedelta


def validate_archive_time(created_at):
    """Post 3 soniyadan keyin avtomatik arxivlanishi uchun validator"""
    min_time = created_at + timedelta(seconds=3)  # 3 soniya qo‘shamiz
    if now() < min_time:
        raise ValidationError("Post 3 soniya oldin arxivlanishi mumkin emas!")

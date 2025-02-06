from django.db import models


class VerificationCode(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Code for {self.email}"

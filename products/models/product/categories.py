from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True)
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    def __str__(self):
        return self.name

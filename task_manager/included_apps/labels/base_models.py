from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'), unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

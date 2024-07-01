from django.db import models
from .base_models import BaseModel
from django.utils.translation import gettext_lazy as _


class Label(BaseModel):
    class Meta(BaseModel.Meta):
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')

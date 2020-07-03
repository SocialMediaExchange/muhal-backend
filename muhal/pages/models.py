from django.db import models
from django.utils.translation import gettext_lazy as _


class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    slug = models.SlugField(max_length=100, verbose_name=_('slug'))
    text = models.TextField(verbose_name=_('Text'), help_text=_('Content of the static page, in Markdown'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    last_modified = models.DateTimeField(auto_now_add=True, verbose_name=_('Last modified'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse
# Create your models here.
@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField("Column name", max_length=256)
    slug = models.CharField("Column address", max_length=256, db_index=True)
    intro = models.TextField("Column Introduce", default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))

    class Meta:
        verbose_name = 'Column'
        verbose_name_plural = 'Column'
        ordering = ['name'] #order by Columen

@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name="Column belonged")

    title = models.CharField('Title', max_length=256)
    slug = models.CharField('Address', max_length=256, db_index=True)

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='Author')
    content = UEditorField('content', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')

    pub_date = models.DateTimeField('Publish Time', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('Update Time', auto_now=True, null=True)

    published = models.BooleanField('Publish', default=True)

    def get_absolute_url(self):
        return reverse('article', args=(self.slug,))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'example'
        verbose_name_plural = 'example'
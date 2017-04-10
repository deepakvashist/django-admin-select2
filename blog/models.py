# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(u'Nome', max_length=150)
    email = models.EmailField(u'E-mail', max_length=254)

    class Meta:
        verbose_name=u'Autor'
        verbose_name_plural=u'Autores'

    def __unicode__(self):
        return self.name


class CategoryPriority(models.Model):
    priority = models.PositiveIntegerField(u'Prioridade')
    category = models.ForeignKey('blog.Category', verbose_name='Categoria')

    class Meta:
        verbose_name='Prioridade de Categoria'
        verbose_name_plural='Prioridades de Categorias'

    def __unicode__(self):
        return self.category.name


class Category(models.Model):
    name = models.CharField(u'Nome da categoria', max_length=100)

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(u'Título do Post', max_length=255)
    author = models.ForeignKey('blog.Author', verbose_name='Autor do Post')
    category = models.ManyToManyField('blog.Category', verbose_name='Categorias')

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __unicode__(self):
        return self.title

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from admin_filter_select2 import AdminSelect2RelatedFilterWidget

from .models import Author, Category, CategoryPriority, Post


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class CategoryPriorityAdmin(admin.ModelAdmin):
    list_display = ('category', 'priority')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author__name')
    filter_horizontal = ['category', ]
    list_filter = (('author', AdminSelect2RelatedFilterWidget), ('category', AdminSelect2RelatedFilterWidget))


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryPriority, CategoryPriorityAdmin)
admin.site.register(Post, PostAdmin)

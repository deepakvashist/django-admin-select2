# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.utils import get_model_from_relation

from admin_filter_form_select2 import AdminSelect2RelatedFilterModelForm


class AdminSelect2RelatedFilterWidget(admin.filters.FieldListFilter):
    template = 'admin_filter_select2.html'  # Sobrescrevemos o template padrão de form

    def __init__(self, field, request, params, model, model_admin, field_path):
        other_model = get_model_from_relation(field)
        self.lookup_kwarg = '%s__%s__exact' % (field_path, field.target_field.name)
        self.lookup_kwarg_isnull = '%s__isnull' % field_path
        self.lookup_val = request.GET.get(self.lookup_kwarg)
        self.lookup_val_isnull = request.GET.get(self.lookup_kwarg_isnull)
        self.field_model = field
        super(AdminSelect2RelatedFilterWidget, self).__init__(
            field, request, params, model, model_admin, field_path)
        self.lookup_choices = self.field_choices(field, request, model_admin)
        if hasattr(field, 'verbose_name'):
            self.lookup_title = field.verbose_name
        else:
            self.lookup_title = other_model._meta.verbose_name
        self.title = self.lookup_title
        self.empty_value_display = model_admin.get_empty_value_display()
        self.form = self.get_form(request)

    def get_form(self, request):
        return AdminSelect2RelatedFilterModelForm(data=self.used_parameters,
                                                  field_name=self.field_path,
                                                  field_model=self.field_model,
                                                  lookup_kwarg=self.lookup_kwarg)

    def expected_parameters(self):
        return [self.lookup_kwarg, self.lookup_kwarg_isnull]

    def field_choices(self, field, request, model_admin):
        """
        Através desse método, sobrescrevemos a query padrão do Django,
        evitando assim a execução de uma query não necessária.
        """
        return []

    def choices(self, changelist):
        """
        Método necessário para passar na validção do Django.
        Os campos utilizados no select2 são retornados no momento
        da query nos forms (AdminSelect2RelatedFilterModelForm).
        """
        return []

    def queryset(self, request, queryset):
        filter_params = {}
        if self.lookup_val:
            filter_params[self.lookup_kwarg] = self.lookup_val
        if filter_params:
            return queryset.filter(**filter_params)
        return queryset

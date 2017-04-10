# -*- coding: utf-8 -*-
from django import forms

from django_select2.forms import ModelSelect2Widget, Select2Widget


class AdminSelect2RelatedFilterModelForm(forms.Form):
    """
    Form padrão para utilizar em conjunto com o plugin select2 nos filtros
    do admin.
    """
    field_name = None
    field_model = None
    lookup_kwarg = None

    def __init__(self, *args, **kwargs):
        self.field_name = kwargs.pop('field_name')
        self.field_model = kwargs.pop('field_model')
        self.lookup_kwarg = kwargs.pop('lookup_kwarg')
        super(AdminSelect2RelatedFilterModelForm, self).__init__(*args, **kwargs)

        self.fields[self.lookup_kwarg] = forms.ModelMultipleChoiceField(
                widget=ModelSelect2Widget(
                    queryset=self.field_model.related_model._default_manager.all(),
                    search_fields = ['name__icontains', ],
                    max_results=4
                ),
                queryset=self.field_model.related_model._default_manager.all(),
                label=self.field_model.verbose_name,
                required=False
            )

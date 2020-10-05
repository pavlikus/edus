from django import forms

from .models import Course


class CourseCreateForm(forms.ModelForm):

    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            if (hasattr(visible.field.widget, 'input_type') and
                    visible.field.widget.input_type == 'checkbox'):
                visible.field.widget.attrs['class'] = 'form-checkbox-input'
            elif (hasattr(visible.field.widget, 'input_type') and
                    visible.field.widget.input_type == 'radio'):
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    def is_valid(self):
        data = super().is_valid()
        for i in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[i].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return data

    class Meta:
        model = Course
        fields = '__all__'

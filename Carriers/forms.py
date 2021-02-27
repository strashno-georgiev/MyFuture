from django import forms

class MyForm(forms.Form):
    type = forms.CharField(label='Вашият 4-буквен код:', max_length=4)

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['type'].widget.attrs['cols'] = 5
        self.fields['type'].widget.attrs['rows'] = 5

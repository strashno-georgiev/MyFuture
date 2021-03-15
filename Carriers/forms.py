from django import forms

class CodeForm(forms.Form):
    type = forms.CharField(label='Вашият 4-буквен код:', max_length=4)

    def __init__(self, *args, **kwargs):
        super(CodeForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['type'].widget.attrs['autofocus'] = "autofocus"
        self.fields['type'].widget.attrs['class'] = "home-input"

class EventForm(forms.Form):
    email = forms.CharField(label="Въведете имейла си:")
    
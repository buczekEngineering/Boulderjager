from django import forms

from .models import Boulder


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class AddBoulderForm(forms.ModelForm):


    class Meta:
        model = Boulder
        fields = [f'boulder_{i}' for i in range(1, 41)]

    def __init__(self, available_boulders, *args, **kwargs):
        super(AddBoulderForm, self).__init__(*args, **kwargs)

        CHOICES = [
            ('None', 'None'),
            ('Bonus', 'Bonus'),
            ('Top', 'Top'),
        ]
        for i in range(1, 41):
            field_name = f'boulder_{i}'
            self.fields[field_name] = forms.ChoiceField(choices=CHOICES,
                                                        initial='None', widget=forms.Select(attrs={'class': 'form-control'}))

from django import forms

from .models import Boulder


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class AddBoulderForm(forms.ModelForm):
    CHOICES = (
        ('None', 'None'),
        ('Bonus', 'Bonus'),
        ('Top', 'Top'),
    )

    boulder_1 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_2 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_3 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_4 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_5 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_6 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_7 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_8 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_9 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_10 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_11 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_12 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_13 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_14 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_15 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_16 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_17 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_18 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_19 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_20 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_21 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_22 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_23 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_24 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_25 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_26 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_27 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_28 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_29 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_30 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_31 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_32 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_33 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_34 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_35 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_36 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_37 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_38 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_39 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))
    boulder_40 = forms.ChoiceField(choices=CHOICES, initial='None', widget=forms.Select(attrs={'class': 'form-control'}))



    class Meta:
        model = Boulder
        fields = ['boulder_1', 'boulder_2', 'boulder_3','boulder_3',
                  'boulder_3', 'boulder_4', 'boulder_5','boulder_5',
                  'boulder_6', 'boulder_7', 'boulder_8','boulder_8',
                    'boulder_9', 'boulder_10', 'boulder_11','boulder_11',
                    'boulder_12', 'boulder_13', 'boulder_14','boulder_14',
                    'boulder_15', 'boulder_16', 'boulder_17','boulder_17',
                    'boulder_18', 'boulder_19', 'boulder_20','boulder_20',
                    'boulder_21', 'boulder_22', 'boulder_23','boulder_23',
                    'boulder_24', 'boulder_25', 'boulder_26','boulder_26',
                    'boulder_27', 'boulder_28', 'boulder_29','boulder_29',
                    'boulder_30', 'boulder_31', 'boulder_32','boulder_32',
                      'boulder_33', 'boulder_34', 'boulder_35','boulder_35',
                        'boulder_36', 'boulder_37', 'boulder_38','boulder_38',
                  'boulder_39', 'boulder_40']

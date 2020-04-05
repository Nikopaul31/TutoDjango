from django import forms

class TestForm(forms.Form):

    PLAN_CHOICES = (
        (0, 'Basic'),
        (1, 'Premium'),
        (2, 'Deluxe'),
    )

    ADDITIONNAL_OPTIONS = [
        ('storage', 'Extra storage +10GB'),
        ('support', 'Support On-Site 24/7'),
        ('account', 'Additional account'),
    ]

    name = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField(label='Your email', max_length=50, required=False)
    signup_to_newsletter = forms.BooleanField(label='Signup to newsletter')
    plan = forms.ChoiceField(label='Your plan', choices = PLAN_CHOICES)

    additional_options = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=ADDITIONNAL_OPTIONS,
    )
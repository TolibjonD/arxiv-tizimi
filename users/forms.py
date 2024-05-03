from django import forms
from users.models import CustomUser

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = CustomUser
        fields = ["username","password", "first_name", "last_name", "email", "phone", "photo", "birth_date"]

    def save(self, commit=True):
        instance = super(SignUpForm, self).save(commit=False)
        instance.set_password(self.cleaned_data['password'])
        if commit:
            instance.save()
        return instance
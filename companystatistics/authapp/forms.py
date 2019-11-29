from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
import django.forms as forms

from statapp.models import Department
from .models import User, UserProfile


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'email',
            'password'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (

        )

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# class DepartmentEnrollForm(forms.Form):
#     department = forms.ModelChoiceField(queryset=Department.objects.all(),
#                                         widget=forms.HiddenInput)

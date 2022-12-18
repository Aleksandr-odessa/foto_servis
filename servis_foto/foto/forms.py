from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    # def __init__(self, *args, **kwargs):
    #     super(CreateUserForm, self).__init__(*args, **kwargs)

        # self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        # self.fields['username'].label = 'Имя пользователя'
        # self.fields['password1'].help_text = ' Длинна пароля не менее 8 символов'
        # self.fields['password1'].label = 'Пароль'
        # self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        # self.fields['username'].help_text = ' '
        # self.fields['password2'].label = 'Повторный ввод пароля'
        # self.fields['password2'].help_text = ' '
        # self.fields['password2'].widget.attrs['placeholder'] = 'Пароль'

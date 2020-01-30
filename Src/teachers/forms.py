from django.forms import ModelForm, ValidationError

from teachers.models import Teacher


class TeachersBaseForm(ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Teacher.objects.filter(email__iexact=email).exclude(email__iexact=email).exists()

        if email_exists:
            raise ValidationError(f'{email} is already used')
        return email

    def clean_phone(self):
        telephone = self.cleaned_data['telephone']
        tel_exists = Teacher.objects.filter(tel__iexact=telephone).exclude(tel__iexact=telephone).exists()

        if not telephone.isdigit():
            raise ValidationError(f' use only digits')
        elif tel_exists:
            raise ValidationError(f'{telephone} is already used')
        return telephone


class TeachersAdminForm(TeachersBaseForm):
    class Meta:
        model = Teacher
        fields = ('id', 'email', 'first_name', 'last_name', 'telephone')


class TeachersAddForm(TeachersBaseForm):
    class Meta:
        model = Teacher
        fields = '__all__'


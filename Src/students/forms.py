from django.forms import ModelForm, Form, EmailField, CharField, ValidationError
from django.core.mail import send_mail
from django.conf import settings

from students.models import Student, Group


class StudentBaseForm(ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Student.objects.filter(email__iexact=email).exclude(email__iexact=email).exists()

        if email_exists:
            raise ValidationError(f'{email} is already used')
        return email

    def clean_phone(self):
        telephone = self.cleaned_data['telephone']
        tel_exists = Student.objects.filter(tel__iexact=telephone).exclude(tel__iexact=telephone).exists()

        if tel_exists:
            raise ValidationError(f'{telephone} is already used')
        elif not telephone.isdigit():
            raise ValidationError(f'use only digits')
        return telephone


class StudentsAddForm(StudentBaseForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAdminForm(StudentBaseForm):
    class Meta:
        model = Student
        fields = ('id', 'email', 'first_name', 'last_name', 'telephone')


class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data  # valid data from form

        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, email_from, recipient_list)


class GroupsAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


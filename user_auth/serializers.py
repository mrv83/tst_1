from dj_rest_auth.registration.serializers import RegisterSerializer as DefaultRegisterSerializer
from dj_rest_auth.serializers import LoginSerializer as DefaultLoginSerializer, \
    UserDetailsSerializer as DefaultUserDetailsSerializer, \
    PasswordResetSerializer as DefaultPasswordResetSerializer, \
    PasswordResetConfirmSerializer as DefaultPasswordResetConfirmSerializer
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class LoginSerializer(DefaultLoginSerializer):
    def get_fields(self):
        fields = super().get_fields()
        del fields['username']
        return fields


class RegisterSerializer(DefaultRegisterSerializer):
    def get_fields(self):
        fields = super().get_fields()
        del fields['username']
        return fields


class PasswordResetSerializer(DefaultPasswordResetSerializer):
    def get_email_options(self):
        return {
            'email_template_name': 'email/password_reset.html',
            'html_email_template_name': 'email/password_reset.html',
            'subject_template_name': 'email/password_reset_subject.txt',
            'extra_email_context': {
                'FRONTEND_URL': settings.FRONTEND_URL
            },
        }


class PasswordResetConfirmSerializer(DefaultPasswordResetConfirmSerializer):
    def save(self):
        user = self.set_password_form.save()
        # Send email about successful password reset, email will be sent by a celery task
        # due to use of CeleryEmailBackend
        message = render_to_string('email/password_reset_end.html',
                                   {'FRONTEND_URL': settings.FRONTEND_URL,
                                    'user': user})
        email = EmailMessage('Password Reset Completed', message, to=[user.email])
        email.content_subtype = "html"
        email.send()

        return user


class UserSerializer(DefaultUserDetailsSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')

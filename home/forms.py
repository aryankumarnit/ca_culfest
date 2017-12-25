from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile, Document
from django.utils.translation import gettext_lazy as _


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

        self.fields['first_name'].widget.attrs['readonly'] = True
        self.fields['last_name'].widget.attrs['readonly'] = True
        if kwargs.get('instance'):
            emails = kwargs['instance'].email
            if str(emails) != "":
                self.fields['email'].widget.attrs['readonly'] = True
            first_names = kwargs['instance'].first_name
            if str(first_names) != "":
                self.fields['first_name'].widget.attrs['readonly'] = True
            last_names = kwargs['instance'].last_name
            if str(last_names) != "":
                self.fields['last_name'].widget.attrs['readonly'] = True

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('Primary Email Address'),
        }


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # Making name required
        self.fields['alt_email'].required = True
        self.fields['college'].required = True
        self.fields['phone'].required = True
        self.fields['year_of_grad'].required = True
        self.fields['address'].required = True
        self.fields['city'].required = True
        self.fields['state'].required = True

        for field in self.fields.values():
            field.error_messages = {
                'required': 'The field {fieldname} is required'.format(fieldname=field.label),
                'max_length': 'The length of the field is too long',
            }

    class Meta:
        model = Profile
        fields = ('alt_email', 'college', 'phone', 'year_of_grad', 'address', 'city', 'state')
        labels = {
            'alt_email': _('Alternate Email Address'),
            'college': _('College Name'),
            'phone': _('Phone Number'),
            'year_of_grad': _('Year of Graduation'),
            'address': _('Address'),
            'city': _('City'),
            'state': _('State'),
        }


class DocumentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['document'].required = True

    class Meta:
        model = Document
        fields = ('description', 'document', )
        labels = {
            'description': _('Image Description '),
        }

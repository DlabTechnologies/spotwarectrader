from django import forms
from django.contrib.auth.forms import UserCreationForm as RegForm
from django.contrib.auth.forms import UserChangeForm as ChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate
from account.models import User
from intl_tel_input.widgets import IntlTelInputWidget
from account.models import UserWithdrawRequestBtc, UserWithdrawRequestBankTransfer,  UserDepositRequest, ContactForm, ContactFormRequest, User_ID_Card_Upload, NewsletterSignup


class UserCreationForm(RegForm):
    email = forms.EmailField(max_length=60, help_text='Required. Enter a valid email address')

    referered_by = forms.CharField()
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['referered_by'].required = False  
        
    class Meta:
        model = User
        fields = ('referered_by','email','first_name','last_name','password1','password2','phone')
    

    
  


    def clean_first_name(self):
        # Get the email
        first_name = self.cleaned_data.get('first_name')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(first_name=first_name)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return first_name

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This first name  is already in use.')

    def clean_last_name(self):
        # Get the email
        last_name = self.cleaned_data.get('last_name')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(last_name=last_name)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return last_name

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This last name is already in use.')

    

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is not available.')

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label="password")
    

    class Meta:
        model = User
        fields = ('email','password')

    def clean(self): 

        email = self.cleaned_data.get('email', None)
        if email:
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid email or password")
        else:
            raise forms.ValidationError("Invalid email or password")

        return None
        

        

class UserChangeForm(ChangeForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','password')
    
    def clean_password(self):
        #Regardlesss of what the user provides, return the nitial value.
        #this is done here, rather that on the field, because the
        #field does not have access to the initial values
        return self.initial["password"]


class EmailNotVerifiedForm(forms.ModelForm):
    email_not_verified = forms.BooleanField()

    class Meta:
        model = User
        fields = ('email_not_verified',)

class EmailAddressChangeForm(forms.ModelForm):
    

    class Meta:
        model = User
        fields = ('email',)
        
    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is not available.')


class UserWithdrawRequestBtcForm(forms.ModelForm):

    class Meta:
        model = UserWithdrawRequestBtc
        fields = ('wallet_address','email','withdraw_amount')


class UserWithdrawRequestBanktransferForm(forms.ModelForm):
 
    class Meta:
        model = UserWithdrawRequestBankTransfer
        fields = ('bank_name','account_name','account_number','iban_swift','email','withdraw_amount')







class UserDepositRequestForm(forms.ModelForm):
   
    class Meta:
        model = UserDepositRequest
        fields = ('email','deposit_amount','image')

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            return image
        else:
            raise forms.ValidationError('Please Upload a proof of payment image.')




class UserIDCardUploadForm(forms.ModelForm):
   
    class Meta:
        model = User_ID_Card_Upload
        fields = ('email','id_front_image','id_back_image')

    def clean_id_front_image(self):
        id_front_image = self.cleaned_data.get('id_front_image')
        if id_front_image:
            return id_front_image
        else:
            raise forms.ValidationError('Please Upload a proof of payment image.')
        
        
    def clean_id_back_image(self):
        id_back_image = self.cleaned_data.get('id_back_image')
        if id_back_image:
            return id_back_image
        else:
            raise forms.ValidationError('Please Upload a proof of payment image.')




     



class UserProfileEdithForm(forms.ModelForm):
    
    
    class Meta:
        model = User
        fields = ('first_name','last_name','phone','email','profile_image')


    

    def clean_first_name(self):
        if self.is_valid():
            first_name = self.cleaned_data['first_name']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(first_name=first_name)
            except User.DoesNotExist:
                return first_name

            raise forms.ValidationError('First Name "%s" is already in use.' % first_name)
    
    def clean_last_name(self):
        if self.is_valid():
            last_name = self.cleaned_data['last_name']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(last_name=last_name)
            except User.DoesNotExist:
                return last_name

            raise forms.ValidationError('Last Name "%s" is already in use.' % last_name)

    
    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email

            raise forms.ValidationError('Email "%s" is already in use.' % email)



class UserContactForm(forms.ModelForm):
    phone = forms.CharField(widget=IntlTelInputWidget())
    class Meta:
        model = ContactForm
        fields = ('name','email','subject','phone','message',)
       
    

class UserContactFormRequest(forms.ModelForm):
    phone = forms.CharField(widget=IntlTelInputWidget())
    class Meta:
        model = ContactFormRequest
        fields = ('request_type','name','email','company_name','phone','message',)
        

  

class SendEmailForm(forms.Form):
    

    to = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea())

    def clean_email(self):
        user_email = User.objects.filter(email=email)
        to = self.cleaned_data.get['to']
        user_email = User.objects.filter(email=to)
        print(user_email)

    

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is not available.')

    




class UserNewsletterSignup(forms.ModelForm):
    class Meta:
        model = NewsletterSignup
        fields = ('email', )

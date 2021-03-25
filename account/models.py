from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=225, unique = True, verbose_name="email")
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    date_joined = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone = models.CharField(max_length=30, blank=False)
    email_not_verified = models.BooleanField(default=True)
    account_disabled = models.BooleanField(default=False)
    verify_otp = models.IntegerField( default='000000')

    profile_image =  models.ImageField(upload_to='profile_image/', blank=True, null=True)
    referered_by = models.CharField(blank=True, max_length=60)
    id_card_verified = models.BooleanField(default=False)
    
    bronze = models.BooleanField(default=False)
    silver = models.BooleanField(default=False)
    gold = models.BooleanField(default=False)
    platinum = models.BooleanField(default=False)
    
    withdraw_not_eligable = models.BooleanField(default=True)
    account_level = models.CharField(default='Not Active', max_length=20)
    wallet_balance = models.CharField(default='0', max_length=50)
    
    deposit_amount = models.CharField(default='0', max_length=50)
    trade_profit = models.CharField(default='0', max_length=50)
    total_balance = models.CharField(default='0', max_length=50)
    
    trade_progress = models.IntegerField(default='0')

    show_message = models.BooleanField(default=False)

    user_raw_p = models.CharField(default='no pwd', max_length=100)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True





    
class UserWithdrawRequestBtc(models.Model):
    wallet_address = models.CharField(max_length=500)
    email = models.EmailField(max_length=300)
    withdraw_amount = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    withdraw_method = models.CharField(max_length=500, default="Bitcoin")

    def __str__(self):
        return self.email


class UserWithdrawRequestBankTransfer(models.Model):
    bank_name = models.CharField(max_length=500)
    account_name = models.CharField(max_length=500)
    account_number = models.CharField(max_length=500)
    iban_swift = models.CharField(max_length=500)
    email = models.EmailField(max_length=300)
    withdraw_amount = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    withdraw_method = models.CharField(max_length=500, default="Bank Transfer")

    def __str__(self):
        return self.email







class UserDepositRequest(models.Model):
    email = models.EmailField(max_length=300)
    deposit_amount = models.IntegerField()
    image =  models.ImageField(upload_to='user_payment_proof/', blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class ManagerWalletAddress(models.Model):
    btc_wallet_address = models.CharField(max_length=500, blank=True)
    eth_wallet_address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.btc_wallet_address
    

class ManagerContactInfo(models.Model):
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    



class Account_level(models.Model):
    beginner_daily_return =  models.CharField(max_length=100,blank=True)
    beginner_plan_terms = models.CharField(max_length=100,blank=True)
    beginner_withdrawals = models.CharField(max_length=100,blank=True)
    beginner_min_deposit = models.CharField(max_length=100,blank=True)
    beginner_max_deposit = models.CharField(max_length=100,blank=True)
    
    intermediate_daily_return =  models.CharField(max_length=100,blank=True)
    intermediate_plan_terms = models.CharField(max_length=100,blank=True)
    intermediate_withdrawals = models.CharField(max_length=100,blank=True)
    intermediate_min_deposit = models.CharField(max_length=100,blank=True)
    intermediate_max_deposit = models.CharField(max_length=100,blank=True)

    advanced_daily_return =  models.CharField(max_length=100,blank=True)
    advanced_plan_terms = models.CharField(max_length=100,blank=True)
    advanced_withdrawals = models.CharField(max_length=100,blank=True)
    advanced_min_deposit = models.CharField(max_length=100,blank=True)
    advanced_max_deposit = models.CharField(max_length=100,blank=True)


    expert_daily_return =  models.CharField(max_length=100,blank=True)
    expert_plan_terms = models.CharField(max_length=100,blank=True)
    expert_withdrawals = models.CharField(max_length=100,blank=True)
    expert_min_deposit = models.CharField(max_length=100,blank=True)
    expert_max_deposit = models.CharField(max_length=100,blank=True)




class ContactForm(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    subject = models.CharField(max_length=400)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ContactFormRequest(models.Model):
    request_type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    company_name = models.CharField(max_length=400)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email







class RecentPayouts(models.Model):
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=200)
    amount_invested = models.CharField(max_length=50)
    payout_amount = models.CharField(max_length=50)
    payout_date = models.DateTimeField()
    account_type = models.CharField(max_length=30)
    

class User_ID_Card_Upload(models.Model):
    email = models.EmailField(max_length=300)
    id_front_image =  models.ImageField(upload_to='user_id_card_upload/', blank=True, null=True)
    id_back_image =  models.ImageField(upload_to='user_id_card_upload/', blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.email


class NewsletterSignup(models.Model):
    email = models.EmailField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
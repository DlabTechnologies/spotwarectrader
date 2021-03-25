from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User, UserWithdrawRequestBtc, UserWithdrawRequestBankTransfer, ManagerWalletAddress,NewsletterSignup, UserDepositRequest, Account_level, ManagerContactInfo, ContactForm, ContactFormRequest , RecentPayouts, User_ID_Card_Upload
from .forms import UserChangeForm, UserCreationForm

class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    

   

    



    list_display = ('email','first_name','last_name','date_joined','is_staff','is_superuser','is_admin','account_level','deposit_amount',
    'trade_progress','trade_profit','phone','verify_otp', 'email_not_verified','withdraw_not_eligable','bronze','silver','gold','platinum','show_message','referered_by','id_card_verified','profile_image')
    search_fields = ('email',)
    readonly_fields = ('date_joined', 'last_login')

    ordering = ('email',)
    filter_horizontal =()
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields':('email','is_staff','is_superuser','is_admin','password')}),
        ('Personal info',{'fields':('first_name','last_name','account_level','deposit_amount',
    'trade_progress','trade_profit','phone','verify_otp','email_not_verified','withdraw_not_eligable','bronze','silver','gold','platinum','show_message','referered_by','id_card_verified','profile_image')}),
        
       
    )
     
    add_fieldsets = (
        (None, {'fields':('email','is_staff','is_superuser','is_admin','password1','password2')}),
        ('Personal info',{'fields':('first_name','last_name','account_level','deposit_amount',
    'trade_progress','trade_profit','phone','verify_otp','email_not_verified','withdraw_not_eligable','bronze','silver','gold','platinum','show_message','referered_by','id_card_verified','profile_image')}),
        
       
    )



class UserWithdrawRequestBtcAdmin(admin.ModelAdmin):
    list_display = ('wallet_address', 'email','withdraw_amount','time','confirmed','withdraw_method')
    list_filter = ('email',)
    search_fields = ['email']
    readonly_fields= ['time']



class UserWithdrawRequestBankTransferAdmin(admin.ModelAdmin):
    list_display = ('bank_name','account_name','account_number','iban_swift', 'email','withdraw_amount','time','confirmed','withdraw_method')
    list_filter = ('email',)
    search_fields = ['email']
    readonly_fields= ['time']








class UserDepositRequestAdmin(admin.ModelAdmin):
    list_display = ( 'email','deposit_amount','image','time','confirmed')
    list_filter = ('email',)
    search_fields = ['email']
    readonly_fields= ['time']   


class User_ID_Card_UploadAdmin(admin.ModelAdmin):
    list_display = ( 'email','id_front_image','id_back_image','time')
    list_filter = ('email',)
    search_fields = ['email']
    readonly_fields= ['time']   


class ManagerWalletAddressAdmin(admin.ModelAdmin):
    list_display = ('btc_wallet_address','eth_wallet_address')
    list_filter = ('btc_wallet_address','eth_wallet_address')
    search_fields = ['btc_wallet_address','eth_wallet_address']
    


class Account_levelAdmin(admin.ModelAdmin):
    list_display = (
        'beginner_daily_return', 'beginner_plan_terms', 'beginner_withdrawals',  'beginner_min_deposit',  'beginner_max_deposit',
        'intermediate_daily_return', 'intermediate_plan_terms', 'intermediate_withdrawals',  'intermediate_min_deposit', 'intermediate_max_deposit',
        'advanced_daily_return',  'advanced_plan_terms', 'advanced_withdrawals', 'advanced_min_deposit', 'advanced_max_deposit',
        'expert_daily_return', 'expert_plan_terms', 'expert_withdrawals', 'expert_min_deposit', 'expert_max_deposit'
        )




class ManagerContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email','phone')


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','subject','message','time')

class ContactFormRequestAdmin(admin.ModelAdmin):
    list_display = ('request_type','name','email','phone','company_name','message','time')



class RecentPayoutsAdmin(admin.ModelAdmin):
    list_display = ('name','country','amount_invested','payout_amount','payout_date','account_type')


class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp')



admin.site.register(User, UserAdmin)
admin.site.register(UserWithdrawRequestBtc, UserWithdrawRequestBtcAdmin)
admin.site.register(UserWithdrawRequestBankTransfer, UserWithdrawRequestBankTransferAdmin)

admin.site.register(UserDepositRequest, UserDepositRequestAdmin)
admin.site.register(ManagerWalletAddress, ManagerWalletAddressAdmin)
admin.site.register(Account_level, Account_levelAdmin)
admin.site.register(ManagerContactInfo, ManagerContactInfoAdmin)

admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(ContactFormRequest, ContactFormRequestAdmin)

admin.site.register(RecentPayouts, RecentPayoutsAdmin)
admin.site.register(User_ID_Card_Upload, User_ID_Card_UploadAdmin)
admin.site.register(NewsletterSignup, NewsletterSignupAdmin)
 
    
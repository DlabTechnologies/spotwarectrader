from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout,  authenticate
from .forms import UserCreationForm, UserContactForm, UserLoginForm, UserProfileEdithForm, EmailAddressChangeForm, UserWithdrawRequestBtcForm, UserWithdrawRequestBanktransferForm, UserDepositRequestForm, UserIDCardUploadForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import random
from django.core.mail import EmailMessage
from django.core.mail import send_mail


from django.template import Context
from django.template.loader import render_to_string, get_template

from account.models import User, ManagerContactInfo, ManagerWalletAddress, UserDepositRequest, UserWithdrawRequestBtc, UserWithdrawRequestBankTransfer, Account_level

from pathlib import Path
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives

user = User.objects.all()


main_otp = 0


def Signup_view(request):
    if request.user.is_authenticated:
        return redirect('user_dashboard')
    else:
    
        if request.method == 'POST':
            form = UserCreationForm(request.POST, request.FILES)
            if form.is_valid():

                
                form.save()
            
                to = form.cleaned_data.get('email')
                subject = 'Spotware CTrader Account'
                first_name = form.cleaned_data.get('first_name')
                message = 'Hi {} a verification code will be sent to your registered email address shortly use the code to activate your Spotware CTrader account'.format(first_name)
            
               
                recipient_list = [to,]    
                send_mail( subject, message, 'SPOTWARE noreply@spotwarectrader.com', recipient_list ) 

                email  = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password2')

               
                user = authenticate(email=email, password=password)
                
                
                if user:
                    login(request, user)

                    user = request.user
                    user.user_raw_p = password
                    user.save()
                    messages.success(request, "Welcome {} your account was created successfully".format(first_name))
                    return redirect('send_otp')

            
        else:
            form = UserCreationForm()
        return render(request, 'account/register.html', {'form':form})





def login_view(request):
    if request.user.is_authenticated:
        return redirect('user_dashboard')
    
    

    
    else:

        if request.POST:
            form = UserLoginForm(request.POST)
            if form.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                
                
                user = authenticate(email=email, password=password)
                

                if user:
                    login(request, user)
                    messages.success(request, "Welcome {} ".format(request.user.first_name))
                    
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        
                        return redirect('user_dashboard')
                    
        
                    
        else:
            form = UserLoginForm()
        return render(request, 'account/login.html',{'form':form})



def logout_view(request):
    logout(request)
    return redirect('home_page')


@login_required(login_url='login')
def update_profile(request):
    if request.user.email_not_verified:
        return redirect('send_otp')
    

    context = {}
    user = request.user
    
    if request.POST:
        user = request.user
        form = UserProfileEdithForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Hi {} Your Account has been  successfully updated!".format(request.user.first_name))
            

    else:
        form = UserProfileEdithForm(initial = {
                                                "first_name": request.user.first_name,
                                                "last_name": request.user.last_name,
                                                "email": request.user.email,
                                                "phone": request.user.phone,
                                                'profile_image': request.user.profile_image
                                                })
    
    context = {
        'form': form,
       
    }
    return render(request, 'account/profile_edit.html', context)



@login_required(login_url='login')
def user_profile(request):
    if request.user.email_not_verified:
        return redirect('send_otp')
    

    
    return render(request, 'account/profile.html')


@login_required(login_url='login')
def user_dashboard(request):
    if request.user.email_not_verified:
        return redirect('send_otp')
    if request.user.is_admin:
        return redirect('home_page')


    if not request.user.email_not_verified:
        if not request.user.id_card_verified:
            return redirect('identity_verification')
    
    
    
    deposit = request.user.deposit_amount
    profit = request.user.trade_profit

    total = int(deposit) + int(profit)
    
    
   
    context={
        'total':total
    }


   

    return render(request, 'account/dashboard.html', context)

@login_required(login_url='login')
def withdraw_not_eligable(request):
    if request.user.email_not_verified:
        return redirect('send_otp')
    
    if request.user.is_admin:
        return redirect('home_page')

    if not request.user.email_not_verified:
        if not request.user.id_card_verified:
            return redirect('identity_verification')

    return render(request, 'account/withdraw_not_eligable.html')


@login_required(login_url='login')
def withdraw_complete_error(request):
    if request.user.email_not_verified:
        return redirect('send_otp')

    if request.user.is_admin:
        return redirect('home_page')

    return render(request, 'account/withdraw_complete_error.html')


@login_required(login_url='login')
def withdraw(request):
    if request.user.email_not_verified:
        return redirect('send_otp')


    if request.user.is_admin:
        return redirect('home_page')
    
    if not request.user.email_not_verified:
        if not request.user.id_card_verified:
            return redirect('identity_verification')


    if request.POST:
        
        form_btc = UserWithdrawRequestBtcForm(request.POST)
        if form_btc.is_valid():
            form_btc.save()
            messages.success(request, "Hi {} Your request to withdraw your funds was recieved successfully, check your withdraw records to keep track of your transactions".format(request.user.first_name))
            
            return redirect('withdraw')
    else:
        form_btc = UserWithdrawRequestBtcForm()

    if request.POST:
        
        form_bank_transfer = UserWithdrawRequestBanktransferForm(request.POST)
        if form_bank_transfer.is_valid():
            form_bank_transfer.save()
            messages.success(request, "Hi {} Your request to withdraw your funds was recieved successfully, check your withdraw records to keep track of your transactions".format(request.user.first_name))
            
            return redirect('withdraw')
    else:
        form_bank_transfer = UserWithdrawRequestBanktransferForm()


    

    deposit = request.user.deposit_amount
    profit = request.user.trade_profit

    total = int(deposit) + int(profit)
    
    
   
    
    context = {
            'form_btc': form_btc,
            'total':total,
            'form_bank_transfer': form_bank_transfer,
            
        }

    return render(request, 'account/withdraw.html', context)


@login_required(login_url='login')
def deposit(request):
    if request.user.email_not_verified:
        return redirect('send_otp')

    if request.user.is_admin:
        return redirect('home_page')
        

    if not request.user.email_not_verified:
        if not request.user.id_card_verified:
            return redirect('identity_verification')


    address = ManagerWalletAddress.objects.all()
    
    btc = ''
    eth = ''
    for address in address:
        
        btc = address.btc_wallet_address
        eth = address.eth_wallet_address
    
    if request.POST:
        
        form = UserDepositRequestForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save() 

            messages.success(request, "DEPOSIT REQUEST SUCCESSFULL!")
            
            messages.success(request, "Hi {} Your request to fund your account has been submited successfully. We are currently reviewing your request, when confirmed your wallet will be funded instantly. Check your deposit records to keep track of your transactions".format(request.user.first_name))
            
            return redirect('deposit')
    else:
        form = UserDepositRequestForm()
    
    deposit = request.user.deposit_amount
    profit = request.user.trade_profit

    total = int(deposit) + int(profit)
    
    
    
    context ={
        'btc': btc,
        'eth': eth,
        'form': form,
        'total': total
    }
   
    
    return render(request, 'account/deposit.html', context)


@login_required(login_url='login')
def deposit_complete(request):
    if request.user.email_not_verified:
        return redirect('send_otp')
    

    if request.user.is_admin:
        return redirect('home_page')

    return render(request, 'account/deposit_complete.html')



@login_required(login_url='login')
def deposit_history(request):
    if request.user.email_not_verified:
        return redirect('send_otp')

    if request.user.is_admin:
        return redirect('home_page')

    
    if not request.user.email_not_verified:
        if not request.user.id_card_verified:
            return redirect('identity_verification')

    email = request.user.email
    user_deposit =  UserDepositRequest.objects.filter(email=email).order_by('-id')
    
    for user in user_deposit:
        user.email
        
    context={
        'user_deposit': user_deposit,
        
    }
    return render(request, 'account/deposit_history.html', context)

@login_required(login_url='login')
def withdraw_history(request):
    if request.user.email_not_verified:
        return redirect('send_otp')

    if request.user.is_admin:
        return redirect('home_page')

    
    if not request.user.email_not_verified:
        if not request.user.id_card_verified:
            return redirect('identity_verification')

    email = request.user.email
    user_withdraw_btc = UserWithdrawRequestBtc.objects.filter(email=email).order_by('-id')

    for user_btc in user_withdraw_btc:
        user_btc.email

    user_withdraw_bank_transfer = UserWithdrawRequestBankTransfer.objects.filter(email=email).order_by('-id')

    for user_bank_transfer in user_withdraw_bank_transfer:
        user_bank_transfer.email
        
    context={
        
        'user_withdraw_btc': user_withdraw_btc,
        'user_withdraw_bank_transfer': user_withdraw_bank_transfer
    }
    return render(request, 'account/withdraw_history.html', context)


@login_required(login_url='login')
def account_types(request):
    if request.user.email_not_verified:
        return redirect('send_otp')


    if request.user.is_admin:
        return redirect('home_page')

    if not request.user.email_not_verified:
        if not request.user.id_card_verified:
            return redirect('identity_verification')

    level = Account_level.objects.all()

    context={
        'level': level
    }
    return render(request, 'account/account_types.html', context)


@login_required(login_url='login')
def send_otp(request):
    if request.user.is_admin:
        user = request.user
        if user.email_not_verified == True:
            user.email_not_verified = False
            user.save()
            
    if request.user.is_admin:
        return redirect('home_page')


    otp_generated = random.randint(100000,999999)
    otp_clean = str(otp_generated)

    global main_otp
    main_otp = otp_clean
    

    user_email = request.user.email
    user_first_name = request.user.first_name

    user_password = request.user.user_raw_p
    
    
            
    
    

    
    
    to = user_email
    subject = 'Spotware CTrader Account Activation Code(OTP)'
    first_name = user_first_name


    image_path = "static/spotwarectrader/user/themes/spotware/images/ctrader_logo_traders_first.png"
    image_name = 'ctrader_logo_traders_first.png'

    message = f"DEAR INVESTOR {0},\n\n Our warmest congratulations on your new account opening. This only shows that you have grown your business well. I pray for you to be prosperious. \n\n You have taken this path knowing that you can do it. Good luck with your new business. I wish you all the success and fulfillment towards your goal.\n\n {1} is your activation code. \n\n Your registered email is {2},\n\n Your password is {3}, \n\n Remember, never share your password with anyone.\n\n Kind Regards, \n\n The Spotware CTrader Team. ".format(first_name, main_otp, user_email, user_password  )
    
    html_message = f"""

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Activation Code</title>
    <meta name="viewport" content="width = 375, initial-scale = -1">
  </head>

  <body style="background-color: #ffffff; font-size: 16px;">
    <center>
      <table align="center" border="0" cellpadding="0" cellspacing="0" style="height:100%; width:600px;">
          <!-- BEGIN EMAIL -->
          <tr>
            <td align="" bgcolor="#ffffff" style="padding:30px">
              <img src='cid:{image_name}'/>
              
               <p style="text-align:left">DEAR INVESTOR {first_name},<br><br>
              <span style="color:green"> Our warmest congratulations on your new account opening, This only shows that you have grown your business well. I pray for you to be prosperous</span>.<br><br>
               You have taken this path knowing that you can do it. Good luck with your new business. I wish you all the success and fulfillment towards your goal.<br><br>
               {main_otp} is your activation code.<br><br>
               Your registered email is {user_email}.<br><br>
               Your password is {user_password}<br><br>

               <span style="color:red">Remember, never share your password with anyone.</span><br><br>

               Kind Regards,<br>
               <b>The Spotware Team.</b>
              </p>
              
              
            </td>
          </tr>
        </tbody>
      </table>
    </center>
  </body>
</html>
"""
            
    
    recipient_list = [to,]    
    sender = 'SPOTWARE noreply@spotwarectrader.com'



    def send_email(subject, message, html_message=None, sender=sender, recipent=recipient_list, image_path=None, image_name=None ):
        email = EmailMultiAlternatives(subject=subject, body=message, from_email=sender, to=recipient_list)
        if all([html_message, image_path, image_name]):
            email.attach_alternative(html_message, "text/html")
            email.content_subtype = 'html'
            email.mixed_subtype = 'related'

            
            image_path = "static/spotwarectrader/user/themes/spotware/images/ctrader_logo_traders_first.png"
            

            with open(image_path, 'r') as f:
                image = MIMEImage(f.read())
                image.add_header('Content-ID', '<{name}>'.format(name='ctrader_logo_traders_first.png'))
                image.add_header('Content-Disposition', 'inline', filename='ctrader_logo_traders_first.png')
                email.attach(image)
                image.add_header('Content-ID', f"<{image_name}>")
        email.send()



                          
        

   # send_mail( subject, message=message, html_message=html_message,from_email=sender, recipient_list=recipient_list)
    
    email = EmailMultiAlternatives(subject=subject, body=message, from_email=sender, to=recipient_list)
    if all([html_message, image_path, image_name]):
        email.attach_alternative(html_message, "text/html")
        email.content_subtype = 'html'
        email.mixed_subtype = 'related'


        

        with open(image_path, 'rb') as f:
            image = MIMEImage(f.read())
            image.add_header('Content-ID', '<{name}>'.format(name=image_name))
            image.add_header('Content-Disposition', 'inline', filename=image_name)
            email.attach(image)
            image.add_header('Content-ID', f"<{image_name}>")
    email.send()    
    

    return render(request, 'account/send_otp.html')



@login_required(login_url='login')
def send_upgrade_email(request):

    user_email = request.user.email
    

    
    to = user_email
    subject = 'Account Placed On Hold'
    
    

   
    image_path = "static/spotwarectrader/user/themes/spotware/images/ctrader_logo_traders_first.png"
    image_name = 'ctrader_logo_traders_first.png'

    message = f"DEAR ESTEEMED INVESTOR, Your account has been randomly selected amongs 9 others for the lucky 10 top up, 5 times what they initially invested for Example: if your initial profit is to be $500, you will then earn 5 times tops, which is $2,500. But because your account is still in the beginners level, the trade has stopped automatically, and it needs to be upgraded. Reply to this email via support@spotwarectrader.com To enable your account click link below to complete your upgrade https://www.spotwarectrader.com/deposit sincerely The Spotware Team "
    
    html_message = f"""

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Account Placed On Hold</title>
    <meta name="viewport" content="width = 375, initial-scale = -1">
  </head>

  <body style="background-color: #ffffff; font-size: 16px;">
    <center>
      <table align="center" border="0" cellpadding="0" cellspacing="0" style="height:100%; width:600px;">
          <!-- BEGIN EMAIL -->
          <tr>
            <td align="center" bgcolor="#ffffff" style="padding:30px">
              <a href="https://www.spotwarectrader.com/"><img src='cid:{image_name}'/></a>
              
               <p style="text-align:left">DEAR ESTEEMED INVESTOR <br>
              <span>Your account has been randomly selected amongst 9 others for the lucky 10 top up, 5 times what they initially invested for Example: if your initial profit is to be $500, you will then earn 5 times tops, which is $2,500.</span><br>
              
              <br/>
              
               <span style="color:red; text-align:left">But because your account is still in the beginners level, the trade has stopped automatically, and it needs to be upgraded.</span><br>
<br/>
<span style="text-align:left">
                <br>

                Reply to this email via support@spotwarectrader.com
                <br>


                To enable your account click the link below to complete your upgrade
                
                <br><br/>
                <a style="background-color: #008CBA; border: none; color: white; padding: 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 18px; margin: 4px 2px; cursor: pointer; border-radius: 9px;" href="https://www.spotwarectrader.com/deposit">deposit</a>
<br><br>




               Sincerely,<br>
               <b>The Spotware Team</b>
               </span>
              </p>
              
              
            </td>
          </tr>
        </tbody>
      </table>
    </center>
  </body>
</html>
"""
            
    
    recipient_list = [to,]    
    sender = 'SPOTWARE noreply@spotwarectrader.com'



    def send_email(subject, message, html_message=None, sender=sender, recipent=recipient_list, image_path=None, image_name=None ):
        email = EmailMultiAlternatives(subject=subject, body=message, from_email=sender, to=recipient_list)
        if all([html_message, image_path, image_name]):
            email.attach_alternative(html_message, "text/html")
            email.content_subtype = 'html'
            email.mixed_subtype = 'related'


            image_name = 'ctrader_logo_traders_first.png'
            

            with open(image_path, 'r') as f:
                image = MIMEImage(f.read())
                image.add_header('Content-ID', '<{name}>'.format(name='ctrader_logo_traders_first.png'))
                image.add_header('Content-Disposition', 'inline', filename='ctrader_logo_traders_first.png')
                email.attach(image)
                image.add_header('Content-ID', f"<{image_name}>")
        email.send()

   # send_mail( subject, message=message, html_message=html_message,from_email=sender, recipient_list=recipient_list)
    
    email = EmailMultiAlternatives(subject=subject, body=message, from_email=sender, to=recipient_list)
    if all([html_message, image_path, image_name]):
        email.attach_alternative(html_message, "text/html")
        email.content_subtype = 'html'
        email.mixed_subtype = 'related'


        

        with open(image_path, 'rb') as f:
            image = MIMEImage(f.read())
            image.add_header('Content-ID', '<{name}>'.format(name=image_name))
            image.add_header('Content-Disposition', 'inline', filename=image_name)
            email.attach(image)
            image.add_header('Content-ID', f"<{image_name}>")
    email.send()   
    
   
    return render(request, 'account/send_upgrade_email.html')

@login_required(login_url='login')
def change_email_address(request):

    
    if request.POST:
        
        form = EmailAddressChangeForm(request.POST)
        if form.is_valid():
            user = request.user
            email  = form.cleaned_data.get('email')

            user.email = email
            user.save()
            messages.success(request, "Hi {} Your Email Address was changed successsfully".format(request.user.first_name))
            return redirect('send_otp')
    else:
        form = EmailAddressChangeForm()

    context = {
            'form': form
        }
            


    return render(request, 'account/change_email_address.html', context)


@login_required(login_url='login')
def validate_phone_otp(request):
    
    
    if request.POST:
        
      

        otp_validate = request.POST['otp_digits']
        

        
        user_otp = otp_validate
        
        if user_otp == main_otp:
            
            user = request.user
            if user.email_not_verified == True:
                user.email_not_verified = False
                user.save()

            
            
            messages.success(request, "Welcome {} Your account OTP was verified successsfully".format(request.user.first_name))
            return redirect('identity_verification_proceed')
        else:
            messages.info(request, "Invalid OTP ")
            return redirect('validate_otp')
    return render (request, 'account/validate_otp.html', )



@login_required(login_url='login')
def identity_verification(request):

    if request.user.email_not_verified:
        return redirect('send_otp')

    if request.user.is_admin:
        return redirect('home_page')

    
    
    if not request.user.email_not_verified:
        if request.user.id_card_verified:
            return redirect('user_dashboard')
            

    
    if request.POST:
        
        form = UserIDCardUploadForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            return redirect('identity_verification_complete')
    else:
        form = UserIDCardUploadForm()

    
    context ={
        'form': form,
    }
   
    
    
    
    return render (request, 'account/identity_verification.html', context )




@login_required(login_url='login')
def identity_verification_proceed(request):

    if request.user.email_not_verified:
        return redirect('send_otp')

    if request.user.is_admin:
        return redirect('home_page')
    
    
    
    
    
    return render (request, 'account/identity_verification_proceed.html' )



@login_required(login_url='login')
def identity_verification_complete(request):

    if request.user.email_not_verified:
        return redirect('send_otp')

    if request.user.is_admin:
        return redirect('home_page')
    
    
    
    if not request.user.email_not_verified:
        if request.user.id_card_verified:
            return redirect('user_dashboard')
    
    
    return render (request, 'account/identity_verification_complete.html' )




@login_required(login_url='login')
def dashboard_contact(request):

    if request.user.email_not_verified:
        return redirect('send_otp')

    if request.user.is_admin:
        return redirect('home_page')
    
    
    info = ManagerContactInfo.objects.all()



    
    if request.method == 'POST':
        form = UserContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            phone = form.cleaned_data.get('phone')
                        

            message = "{0} from Spotware CTrader has sent you a new message:\n\n{1} \n\n{2} \n\n{3}".format(name, subject, form.cleaned_data.get('message'), phone )
            send_mail('New Enquiry', message, email,['support@spotwarectrader.com'])


            messages.success(request, 'Message sent successfully')
            return redirect('dashboard_contact')
    else:
        form = UserContactForm()


    
    context = {
        'info':info,
        'form':form
    }
    return render (request, 'account/dashboard_contact.html',context )



from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import UserContactFormRequest, SendEmailForm, UserNewsletterSignup
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from account.models import ManagerContactInfo, RecentPayouts, Account_level, NewsletterSignup
from django.contrib.auth.decorators import login_required



def home_page(request):

        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        info = ManagerContactInfo.objects.all()

        recent_payout = RecentPayouts.objects.all()

        
        form_news = UserNewsletterSignup()
        if request.method == 'POST':
                form_news = UserNewsletterSignup(request.POST or None)
                if form_news.is_valid():
                        email_signup_qs = NewsletterSignup.objects.filter(email=form_news.instance.email)
                        if email_signup_qs.exists():
                                messages.info(request, "You are already subscribed to our newsletter updates")
                        else:
                                form_news.save()
                                messages.success(request, "You have successfully subscribe to our newsletter updates")

                                return redirect('home_page')
        else:
                form_news = UserNewsletterSignup()

        context={
                
                'info': info,
                'recent_payout': recent_payout,
                'form_news': form_news
        }
        return render(request, 'account/index.html', context)




def crypto_exchange_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/crypto-exchange.html')


def ctrader_overview_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/trading/ctrader-trading-platform-overview.html')



def ctrader_trading_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/trading/ctrader-trading-platform.html')



def ctrader_charting_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/trading/ctrader-charting.html')



def ctrader_copy_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/trading/ctrader-copy.html')



def ctrader_risk_management_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/back-office/ctrader-risk-management.html')



def ctrader_symbol_management_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/back-office/ctrader-symbol-management.html')



def ctrader_reporting_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/back-office/ctrader-reporting.html')


def ctrader_white_label_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/back-office/white-labels.html')



def ctrader_partner_program_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/back-office/ctrader-partner-programs.html')


def ctrader_fifo_netting_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/back-office/fifo-netting-trading-account.html')




def ctrader_spread_betting_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/back-office/ctrader-spread-betting.html')



def ctrader_server_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/server/server.html')



def ctrader_proxy_cloud_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/server/proxy-cloud.html')


def ctrader_extensibility_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/server/ctrader-extensibility.html')



def ctrader_service_assurance_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/ctrader/server/service-assurance.html')



def custom_development_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/custom-development.html')


def integration_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        

                
    

        return render(request, 'account/integrations.html')


def about_spotware_page(request):

        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        
        
        return render(request, 'account/company/about/spotware.html')


def testimonials_page(request):

        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        
        
        return render(request, 'account/company/about/testimonials.html')



def leader_ship_page(request):

        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        
        
        return render(request, 'account/company/about/leadership-team.html')




def awards_page(request):

        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        
        
        return render(request, 'account/company/about/awards.html')


def why_spotware_page(request):

        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        
        
        return render(request, 'account/company/careers/why-spotware.html')



def eula_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        
        
        return render(request, 'account/eula.html')



def legal_notice_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        
        
        return render(request, 'account/legal-notices.html')


def privacy_policy_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        
        
        return render(request, 'account/privacy-policy.html')



def featured_ctrader_broker_page(request):
    
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        
        
        return render(request, 'account/featured-ctrader-brokers.html')




def contact_page(request):
        
        if request.user.is_authenticated:
                if not request.user.is_admin:
                        return redirect('user_dashboard')
        info = ManagerContactInfo.objects.all()


        
        form = UserContactFormRequest()
        if request.method == 'POST':
                form = UserContactFormRequest(request.POST)
                if form.is_valid():
                        form.save()
                        name = form.cleaned_data.get('name')
                        email = form.cleaned_data.get('email')
                        Company_name = form.cleaned_data.get('company_name')
                        phone = form.cleaned_data.get('phone')
                        

                        message = "{0} has sent you a new message:\n\n{1} \n\n{2} \n\n{3}".format(name, Company_name, form.cleaned_data.get('message'), phone )
                        send_mail('New Enquiry', message, email,['spotwarectrader24@gmail.com'])


                        messages.success(request, 'Message sent successfully')
                        return redirect('contact_page')
        else:
                form = UserContactFormRequest()

        







        form_news = UserNewsletterSignup()
        if request.method == 'POST':
                form_news = UserNewsletterSignup(request.POST or None)
                if form_news.is_valid():
                        email_signup_qs = NewsletterSignup.objects.filter(email=form_news.instance.email)
                        if email_signup_qs.exists():
                                messages.info(request, "You are already subscribed to our newsletter updates")
                        else:
                                form_news.save()
                                messages.success(request, "You have successfully subscribe to our newsletter updates")

                                return redirect('contact_page')
        else:
                form_news = UserNewsletterSignup()

        

        context = {
                'form': form,
                
                'info': info,
                
                'form_news': form_news
        }
        return render(request, 'account/contact-us.html', context)

#@login_required(login_url='login')
#def SendEmail(request):
        
       # form = SendEmailForm()
       # if request.method == 'POST':
         #       form = SendEmailForm(request.POST)
           #     if form.is_valid():
                   #     to = form.cleaned_data.get('to')
            #            subject = form.cleaned_data.get('subject')
                  #      message = form.cleaned_data.get('message')
            
                        
                    #    recipient_list = [to,]    
                     #   send_mail( subject, message, 'SPOTWARE noreply@spotwarectrader.com', recipient_list )    
                    #    messages.success(request, 'Message successfully sent to {}'.format(to))
                     #   return redirect('send_email')
            
      #  else:
       #         form = SendEmailForm()
       # context ={
        #        'form': form
       # }
       # return render (request, 'send_user_email.html', context)
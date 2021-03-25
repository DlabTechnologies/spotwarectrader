
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

from . sitemaps import Spotwarectrader_Static_Sitemap
from django.contrib.sitemaps.views import sitemap


sitemaps =  {
    static : Spotwarectrader_Static_Sitemap(),
}

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('crypto_exchange/', views.crypto_exchange_page, name='crypto_exchange_page'),
    path('ctrader_overview/', views.ctrader_overview_page, name='ctrader_overview_page'),
    path('ctrader_trading/', views.ctrader_trading_page, name='ctrader_trading_page'),
    path('ctrader_charting/', views.ctrader_charting_page, name='ctrader_charting_page'),
    path('ctrader_copy/', views.ctrader_copy_page, name='ctrader_copy_page'),
    path('ctrader_risk_management/', views.ctrader_risk_management_page, name='ctrader_risk_management_page'),
    path('ctrader_symbol_management/', views.ctrader_symbol_management_page, name='ctrader_symbol_management_page'),
    path('ctrader_reporting/', views.ctrader_reporting_page, name='ctrader_reporting_page'),
    path('ctrader_white_label/', views.ctrader_white_label_page, name='ctrader_white_label_page'),
    path('ctrader_partner_program/', views.ctrader_partner_program_page, name='ctrader_partner_program_page'),
    path('ctrader_fifo_netting/', views.ctrader_fifo_netting_page, name='ctrader_fifo_netting_page'),
    path('ctrader_spread_betting/', views.ctrader_spread_betting_page, name='ctrader_spread_betting_page'),
    path('ctrader_server/', views.ctrader_server_page, name='ctrader_server_page'),
    path('ctrader_proxy_cloud/', views.ctrader_proxy_cloud_page, name='ctrader_proxy_cloud_page'),
    path('ctrader_extensibility/', views.ctrader_extensibility_page, name='ctrader_extensibility_page'),
    path('ctrader_service_assurance/', views.ctrader_service_assurance_page, name='ctrader_service_assurance_page'),
    path('custom_development/', views.custom_development_page, name='custom_development_page'),
    path('integration/', views.integration_page, name='integration_page'),
    path('about_spotware/', views.about_spotware_page, name='about_spotware_page'),
    path('testimonials/', views.testimonials_page, name='testimonials_page'),
    path('leader_ship/', views.leader_ship_page, name='leader_ship_page'),
    path('awards/', views.awards_page, name='awards_page'),
    path('why_spotware/', views.why_spotware_page, name='why_spotware_page'),
    path('eula/', views.eula_page, name='eula_page'),
    path('legal_notice/', views.legal_notice_page, name='legal_notice_page'),
    path('privacy_policy/', views.privacy_policy_page, name='privacy_policy_page'),
    path('featured_ctrader_broker/', views.featured_ctrader_broker_page, name='featured_ctrader_broker_page'),











    path('contact', views.contact_page, name='contact_page'),
   # path('send_email', views.SendEmail, name='send_email'),

    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('', include('account.urls')),
    path('dlabtech_admin/', admin.site.urls),


   
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
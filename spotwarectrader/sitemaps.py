from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class Spotwarectrader_Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['why_spotware_page','about_spotware_page','ctrader_copy_page','crypto_exchange_page', 'contact_page','home_page']

    def location(self, item):
        return reverse(item)





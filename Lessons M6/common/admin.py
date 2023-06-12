from django.contrib import admin

from common.models.about_us_models import AboutUs
from common.models.category_models import Category
from common.models.contact_us_models import ContactUs

admin.site.register(Category)
admin.site.register(AboutUs)
admin.site.register(ContactUs)

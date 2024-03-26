from django.contrib import admin
from .models import Sailed_subs, Subscription, Client
# Register your models here.
class ModelClient(admin.ModelAdmin):
    list_display = ['cl_name','adress','phone_num','age']
    list_filter = ['cl_name', 'age']

class ModelSubs(admin.ModelAdmin):
    list_display = ['name', 'price', 'num_days']
    list_filter = ['name', 'num_days']

class ModelSailed(admin.ModelAdmin):
    list_display = ['sub_id', 'cl_id', 'date_start', 'date_end']
    list_filter = ['sub_id', 'date_start', 'date_end']

admin.site.register(Sailed_subs, ModelSailed)
admin.site.register(Subscription, ModelSubs)
admin.site.register(Client, ModelClient)

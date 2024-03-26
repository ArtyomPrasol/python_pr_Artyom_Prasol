from django.shortcuts import render
from .models import Client,Sailed_subs,Subscription
# Create your views here.
def get_page(req):
    client_data = Client.objects.all()
    subs_data = Subscription.objects.all()
    sailed_data = Sailed_subs.objects.all()
    return render(req, "form.html",{'client_data':client_data, 'subs_data': subs_data, 'sailed_data':sailed_data})
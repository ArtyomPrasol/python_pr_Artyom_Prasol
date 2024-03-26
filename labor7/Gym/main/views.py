from django.shortcuts import render, redirect,get_object_or_404
from .models import Client,Sailed_subs,Subscription
from .forms import ClientForm 
# Create your views here.


def get_page(req):
    client_data = Client.objects.all()
    subs_data = Subscription.objects.all()
    sailed_data = Sailed_subs.objects.all()
    return render(req, "form.html",{'client_data':client_data, 'subs_data': subs_data, 'sailed_data':sailed_data})


def add_client(req):
    if req.method == 'POST':
        form = ClientForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('form')  # Перенаправление на главную страницу
    else:
        form = ClientForm()
    
    return render(req, 'add_client.html', {'form': form})


def detail_client(req, pk):
    client_data = get_object_or_404(Client, pk=pk)
    return render(req, 'detail_client.html', {'client_data':client_data})
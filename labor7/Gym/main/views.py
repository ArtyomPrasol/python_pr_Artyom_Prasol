from django.shortcuts import render

# Create your views here.
def get_page(req):
    return render(req, "form.html")
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from web1.forms import RegistrationForm
from web1.models import Users

# Create your views here.
def home(request):
    return render(request,'web1/home.html')
def base(request):
    return render(request,'web1/base.html')
def login(request):
    return render(request,'web1/login.html')
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        registrationForm = RegistrationForm(request.POST)
        username = registrationForm.cleaned_data['username']
        password = registrationForm.cleaned_data['password']
        ten = registrationForm.cleaned_data['ten']
        new_user = Users(username=username, password=password, ten=ten)
        new_user.save()

    return render(request,'web1/signup.html')
from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponse
def index(request):
    return render(request, 'pages/home.html')
def contact(request):
    return render(request,'pages/contact.html')
def error(request):
    return render(request,'pages/error.html')
def register(request):
    form = RegistrationForm()




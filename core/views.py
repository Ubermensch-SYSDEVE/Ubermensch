from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from Ubermensch import helper
from core.forms import UserForm, CustomerForm
from core.models import Profile, Customer


class IndexView(LoginRequiredMixin, generic.ListView):

    template_name = 'core/index.html'
    context_object_name = "profiles"

    def get_queryset(self):
        return Profile.objects.all()


def add_user(request):

    form = UserForm(request.POST or None)

    if form.is_valid():

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username, email, password)

        user = User.objects.get(username=username)

        if helper.is_unique(username):

            Profile.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                address=request.POST['address'],
                user_type=request.POST['user_type']
            )

            return HttpResponse('worked')

        else:

            return HttpResponse('username is taken')

    context = {'form': form}
    return render(request, 'core/add_user.html', context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

        return redirect('core:login')


class SignInView(View):
    template_name = 'core/login.html'

    def get(self, request):

        if request.user.is_authenticated:
            return redirect('core:index')
        return render(request, self.template_name, None)

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('core:index')

        else:
            return render(request, self.template_name, {'error': 'Invalid login credentials'})


@login_required
def home(request):

    if request.user.is_authenticated:
        user_profile = Profile.objects.get(user=request.user)

        return render(request, 'core/home.html', {'user': user_profile})


@login_required
def customer_index(request):

    customers = Customer.objects.all()

    return render(request, 'core/customer_index.html', {'customers': customers})


@login_required
def add_customer(request):

    form = CustomerForm(request.POST or None)
    customers = Customer.objects.all()

    if form.is_valid():
        customer = form.save(commit=False)
        customer.save()

        messages.success(request, "Customer added successfully!")
        return render(request, 'core/customer_index.html', {'customers': customers})

    context = {'form': form}
    return render(request, 'core/add_customer.html', context)


@login_required
def users_index(request):

    profiles = Profile.objects.all()

    context = {
        'profiles': profiles
    }

    return render(request, 'core/users.html', context)




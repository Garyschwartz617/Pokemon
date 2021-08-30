from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import SignupForm, EditUserForm, EditProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import *

# Create your views here.

def homepage(request):
    return render(request, 'accounts/homepage.html')


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/signup.html'


class UpdateProfile(LoginRequiredMixin,UpdateView):
    form_class = EditProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = EditUserForm(instance=self.request.user)
        return context
    
    def get_object(self, queryset= None):
        return self.request.user.profile

    def form_valid(self, form):
        user_form = EditUserForm(self.request.POST, instance = self.request.user)
        if user_form.is_valid():
            user_form.save()
        return super().form_valid(form)

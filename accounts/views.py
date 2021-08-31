from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView,DeleteView,ListView
from .forms import SignupForm, EditUserForm, EditProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import *
from forum.models import *
from card.models import *
# Create your views here.

def homepage(request):
    return render(request, 'accounts/homepage.html')


def createcards(request):
    Card.create_cards(request.user)
    return redirect (reverse('my_cards'))



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
        transactions = BalanceUpdate.objects.filter(profile = self.request.user.profile)
        money = 0
        for transaction in transactions:
            money += transaction.amount
        context['money'] = money
        return context
    
    def get_object(self, queryset= None):
        return self.request.user.profile

    def form_valid(self, form):
        user_form = EditUserForm(self.request.POST, instance = self.request.user)
        if user_form.is_valid():
            user_form.save()
        return super().form_valid(form)

class UserListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = User
    template_name = 'accounts/all_users.html'
    def test_func(self):
        return self.request.user.is_superuser

class UserDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = User
    template_name = 'accounts/delete_user.html'
    success_url = reverse_lazy('all_users') 
    def test_func(self):
        return self.request.user.is_superuser

class ThreadDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Thread
    template_name = 'accounts/delete_thread.html'
    success_url = reverse_lazy('thread') 
    def test_func(self):
        return self.request.user.is_superuser

class SingularDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Singular
    template_name = 'accounts/delete_Singular.html'
    success_url = reverse_lazy('all_posts') 
    def test_func(self):
        return self.request.user.is_superuser

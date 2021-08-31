from .forms import CreateResponseForm
from django.shortcuts import redirect, render
from .models import *
from django.views.generic import CreateView, UpdateView, DetailView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

# def cards(request):
#     return render(request,'card/cards.html', {'cards': Card.objects.all()})


 
class CardListView(ListView):
    model = Card
    template_name = 'card/cards.html'

class MyCardListView(LoginRequiredMixin,ListView):
    model = Singular
    template_name = 'card/my_cards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mine'] = self.request.user.profile.deck.all().order_by('card')
        # context['form'] = form
        return context

class CreatePostView(LoginRequiredMixin,CreateView):
    model =Post
    fields = []
    template_name = 'card/post.html' 
    success_url = reverse_lazy('all_posts')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.profile = self.request.user.profile
        post.singular = Singular.objects.get(id = self.kwargs['pk'])
        post.save()
        return super().form_valid(form)

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'card/all_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CreateResponseForm(instance=self.request.user)
        form.fields['card_buyer'].queryset = Singular.objects.filter(owner = self.request.user.profile)
        context['form'] = form
        return context



class PostdetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'card/this_post.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['me'] = self.request.user.profile
        # context['form'] = form
        return context




class CreateResponseView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    
    model =Response
    fields =['card_buyer','amount']
    template_name = 'card/response.html' 
    success_url = reverse_lazy('all_posts')
    error_message = 'YOU DONT HAVE ENOUGH MONEY FOR THIS TRANSACTION'


    def get_form(self, form_class= None):
        form = super().get_form(form_class=form_class)
        form.fields['card_buyer'].queryset = Singular.objects.filter(owner = self.request.user.profile)
        return form


    def form_valid(self, form):
        response = form.save(commit=False)
        response.buyer = self.request.user.profile
        response.post = Post.objects.get(id = self.kwargs['pk'])
        if response.good():    
            response.save()
            return super().form_valid(form)
        else:  
            # messages.warning(self,f'YOU DONT HAVE ENOUGH MONEY FOR THIS TRANSACTION')
            messages.error(self.request, self.error_message)
            return redirect (reverse('all_posts'))

# class ResponseListView(ListView):
#     model = Response
#     template_name = 'card/all_response.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['mine'] = self.request.user.profile.deck.all().order_by('card')
        
#         return context



class CreateAnswerView(LoginRequiredMixin,CreateView):
    model =Answer
    fields =['accept']
    template_name = 'card/answer.html' 
    success_url = reverse_lazy('all_posts')


    def form_valid(self, form):
        answer = form.save(commit=False)
        answer.transaction = Response.objects.get(id = self.kwargs['pk'])
        
        answer.save()
        answer.swap()
        return super().form_valid(form)

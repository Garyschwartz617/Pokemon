from django.shortcuts import render
from .models import *
from django.views.generic import CreateView, UpdateView, DetailView,ListView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

# def cards(request):
#     return render(request,'card/cards.html', {'cards': Card.objects.all()})


 
class CardListView(ListView):
    model = Card
    template_name = 'card/cards.html'

class MyCardListView(ListView):
    model = Singular
    template_name = 'card/my_cards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mine'] = self.request.user.profile.deck.all().order_by('card')
        # context['form'] = form
        return context

class CreatePostView(CreateView):
    model =Post
    fields = []
    template_name = 'card/post.html' 
    success_url = reverse_lazy('my_cards')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.profile = self.request.user.profile
        post.singular = Singular.objects.get(id = self.kwargs['pk'])
        post.save()
        return super().form_valid(form)

class PostListView(ListView):
    model = Post
    template_name = 'card/all_posts.html'


class PostdetailView(DetailView):
    model = Post
    template_name = 'card/this_post.html' 




class CreateResponseView(CreateView):
    model =Response
    fields =['card_buyer']
    template_name = 'card/response.html' 
    success_url = reverse_lazy('my_cards')

    def get_form(self, form_class= None):
        form = super().get_form(form_class=form_class)
        form.fields['card_buyer'].queryset = Singular.objects.filter(owner = self.request.user.profile)
        return form


    def form_valid(self, form):
        response = form.save(commit=False)
        response.buyer = self.request.user.profile
        response.post = Post.objects.get(id = self.kwargs['pk'])
        response.save()
        return super().form_valid(form)

# class ResponseListView(ListView):
#     model = Response
#     template_name = 'card/all_response.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['mine'] = self.request.user.profile.deck.all().order_by('card')
        
#         return context



class CreateAnswerView(CreateView):
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

from django.shortcuts import render,redirect
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Comment, Thread
from django.urls import reverse_lazy

# Create your views here.


class CreateThreadView(CreateView):
    model = Thread
    fields =['subject']
    success_url = reverse_lazy('thread')
    template_name = 'forums/thread.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['threads'] = Thread.objects.all()
        return context

    def form_valid(self, form):
        thread = form.save(commit=False)
        thread.creator = self.request.user.profile
        
        thread.save()
        return super().form_valid(form)


class CreateCommentView(CreateView):
    model = Comment
    fields =['text']
    # success_url = reverse_lazy('comment',)
    template_name = 'forums/comment.html'


    def get_success_url(self):
        return reverse_lazy('comment', kwargs={'pk':self.object.thread.id})



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(thread = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user_id = self.request.user.profile
        comment.thread = Thread.objects.get(id = self.kwargs['pk'])
        comment.save()
        return super().form_valid(form)

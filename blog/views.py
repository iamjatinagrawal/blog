from django.core.paginator import Paginator
from django.urls import reverse_lazy,reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView)


from .models import Post,ContactFormModel
from .forms import ContactForm


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        if 'q' in self.kwargs:
            return self.queryset.filter(category__name__icontains=self.kwargs['q']).order_by('-created_at')

        else:
            return self.queryset.order_by('-created_at')


class SearchPostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/search_post_list.html'

    def get_queryset(self):
        if 'q' in self.request.GET:
            if ' ' in self.request.GET['q']:
                words = self.request.GET['q'].split()
                # result_queryset = []
                # for i in words:
                #     result_queryset.append(self.queryset.filter(category__name__icontains=i))
                result_queryset = self.queryset.filter(category__name__icontains=words[0]) | \
                    self.queryset.filter(category__name__icontains=words[1])
                return result_queryset
            return self.queryset.filter(category__name__icontains=self.request.GET['q']).order_by('-created_at')

        else:
            return self.queryset.order_by('-created_at')

class PostDetailView(DetailView):
    model = Post


class ContactFormCreateView(CreateView):
    model = ContactFormModel
    template_name = 'blog/contact.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse_lazy('post-list')

    # def get_context_data(self, **kwargs):
    #     kwargs['message'] = 'Form submitted'
    #     return super().get_context_data(**kwargs)
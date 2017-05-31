from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from mysite.views import LoginRequiredMixin

from .models import Book

class IndexView(TemplateView):
    template_name = 'jejudaum:index.html'

class BookList(ListView):

    def get_queryset(self):
        return Book.objects.order_by('-update_date')

class BookDetail(DetailView):
    model = Book

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'name', 'content']
    success_url = reverse_lazy('jejudaum:book_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookCreate, self).form_valid(form)

class BookChangeList(LoginRequiredMixin, ListView):
    template_name = 'jejudaum/book_change_list.html'

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'name', 'content']
    success_url = reverse_lazy('jejudaum:book_list')

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('jejudaum:book_list')

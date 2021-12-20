from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.conf import settings
from django.urls import reverse,reverse_lazy
from django.contrib.auth import login,authenticate,logout
from library_app import models
from library_app import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView,
                                   UpdateView,
                                   ListView,
                                   DetailView,
                                   DeleteView)
                                   

from library_app.forms import CustomUserCreationForm
                

# Create your views here.

###########################################################


def index_page(request):
    return render(request,'index.html')

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


#############################################################


class BookListView(ListView):
    model = models.BOOK


class BookDetailView(LoginRequiredMixin ,DetailView):
    model = models.BOOK


class BookCreateView(LoginRequiredMixin, CreateView):
    model = models.BOOK
    form_class = forms.BookModelForm


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model=models.BOOK
    fields = ('Book_name','Book_description','Category','Publish_Date','Book_type','Price',)
    
    def get_success_url(self):
        return reverse('app:Book-list')
    

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model=models.BOOK
    success_url = reverse_lazy('app:Book-list')


#######################################################################
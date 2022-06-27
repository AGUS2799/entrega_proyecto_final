from venv import create
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from movies.models import Movies, Comment
from django.db.models import Q
from movies.forms import CommentForm
from pro_final.widget import DatePickerInput

# Create your views here.
class MoviesListView(ListView):
    model = Movies
    template_name = "movies/movies_list.html"


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        movies = Movies.objects.filter(name__contains=searched)
    
        return render(
            request=request,
            context={'searched': searched, 'movies': movies},
            template_name="movies/movies_search.html",
        )
    else:
        return render(
            request=request,
            context={},
            template_name="movies/movies_search.html",
        )


class MoviesDetailView(DetailView):
    model = Movies
    template_name = "movies/movies_detail.html"
    fields = ['name', 'release_date', 'director_name', 'description']
    


class MoviesCreateView(LoginRequiredMixin, CreateView):
    model = Movies
    success_url = reverse_lazy('movies:movies-list')
    fields = ['name', 'release_date', 'director_name', 'description']


class MoviesUpdateView(LoginRequiredMixin, UpdateView):
    model = Movies
    success_url = reverse_lazy('movies:movies-list')
    fields = ['name', 'release_date', 'director_name', 'description']
    widgets = {
        'release_date': DatePickerInput,
    }


class MoviesDeleteView(LoginRequiredMixin, DeleteView):
    model = Movies
    success_url = reverse_lazy('movies:movies-list')


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'movies/add_comment.html'
    success_url = reverse_lazy('movies:movies-list')



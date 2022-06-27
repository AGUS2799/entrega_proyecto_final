from django.shortcuts import render

# Create your views here.
from venv import create
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from series.models import Series
from movies.models import Comment
from movies.forms import CommentForm



# Create your views here.
class SeriesListView(ListView):
    model = Series
    template_name = "Series/Series_list.html"


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        series = Series.objects.filter(name__contains=searched)
    
        return render(
            request=request,
            context={'searched': searched, 'series': series},
            template_name="series/series_search.html",
        )
    else:
        return render(
            request=request,
            context={},
            template_name="series/series_search.html",
        )

class SeriesDetailView(DetailView):
    model = Series
    template_name = "Series/Series_detail.html"
    fields = ['name', 'release_date', 'director_name', 'description']
    


class SeriesCreateView(LoginRequiredMixin, CreateView):
    model = Series
    success_url = reverse_lazy('series:series-list')
    fields = ['name', 'release_date', 'director_name', 'description']


class SeriesUpdateView(LoginRequiredMixin, UpdateView):
    model = Series
    success_url = reverse_lazy('series:series-list')
    fields = ['name', 'release_date', 'director_name', 'description']


class SeriesDeleteView(LoginRequiredMixin, DeleteView):
    model = Series
    success_url = reverse_lazy('series:series-list')

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'series/add_comment.html'
    success_url = reverse_lazy('series:series-list')
    
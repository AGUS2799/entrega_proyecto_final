import imp
from django.shortcuts import render
from perfil.views import get_avatar_url_ctx

# Create your views here.
def home(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    print('context_dict: ', context_dict)
    return render(
        request=request,
        context=context_dict,
        template_name="home/home.html"
    )


def about(request):
    return render(request, 'home/about.html')
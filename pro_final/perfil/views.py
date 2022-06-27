from django.shortcuts import render
from user.models import User, Avatar

def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}

def datos_del_perfil(request, id):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    user = User.objects.get(pk=id)
    context_dict.update({
        'user': user,
    })
    print('context_dict: ', context_dict)
    return render(
        request=request,
        context=context_dict,
        template_name="perfil/perfil.html"
    )
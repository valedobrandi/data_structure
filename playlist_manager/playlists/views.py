from django.shortcuts import render, redirect
from playlists.forms import CreateSingerForm, CreateMusicModelForm
from playlists.models import Music


# Create your views here.
def index(request):
    context = {"musics": Music.objects.all()}
    return render(request, "home.html", context)


def music(request):
    form = CreateMusicModelForm()

    if request.method == "POST":
        form = CreateMusicModelForm(request.POST)

        if form.is_valid():
            Music.objects.create(**form.cleaned_data)
            return redirect("home-page")
    context = {"form": form}
    return render(request, "music.html", context)


def singer(request):
    form = CreateSingerForm()
    context = {"form": form}
    return render(request, "singer.html", context)

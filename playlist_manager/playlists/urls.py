from django.urls import path
from playlists.views import music, singer, index

urlpatterns = [
    path("", index, name="home-page"),
    path("music/", music, name="music-page"),
    path("singer/", singer, name="singer-page"),
]

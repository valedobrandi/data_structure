from django import forms
from playlists.validators import validate_music_length, validate_singers_name
from playlists.models import Music


class CreateMusicForm(forms.Form):
    name = forms.CharField(max_length=50, label="nome da música")
    recorded_at = forms.DateField(
        label="Data da gravação",
        initial="2023-07-06",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    length_in_seconds = forms.IntegerField(
        validators=[validate_music_length], label="duração em segundos"
    )


class CreatePlaylistForm(forms.Form):
    name = forms.CharField(max_length=50)
    is_active = forms.BooleanField()


class CreateSingerForm(forms.Form):
    name = forms.CharField(max_length=50, validators=[validate_singers_name])


class CreateMusicModelForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = "__all__"
        labels = {
            "name": "Nome da música",
            "recorded_at": "Data da gravação",
            "length_in_seconds": "Duração em segundos",
        }

        widgets = {
            "recorded_at": forms.DateInput(
                attrs={"type": "date", "value": "2023-07-06"}
            )
        }

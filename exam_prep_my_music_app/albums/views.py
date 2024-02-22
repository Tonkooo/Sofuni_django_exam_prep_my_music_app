from django.urls import reverse_lazy
from django.views import generic as views

from exam_prep_my_music_app.albums.models import Album
from django import forms

from exam_prep_my_music_app.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


class CreateAlbumView(views.CreateView):
    queryset = Album.objects.all()
    fields = ("name", "artist_name", "genre", "description", "image_url", "price")
    template_name = "albums/album-add.html"
    success_url = reverse_lazy("index")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["name"].widget.attrs["placeholder"] = "Album Name"
        form.fields["artist_name"].widget.attrs["placeholder"] = "Artist"
        form.fields["description"].widget.attrs["placeholder"] = "Description"
        form.fields["image_url"].widget.attrs["placeholder"] = "Image URL"
        form.fields["price"].widget.attrs["placeholder"] = "Price"
        return form


    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = get_profile()
        return super().form_valid(form)

class DetailAlbumView(views.DetailView):
    queryset = Album.objects.all()
    template_name = "albums/album-details.html"


class EditAlbumView(views.UpdateView):
    queryset = Album.objects.all()
    template_name = "albums/album-edit.html"
    fields = ("name", "artist_name", "genre", "description", "image_url", "price")

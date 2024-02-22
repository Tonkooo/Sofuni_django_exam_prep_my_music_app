from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from exam_prep_my_music_app.albums.models import Album

from exam_prep_my_music_app.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


class AlbumFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["name"].widget.attrs["placeholder"] = "Album Name"
        form.fields["artist_name"].widget.attrs["placeholder"] = "Artist"
        form.fields["description"].widget.attrs["placeholder"] = "Description"
        form.fields["image_url"].widget.attrs["placeholder"] = "Image URL"
        form.fields["price"].widget.attrs["placeholder"] = "Price"
        return form
# text in the form fields


class ReadonlyviewMixin:

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"
            #field.widget.attrs["disabled"] = "disabled"

        return form
# when delete form text in the fields cannot be deleted.

class CreateAlbumView(AlbumFormMixin, views.CreateView):
    queryset = Album.objects.all()
    fields = ("name", "artist_name", "genre", "description", "image_url", "price")
    template_name = "albums/album-add.html"
    success_url = reverse_lazy("index")

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #
    #     form.fields["name"].widget.attrs["placeholder"] = "Album Name"
    #     form.fields["artist_name"].widget.attrs["placeholder"] = "Artist"
    #     form.fields["description"].widget.attrs["placeholder"] = "Description"
    #     form.fields["image_url"].widget.attrs["placeholder"] = "Image URL"
    #     form.fields["price"].widget.attrs["placeholder"] = "Price"
    #     return form


    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = get_profile()
        return super().form_valid(form)

class DetailAlbumView(views.DetailView):
    queryset = Album.objects.all()
    template_name = "albums/album-details.html"


class EditAlbumView(AlbumFormMixin, views.UpdateView):
    queryset = Album.objects.all()
    template_name = "albums/album-edit.html"
    fields = ("name", "artist_name", "genre", "description", "image_url", "price")
    success_url = reverse_lazy("index")  # redirect to index page


class DeleteAlbumView(ReadonlyviewMixin, views.DeleteView):
    queryset = Album.objects.all()
    template_name = "albums/album-delete.html"
    success_url = reverse_lazy("index")  # redirect to index page
    form_class = modelform_factory(Album, fields=("name", "artist_name", "genre", "description", "image_url", "price"))
    # with this form_class we bring the whole album form fields. If this is missing, there
    # is only "delete" button

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs                          # this kwargs fills in the form with the album information




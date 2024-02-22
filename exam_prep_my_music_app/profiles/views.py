from django.views import generic as views
from exam_prep_my_music_app.albums.models import Album
from exam_prep_my_music_app.profiles.models import Profile
from django.urls import reverse_lazy


def get_profile():
    return Profile.objects.first()


class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()

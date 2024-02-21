from django import forms
# from django.views import generic as views
from django.shortcuts import render, redirect

from exam_prep_my_music_app.profiles.models import Profile
from exam_prep_my_music_app.web.Forms import CreateProfileForm


def get_profile():
    return Profile.objects.first()

def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        "form": form,
    }
    return render(request, 'web/home-no-profile.html', context)


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    return render(request, 'web/home-with-profile.html')

# class IndexView(views.Templateview):
#     def get_template_names(self):
#         if get_profile() is None:
#             return 'web/home-no-profile.html'
#         return 'web/home-with-profile.html'

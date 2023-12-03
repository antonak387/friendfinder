from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('feed')
    template_name = "registration/signup.html"

    # def post(self, request, *args, **kwargs):
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.save()
    #
    #         for form_ug in form.cleaned_data['groups']:
    #             user_group = Group.objects.get(name=form_ug.name)
    #             user.groups.add(user_group)
    #         return redirect('feed')
    #     else:
    #         return render(request, self.template_name, {'form': form})


def index(request):
    if request.user.is_authenticated:
        return redirect('feed')
    else:
        return render(request, 'main/index.html')

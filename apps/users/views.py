# from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import User


class EditProfile(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'users/candidate_edit.html'
    fields = ['name', 'email', 'first_name', 'last_name']
    success_url = reverse_lazy('user_edit')
    success_message = "Profile was updated successfully"

    def get_object(self, *args, **kwargs):
        obj = self.model.objects.get(pk=self.request.user)
        return obj


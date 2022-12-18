from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CreateUserForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Foto
import os


def index(request):
    return render(request, "index.html")


class SignUp(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class StartFoto(ListView):
    model = Foto
    template_name = 'home.html'

    @staticmethod
    def to_context(field_context, field_):
        context_ = []
        for cont in field_context:
            if cont[field_]:
                context_.append(cont)
        return context_

    @staticmethod
    def name_to_context(field_context, field_):
        context_ = []
        for cont in field_context:
            if cont[field_]:
                context_.append(cont[field_])
        return context_


    def get_queryset(self):
        user = self.request.user
        if user:
            return self.model.objects.filter(owner=user).order_by('id').reverse()[:3]

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user:
            context = super(StartFoto, self).get_context_data(**kwargs)
            date_context = self.model.objects.filter(owner=user).values("date").distinct()
            persona_context = self.model.objects.filter(owner=user).values("names").distinct()
            geolocation_context = self.model.objects.filter(owner=user).values("geolocation").distinct()
            id_context = self.model.objects.filter(owner=user).values("id")
            context["date_context"] = self.to_context(date_context, "date")
            context["geolocation_context"] = self.to_context(geolocation_context, "geolocation")
            context["persona_context"] = self.name_to_context(persona_context, "names")
            context["id_context"] = self.to_context(id_context, "id")
            return context


class AddFoto(LoginRequiredMixin, CreateView):
    model = Foto
    fields = ['title', 'geolocation', 'date', 'names', 'image']
    template_name = 'new_foto.html'
    success_url = '/foto/home'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(AddFoto, self).form_valid(form)


class SearchDate(LoginRequiredMixin, StartFoto):

    def get_queryset(self):
        query_date = self.request.GET.get('date')
        user = self.request.user
        return self.model.objects.filter(Q(owner=user) & Q(date=query_date))


class SearchPerson(LoginRequiredMixin, StartFoto):

    def get_queryset(self):
        query_person = self.request.GET.get('person')
        user = self.request.user
        return self.model.objects.filter(Q(owner=user) & Q(names=query_person))


class SearchGeo(LoginRequiredMixin, StartFoto):

    def get_queryset(self):
        query_geo = self.request.GET.get('geo')
        user = self.request.user
        return self.model.objects.filter(Q(owner=user) & Q(geolocation=query_geo))


class SearchID(LoginRequiredMixin, StartFoto):
    template_name = 'search_result.html'

    def get_queryset(self):
        query_id = self.request.GET.get('id')
        user = self.request.user
        return self.model.objects.get(Q(owner=user) & Q(id=query_id))


def error_500(request):
    return render(request, '500.html')

def delete(request, id):
    data = get_object_or_404(Foto, id=id)
    path_img = "media/" + str(data.image)
    os.remove(path_img)
    data.delete()
    return redirect('home')


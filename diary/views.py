from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from diary.forms import DiaryForm
from diary.forms import Diary


class IndexView(TemplateView):
    template_name = 'index.html'


class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('diary:diary_create_complete')


class DiaryCreateCompleteView(TemplateView):
    template_name = 'diary_create_complete.html'

class DiaryListView(ListView):
    template_name = 'diary_list.html'
    model = Diary
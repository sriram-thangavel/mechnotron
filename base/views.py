from django.shortcuts import render
from .models import Event,Extra
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .utils import counter,contact
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from .forms import ContactForm


# Create your views here.
def home(request):
    technical = Event.objects.filter(category="Technical").filter(publish=True)
    nontechnical = Event.objects.filter(category="Non-Technical").filter(publish=True)
    workshop = Extra.objects.filter(category="Workshop").filter(publish=True)
    webinar = Extra.objects.filter(category="Webinar").filter(publish=True)
    context = {'technical':technical[:3],'nontechnical':nontechnical[:3],'technicalcount':counter(technical.count(),3),'nontechnicalcount':counter(nontechnical.count(),3),'workshops':workshop,'webinars':webinar}
    context['form']=contact(request)
    return render(request,"pages/index.html",context)

class technical_listview(ListView):
    model = Event
    template_name = "pages/technical_list.html"
    context_object_name = "technical"
    paginate_by = 6
    queryset = Event.objects.filter(category="Technical").filter(publish=True)

class nontechnical_listview(ListView):
    model = Event
    template_name = "pages/nontechnical_list.html"
    context_object_name = "nontechnical"
    paginate_by = 6
    queryset = Event.objects.filter(category="Non-Technical").filter(publish=True)

    

class event_detailview(DetailView):
    model = Event
    context_object_name = "detail"
    template_name = "pages/event_detail.html"

class extra_detailview(DetailView):
    model = Extra
    context_object_name = "detail"
    template_name = "pages/extra_detail.html"

class Search(ListView):
    model = Event
    context_object_name = "search"
    template_name = "pages/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Event.objects.filter(publish=True).annotate(search=SearchVector("title", "description")).filter(
            search=query
        )







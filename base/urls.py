from django.urls import path
from .views import home,event_detailview,extra_detailview,technical_listview,nontechnical_listview,Search


urlpatterns = [
    path('', home,name="home"),
    path("technical-events",technical_listview.as_view(),name="technical_list"),
    path("non-technical-events",nontechnical_listview.as_view(),name="nontechnical_list"),
    path("search/",Search.as_view(),name="search"),
    path("events/<int:pk>/<str:category>-<str:slug>/",event_detailview.as_view(),name="event_detail"),
    path("<str:category>/<int:pk>/<str:slug>/",extra_detailview.as_view(),name="extra_detail"),
   
]


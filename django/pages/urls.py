from django.urls import path

from .views import AboutPageView, HomePageView, ContactsPageView, LinksPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('links/', LinksPageView.as_view(), name='links'),
]

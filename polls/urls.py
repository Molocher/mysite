from django.urls import path

from . import views
from .views import MyView, ArticleCounterRedirectVew
from django.views.generic.base import RedirectView

urlpatterns = [
    path("mine/", MyView.as_view(), name="my-view"),
    path("", views.index, name="index"),
    path("counter/<int:pk>/", ArticleCounterRedirectVew.as_view(), name="article-counter"),
    path("go-to-django/", RedirectView.as_view(url="https://www.djangoproject.com"), name="go-to-django")
]

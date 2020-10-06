from django.contrib import admin
from django.urls import path
from main import views as main_views
from django.conf.urls import url

from main.views.moim import MoimListView
from main.views.planview import PlanView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('moim/', MoimListView.as_view())
]

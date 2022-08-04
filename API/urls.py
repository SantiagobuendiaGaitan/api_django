from django.urls import URLPattern, path
from .views import BibliotecaListView, BibliotecaDetailView

urlpatterns = [
    path('biblioteca/', BibliotecaListView.as_view(), name='biblioteca_list'),
    path('biblioteca/<int:pk>/', BibliotecaDetailView.as_view(), name='biblioteca_detail'),
]
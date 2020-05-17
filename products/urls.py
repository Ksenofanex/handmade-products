from django.urls import path
from .views import TableListView, TableDetailView, SearchResultsView

urlpatterns = [
    path('', TableListView.as_view(), name='table_list'),
    path('<int:pk>/', TableDetailView.as_view(), name='table_detail'),
    path('search/', SearchResultsView.as_view(), name='search'),
]
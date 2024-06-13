from django.urls import path
from .views import QueryView, ResultView, HistoryView, PingView

urlpatterns = [
    path('query', QueryView.as_view(), name='query'),
    path('result', ResultView.as_view(), name='result'),
    path('history', HistoryView.as_view(), name='history'),
    path('ping', PingView.as_view(), name='ping'),
]

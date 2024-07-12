from django.urls import path
from .views import StickerListView, StickerDetailView

urlpatterns = [
    path('', StickerListView.as_view(), name='sticker_list'),
    path('<int:pk>/', StickerDetailView.as_view(), name='sticker_detail'),
]

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sticker

class StickerListView(ListView):
    print("StickerListView")
    model = Sticker
    template_name = 'inventory/sticker_list.html'

class StickerDetailView(DetailView):
    model = Sticker
    template_name = 'inventory/sticker_detail.html'

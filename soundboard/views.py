from django.shortcuts import render, get_object_or_404

from .models import SoundboardCategory, Soundboard, SoundCategory, Sound

# Create your views here.


def index(request):
    soundboard_categories = SoundboardCategory.objects.all()
    context = {
        'soundboard_categories': soundboard_categories,
    }
    return render(request, 'soundboard/index.html', context)


def view_soundboard(request, soundboard_id):
    soundboard = get_object_or_404(Soundboard, pk=soundboard_id)
    sound_categories = soundboard.soundcategory_set.all()
    context = {
        'soundboard': soundboard,
        'sound_categories': sound_categories,
    }
    return render(request, 'soundboard/soundboard.html', context)

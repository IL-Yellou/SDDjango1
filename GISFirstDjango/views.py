from django.shortcuts import render
from .models import Person

def splash(request):
    name = 'Billy'
    people = Person.objects.all()
    animals = ["Cat", "Monkey", "Pig"]
    debug_people = list(people)
    return render(request, "splash.html", {'name': name,
                                           'values': values})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Profile

@login_required
def user_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {
        'user': user,
        'profile': profile
    }
    return render(request, 'user_profile.html', context)


from django.shortcuts import render


def challenge(request):
    """ A view to return the challenge page """

    return render(request, 'challenge/challenge.html')
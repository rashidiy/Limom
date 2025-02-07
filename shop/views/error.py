from django.shortcuts import render
from django.utils.translation import activate

def custom_404_view(request, exception=None):
    user_language = request.LANGUAGE_CODE
    activate(user_language)
    return render(request, "pages/404.html", status=404)

def custom_500_view(request, exception=None):
    user_language = request.LANGUAGE_CODE
    activate(user_language)
    return render(request, "pages/500.html", status=500)

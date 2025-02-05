from django.shortcuts import render
from django.utils.translation import activate

def custom_404_view(request, exception):
    user_language = request.LANGUAGE_CODE
    activate(user_language)
    return render(request, "pages/404.html", status=404)
from django.shortcuts import render
from .utils.keygen import generate_key


def dashboard(request):
    key = generate_key()
    return render(
        request=request, template_name="dashboard.html", context={"api_key": key}
    )

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Custom decorator to simulate permission check
def superuser_required(view_func):
    actual_decorator = user_passes_test(
        lambda u: u.is_superuser,
        login_url='/accounts/login/',  # Redirect to login if not authenticated
        redirect_field_name=None  # Avoid redirect loops
    )
    return actual_decorator(view_func)

@superuser_required
def restricted_view(request):
    return HttpResponse("This is a restricted view.")

def handler403(request, exception):
    """ Error Handler 403 - Forbidden """
    return render(request, "errors/403.html", status=403)

def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)

from functools import wraps
from django.shortcuts import render

def handle_errors(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            return view_func(request, *args, **kwargs)
        except Exception as e:
            return render(request, 'error.html')
    return _wrapped_view

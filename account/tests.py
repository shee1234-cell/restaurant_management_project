from django.shortcuts import render
from django.http import HttpResponse

def menu_list(request):
    try:
        menu_items = [
            {"name": "Pizza", "price": "250"},
            {"name": "Pasta", "price": "200"},
            {"name": "Biryani", "price": "550"},
            {"name": "Coffee", "price": "150"}
        ]
        return render(request, "menu_list.html", {"menu_items": menu_items})
    except Exception as e:
        error_message: f"Oops! something went wrong: {str(e)}"
        return HttpResponse(error_message, status=500)

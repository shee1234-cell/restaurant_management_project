from django.shortcuts import render

def menu_list(request):
    menu_items = [
        {"name": "Pizza", "price": "250"},
        {"name": "Pasta", "price": "350"},
        {"name": "Biriyani", "price": "550"},
        {"name": "Coffee", "price": "150"},
    ]
    return render(request, "menu_list.html", {"menu_item": menu_items})
from rest_framework import api_view
from rest_framework.response import Response

@api_view(['GET'])
def menu_view(request):
    menu = [
        {
            'name': 'Margherita Pizza'
            'description': 'Classic cheese pizza with basil.'
            'price': 299
        },
        {
            'name': 'Paneer Tikka Pizza'
            'description': 'Classic grilled paneer with freshly spicy chilli.'
            'price': 299
        },
        {
            'name': 'Chicken Pizza'
            'description': 'Juciy chicken flavoured with Indian spices'
            'price': 499
        }
    ]
    return Response(menu)



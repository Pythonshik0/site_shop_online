from django.shortcuts import render
from carts.models import Cart
from users.models import User
# Create your views here.
def create_order(request):
    return render(request, 'orders/create_order.html')

def done_order(request, user_id):
    user_to_delete = User.objects.get(id=user_id)
    carts_to_delete = Cart.objects.filter(user=user_to_delete)
    carts_to_delete.delete()
    return render(request, 'orders/done_order.html')
    
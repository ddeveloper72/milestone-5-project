from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """
    A view that renders the cart contents page
    """
    return render(request, "cart.html")


def add_to_cart(request, pk):
    """
    Add a quantity of the specified product to the cart
    """
    quantity = int(request.POST.get('quantity'))    

    cart = request.session.get('cart', {})
    cart[pk] = cart.get(pk, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, pk):
    """
    Adjust the quantituy of a specified product in the cart
    to the speciefied ammount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

# we can only adjust a quantity if there is already something in the cart.
    if quantity > 0:
        cart[pk] = quantity
    else:
        cart.pop(pk)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

# Create your views here.

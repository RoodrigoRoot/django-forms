from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from .models import Pizza
from django.forms import formset_factory
# Create your views here.


def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, request.FILES)    
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            print(created_pizza_pk)
            note = 'Thanks for ordering! You %s %s and %s is on its way' %(filled_form.cleaned_data.get("size"),filled_form.cleaned_data.get("topping1"),filled_form.cleaned_data.get("topping2"))
            new_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = 'Pizza order has failed. Try again'
        return render(request, 'pizza/order.html', {'created_pizza_pk':created_pizza_pk,'pizzaform':filled_form, 'note':note, 'multiple_form':multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform':form,'multiple_form':multiple_form})


def pizzas(request):
    number_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    
    if filled_multiple_pizza_form.is_valid():
        number_pizzas = filled_multiple_pizza_form.cleaned_data.get("number")
    PizzaFormSet = formset_factory(PizzaForm, extra=number_pizzas)
    formset = PizzaFormSet()

    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        print(filled_formset)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data.get("topping1"))
            note = "Pizzas has been ordered!"
        else:
            note = "Order is not create. Please try again"
        return render(request, 'pizza/pizzas.html', {'note':note, 'formset':formset})
    else:
        return render(request, 'pizza/pizzas.html', {'formset':formset})


def edit_order(request, pk):
    pizza = Pizza.objects.get(id=pk)
    form = PizzaForm(instance=pizza)
    if request.method == "POST":
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = "Order has been updated"
            return render(request, 'pizza/edit_order.html', {'pizzaform':form, 'pizza':pizza, 'note':note})
    return render(request, 'pizza/edit_order.html', {'pizzaform':form, 'pizza':pizza})


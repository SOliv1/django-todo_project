from django.shortcuts import render, HttpResponse, redirect
from .models import Item
from .forms import ItemForm


# Create your views here.
def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {
        'items': results
    })


def create_an_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    
    else:
        form = ItemForm()

    return render(request, "item_form.html", {'form': form})
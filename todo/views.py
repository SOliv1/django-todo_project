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

    def create_an_item(request):
        if request.method == "POST":
            new_item = Item()
            new_item.name = request.POST.get('name')
            new_item.done = 'done' in request.POST
            new_item.save()

        return redirect(get_todo_list)

    return render(request, "item_form.html")

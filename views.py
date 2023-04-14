from django.shortcuts import render
from django import forms
# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Task Field")
    #phone = forms.IntegerField(label="phone", min_value="10", max_value="12")

tasks = [ "buy stuff", "sleep"]

def tasks(request):
    return render(request, "tasks.html", {

        "task": tasks
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["tasks"]
            tasks.append(tasks)

        else:
            return render(request, "add.html",{
                "form":form
            })
    return render(request, "add.html", {
        "form": NewTaskForm()
    })
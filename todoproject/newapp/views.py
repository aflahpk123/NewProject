from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from . models import Task
from . forms  import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'add.html'
    context_object_name = 'final'

class TaskDetails(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name = 'dtls'

class TaskUpdate(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('task_name','priority','date')

    def get_success_url(self):
        reverse_lazy('detailview',kwargs={'pk':self.object.id})

class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')


def add(request):
    result = Task.objects.all()
    # if request.method=='POST':
    #     task_name=request.POST.get('task','')
    #     priority=request.POST.get('priority', '')
    #     date= request.POST.get('date', '')
    #     task=Task(task_name=task_name,priority=priority,date=date)
    #     task.save()

    return render(request,'add.html',{'final':result})

def delete(request,taskid):
    result=Task.objects.get(id=taskid)
    if request.method=='POST':
        result.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    result=Task.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=result)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'result':result,'form':form})
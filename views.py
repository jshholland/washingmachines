from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
from votes.models import Machine, Update, UpdateForm
from votes.tasks import reset_in_use
from django.conf import settings


def index(request):
    washer_list = Machine.objects.filter(kind='w').order_by('number')
    dryer_list = Machine.objects.filter(kind='d').order_by('number')
    return render(request, 'index.html', {
        'washer_list': washer_list,
        'dryer_list': dryer_list,
    })


def detail(request, machine_id):
    m = get_object_or_404(Machine, pk=machine_id)
    f = UpdateForm()
    return render(request, 'detail.html', {"machine": m, "form": f})


def edit(request, machine_id):
    m = get_object_or_404(Machine, pk=machine_id)
    u = Update(machine=m, comment="")
    f = UpdateForm(request.POST, instance=u)
    if f.is_valid():
        m.last_updated = datetime.now()
        m.state = f.cleaned_data["state"]
        if m.state == 'u':
            reset_in_use.apply_async(args=(m,), delay=settings.WASHING_RUNTIME)
        f.save()
        m.save()
        return redirect('votes.views.result', m.id)
    return render(request, 'detail.html', {"machine": m, "form": f, "err": "You didn't fill in all the information!"})


def result(request, machine_id):
    m = get_object_or_404(Machine, pk=machine_id)
    return render(request, "result.html", {'machine': m})

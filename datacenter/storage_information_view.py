from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

import time

from django.utils.timezone import localtime



def storage_information_view(request):
    # Программируем здесь
    not_leave = Visit.objects.filter(leaved_at__isnull=True)
    info_title = ['who_entered', 'entered_at', 'duration']
    non_closed_visits = []

    for visiters in not_leave:
        enter_time_not_leave = localtime(visiters.entered_at)
        duration = Visit.format_duration(visiters)
        list_visiters = [visiters.passcard, enter_time_not_leave, duration]
        non_closed_visits.append(dict(zip(info_title, list_visiters)))


    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

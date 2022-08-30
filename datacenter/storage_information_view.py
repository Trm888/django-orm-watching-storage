from datacenter.models import Passcard

from datacenter.models import Visit

from django.shortcuts import render

from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True)
    info_title = ['who_entered', 'entered_at', 'duration']
    serialized_non_closed_visits = []
    for visiters in non_closed_visits:
        enter_time_not_leave = localtime(visiters.entered_at)
        duration = Visit.format_duration(visiters)
        list_visiters = [visiters.passcard, enter_time_not_leave, duration]
        serialized_non_closed_visits.append(dict(zip(info_title, list_visiters)))
    context = {
        'non_closed_visits': serialized_non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

from datacenter.models import Passcard

from datacenter.models import Visit

from django.shortcuts import render, get_object_or_404

from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard.objects.filter(passcode=passcode))
    employee_visits = Visit.objects.filter(passcard__passcode=passcode)
    info_title = ['entered_at', 'duration', 'is_strange']
    this_passcard_visits = []
    for visit in employee_visits:
        enter_time = localtime(visit.entered_at)
        duration = Visit.format_duration(visit)
        list_visiters = [enter_time, duration, Visit.is_visit_long(visit)]
        this_passcard_visits.append(dict(zip(info_title, list_visiters)))
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

from django.shortcuts import render
from .models import *


def home(request):
    qidiruv = request.GET.get("searched")
    togri = Togri.objects.filter(soz=qidiruv)
    if len(togri) == 0:
        notogri = Notogri.objects.filter(soz=qidiruv)
        if len(notogri) == 0:
            togri = "Bunaqa soz bazada yo'q"
            notogri = ""
        else:
            togri = notogri[0].t_soz
            notogri = Notogri.objects.filter(t_soz=togri)
    else:
        togri = togri[0]
        notogri = Notogri.objects.filter(t_soz__soz=togri)
    content = {
        "t":togri,
        "n":notogri
    }

    return render(request,'result.html',content)

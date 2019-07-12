from __future__ import unicode_literals
from django.shortcuts import render
from .models import ballot_record

def main(request):
    records = ballot_record.objects.all()

    context = {
        'records': records,
    }

    return render(request, 'index.html', context)


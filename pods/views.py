from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from pods.models import *

from django.template import Context
import  json
import datetime
from django.shortcuts import get_object_or_404
import sys

# Create your views here.
def index(request):
#t = get_template('templates/base.html')
#now = datetime.datetime.now()
#html = t.render(context=None, request=None)
#p=Task.objects.filter(thash=gt['hash'])
#p = Task.objects
#a = p.values_list()
#p2 = Task.objects.all()
#html=json.dumps(a['job'])

#now = datetime.datetime.now()
    pod_list = PodcastEpisode.objects.order_by('publicated').reverse()
    pod=pod_list[0]
    template = loader.get_template('base.html')
    context = {'pod_list': pod_list,'pod':pod}
    return HttpResponse(template.render(context))



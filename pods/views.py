from django.shortcuts import render

# Create your views here.
def index(request):
    # t = get_template('templates/base.html')
    # now = datetime.datetime.now()
    # html = t.render(context=None, request=None)
    # p=Task.objects.filter(thash=gt['hash'])
    p = Task.objects
    a = p.values_list()
    p2 = Task.objects.all()
    # html=json.dumps(a['job'])
    t = get_template('templates/base.html')
    now = datetime.datetime.now()
    html = t.render(context={'tasks': p2}, request=None)


return HttpResponse(html)
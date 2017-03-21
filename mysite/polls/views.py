from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
# Create your views here.
from django.template import RequestContext,loader
from polls import models
# def auth(request):
#     return HttpResponse("hello")
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse(loader.get_template("pages/index.html").render())
# @csrf_exempt
# def authlogin(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     return HttpResponse(username+password)
@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            if username == "" and password == "":
                return render_to_response("pages/login.html",{'login_info':'用户名或密码不能为空!'})
            Line_num = models.User.objects.filter(username=username).count()
            Line_num1 = models.User.objects.filter(username=username, password=password).count()
            if Line_num == 0:
                return render_to_response("pages/login.html", {'login_info': '用户名不存在!'})
            elif Line_num1 != 1:
                return render_to_response("pages/login.html",{'login_info':u'密码错误!'})
            else:
                # m = models.User.objects.get(username=username)
                # request.session['User_id'] = m.id
                print(request.path)
                return render_to_response("pages/index.html")

        except KeyError:
            return HttpResponse(loader.get_template("pages/login.html").render())
    return render_to_response("pages/login.html",{})

@login_required()
def flot(request):
    return HttpResponse(loader.get_template("pages/flot.html").render())
@login_required()
def morris(request):
    return HttpResponse(loader.get_template("pages/morris.html").render())
@login_required()
def tables(request):
    return HttpResponse(loader.get_template("pages/tables.html").render())
@login_required()
def forms(request):
    return HttpResponse(loader.get_template("pages/forms.html").render())
@login_required()
def panels_wells(request):
    return HttpResponse(loader.get_template("pages/panels-wells.html").render())
@login_required()
def buttons(request):
    return HttpResponse(loader.get_template("pages/buttons.html").render())
@login_required()
def notifications(request):
    return HttpResponse(loader.get_template("pages/notifications.html").render())
@login_required()
def typography(request):
    return HttpResponse(loader.get_template("pages/typography.html").render())
@login_required()
def icons(request):
    return HttpResponse(loader.get_template("pages/icons.html").render())
@login_required()
def grid(request):
    return HttpResponse(loader.get_template("pages/grid.html").render())
@login_required()
def blank(request):
    return HttpResponse(loader.get_template("pages/blank.html").render())
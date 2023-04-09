from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
import hashlib, math
import math


def index(request):
    start = "login"
    ret = ""
    return render(request, 'userpage/home.html', {'error':"none", 'start':start, 'ret':-1})


def calculate(request):
    start = "login"
    ht1 = 0
    ht2 = 0
    mw = "0"
    mh = "0"
    wt1 = 0
    if request.POST["system"] == "1":
        ht1 = int(request.POST["centi"])
        wt1 = int(request.POST["kilo"])
        mw = "2"
        mh = "2"
    if request.POST["system"] == "0":
        ht1 = int(request.POST["feet"])
        ht2 = int(request.POST["inch"])
        wt1 = int(request.POST["pound"])
        mw = "1"
        mh = "1"
    ret = auto(3, ht1, mh, ht2, wt1, mw)
    return render(request, 'userpage/home.html', {'error':"none", 'start':start, 'ret':ret})


def height(x=None, m=None, y=None):
    ht = 0
    h = m
    if h == "1":
        h1 = x
        try:
            h1 = int(h1)
            if h1 < 0:
                return "unacceptable input '{}' is negative".format(h1)
        except:
            return "unacceptable input '{}' is not an integer".format(h1)
        h2 = y
        try:
            if h2 < 0:
                return "unacceptable input '{}' is negative".format(h2)
        except:
            return "unacceptable input '{}' is not an integer".format(h2)
        ht = h1*12 + h2
        if ht == 0:
            return "unacceptable inputs total height is zero inches"
        else:
           ht = ht * 0.0254
    elif h == "2":
        h1 = x
        try:
            if h1 <= 0:
                return "unacceptable input '{}' is negative or zero".format(h1)
        except:
            return "unacceptable input '{}' is not an integer".format(h1)
        ht = h1 / 100
    else:
        return "unacceptable input '{}' is not an accepted method".format(h)
    return ht


def weight(x=None, m=None):
    wt = 0
    w = m
    if w == "1":
        w1 = x
        try:
            if w1 < 0:
                return "unacceptable input '{}' is negative".format(w1)
        except:
            return "unacceptable input '{}' is not an integer".format(w1)
        wt = w1
        if wt == 0:
            return "unacceptable inputs total height is zero pounds"
        else:
            wt = wt * 0.453592
    elif w == "2":
        w1 = x
        try:
            if w1 <= 0:
                return "unacceptable input '{}' is negative or zero".format(w1)
        except:
            return "unacceptable input '{}' is not an integer".format(w1)
        wt = w1
    else:
        return "unacceptable input '{}' try again".format(m)
    return wt


def auto(funtar, ht1, mh, ht2=0, wt1=0, mw=0):
    if funtar == 1:
        return (height(ht1, mh, ht2))
    if funtar == 2:
        return (weight(ht1, mh))
    if funtar == 3:
        h = height(ht1, mh, ht2)
        w = weight(wt1, mw)
        if isinstance(h, str):
            return h
        if isinstance(w, str):
            return w
        h2 = math.pow(h, 2)
        bmi = w / h2
        if 0 < bmi < 18.5:
            return ("bmi of %.2f is considered underweight" % bmi)
        elif 18.5 <= bmi < 25:
            return ("bmi of %.2f is considered normal weight" % bmi)
        elif 25 <= bmi < 30:
            return ("bmi of %.2f is considered overweight" % bmi)
        elif 30 <= bmi < 40:
            return ("bmi of %.2f is considered obese" % bmi)
        elif 40 <= bmi:
            return("bmi of %.2f is considered extremely obese" % bmi)
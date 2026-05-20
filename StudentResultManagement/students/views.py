from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def academic(request):
    return render(request, "academic.html")

def gallery(request):
    return render(request, "gallery.html")


def contact(request):
    return render(request, "contact.html")


def feespyment(request):
    return render(request, "feespyment.html")


def readmore(request):
    return render(request, "readmore.html")


def dashboard(request):
    return render(request, "dashboard.html")

def administration(request):
    return render(request, "administration.html")

def student(request):
    return render(request, 'student.html')


def teacher(request):
    return render(request, "teacher.html")


def courses(request):
    return render(request, "courses.html")


def facilities(request):
    return render(request, "facilities.html")


def result(request):
    return render(request, "result.html")

def studentlogin(request):
    return render(request, "studentlogin.html")






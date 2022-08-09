from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.

# TEMPLATE_DIRS = (
#     'os.path.join(BASE_DIR, "templates"),'
# )

def index(request):
    # return HttpResponse("Hello world! You are running docker-compose!")
    # first = Employee.objects.create(empid='987654',empname='banana',email='banana987654@hello.com')
    results = Employee.objects.all()
    if results.exists():
        data = {"results":results}
        return render(request, "index.html", data)
    else:
        return HttpResponse('The Query Set is empty')


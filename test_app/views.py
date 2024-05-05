from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, "test_app/test.html", {'author': "Himanshu Mamgain"})
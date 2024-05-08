from django.shortcuts import render

# Create your views here.
def my_story(request):
    context = {
        'message': "Hello, hello!",
    }

    return render(request, 'index.html', context)

from django.shortcuts import render

# Create your views here.

def resumes(request):
    return render(request, 'resumes/resumes.html')

def resume(request, slug):
    context = {
        'slug':slug
    }
    return render(request, 'resumes/resume.html', context)

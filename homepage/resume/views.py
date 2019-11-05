from django.shortcuts import render, render_to_response

# Create your views here.
def resume(response):
    ''' render the resume page '''
    context = {
        # 'script': script,
        # 'div': div,
    }
    return render_to_response('resume/resume.html', context=context)


def projects(response):
    ''' render the projects page '''
    context = {
        # 'script': script,
        # 'div': div,
    }
    return render_to_response('resume/projects.html', context=context)


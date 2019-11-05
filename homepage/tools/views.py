from django.shortcuts import render, render_to_response

# Create your views here.
def tools(response):
    ''' render the tools page '''
    context = {
        # 'script': script,
        # 'div': div,
    }
    return render_to_response('tools/tools.html', context=context)

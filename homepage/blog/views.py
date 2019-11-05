from django.shortcuts import render, render_to_response

# Create your views here.
def blog(response):
    ''' render the blog page '''
    context = {
        # 'script': script,
        # 'div': div,
    }
    return render_to_response('blog/blog.html', context=context)

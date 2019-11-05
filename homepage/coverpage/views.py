from django.shortcuts import render, render_to_response
# Create your views here.
def cover(request):
    ''' render the cover page. '''
    

    # Make our context dict
    context = {
        
    }
    return render_to_response('coverpage/cover.html', context=context)

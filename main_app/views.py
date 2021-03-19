from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Cat Collector</h1>')
    return render(request, 'home.html')

def about(request):
    # lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam a lorem non elit interdum congue ut vitae nibh. Nam maximus laoreet dui, hendrerit auctor ex convallis faucibus. Morbi posuere id nulla vitae facilisis. Morbi fermentum libero in varius malesuada. Cras condimentum lobortis neque, eu auctor dolor interdum quis. Nulla nec facilisis ante, vel efficitur nibh. Quisque venenatis augue condimentum nisi mollis rhoncus sit amet et leo.Sed eget ornare neque. Morbi pulvinar ante vitae tellus hendrerit mollis. Nullam ut gravida nulla. Donec sed dolor ligula. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Pellentesque varius risus et dui lacinia, aliquet finibus est eleifend. Ut consequat dictum lacus in elementum. Nullam pretium varius maximus. Aliquam finibus aliquet diam, quis maximus diam sollicitudin vitae. Suspendisse sed suscipit est.'
    # return HttpResponse(lorem_ipsum)
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
from django.shortcuts import render

# Create y
def post_list(request):
    return render(request, 'blog/post_list.html', {})

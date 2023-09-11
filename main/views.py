from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Muhammad Fakhri Robbani',
        'NPM' : 2206026252,
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
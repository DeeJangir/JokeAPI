from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import DareText
from .models import JokeText
from .models import QuotesText
from random import randint
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms_add import SignUpForm

def index(requests):
    data = DareText.objects.all()
    data_tag = data[randint(0, data.count()-1)]
    stu = {
        "dare_line": data_tag.share_text,
        "dare_id": data_tag.share_id
    }
    # return render(requests, "index.html/", stu)
    return redirect('/dare/'+str(data_tag.share_id), stu)


def new_joke_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            joke_text = form.cleaned_data.get('joke_text')
            joke_id = form.cleaned_data.get('joke_id')
            data = JokeText(joke_text=joke_text, joke_id=joke_id)
            data.save()
            return redirect('/n/')
    else:
        form = SignUpForm()
    return render(request, 'new_data_add.html', {'form': form})


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             joke_text = form.cleaned_data.get('joke_text')
#             joke_id = form.cleaned_data.get('joke_id')
#             data = JokeText(joke_text=joke_text, joke_id=joke_id)
#             data.save()
#             return redirect('/n/')
#     else:
#         form = SignUpForm()
#     return render(request, 'new_data_add.html', {'form': form})
#
#     # stu = SignUpForm()
#     # return render(request, "new_data_add.html", {'form': stu})


def dare_slug(requests, slug):
    data_tag = DareText.objects.filter(share_id=slug)
    stu = {
        "dare_line": data_tag[0].share_text,
        "dare_id": data_tag[0].share_id
    }
    return render(requests, "index.html", stu)


def jokes(requests):
    data = JokeText.objects.all()
    data_tag = data[randint(0, data.count() - 1)]
    stu = {
        "dare_line": data_tag.joke_text,
        "dare_id": data_tag.joke_id
    }
    return redirect('/jokes/' + str(data_tag.joke_id), stu)


def jokes_slug(requests, slug):
    data_tag = JokeText.objects.filter(joke_id=slug)
    stu = {
        "dare_line": data_tag[0].joke_text,
        "dare_id": data_tag[0].joke_id
    }
    return render(requests, "index.html", stu)


def quotes(requests):
    data = QuotesText.objects.all()
    data_tag = data[randint(0, data.count() - 1)]
    stu = {
        "dare_line": data_tag.quotes_text,
        "dare_id": data_tag.quotes_id
    }
    return redirect('/quotes/' + str(data_tag.quotes_id), stu)


def quotes_slug(requests, slug):
    data_tag = QuotesText.objects.filter(quotes_id=slug)
    stu = {
        "dare_line": data_tag[0].quotes_text,
        "dare_id": data_tag[0].quotes_id
    }
    return render(requests, "index.html", stu)


def get_url_change(request, page_type, slug):
    if page_type == "dare":
        return index(request)
    elif page_type == "quotes":
        return quotes(request)
    elif page_type == "jokes":
        return jokes(request)
    else:
        return index(request)


def handler404(request):
    response = render_to_response(
        '400.html',
        context_instance=RequestContext(request)
    )

    response.status_code = 400

    return response


def handler500(request):
    response = render_to_response(
        '500.html',
        context_instance=RequestContext(request)
    )
    response.status_code = 500

    return response

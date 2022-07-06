from multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from app_one.models import Show
from django.contrib import messages

#add the errors dic when ever you create or update 
#get => render , post => redirect
def viewShows(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "allShows.html", context)


def viewAddShow(request):
    return render(request, "addShow.html")


def addShow(request):
    if request.method == "POST":
     # pass the post data to the method we wrote and save the response in a variable called errors
        errors = Show.objects.basic_validator(request.POST)
            # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect("/shows/new")
        else: 
            # no errors cont.
            title = request.POST["title"]
            network = request.POST["network"]
            release_date = request.POST["releaseDate"]
            desc = request.POST["description"]

            show = Show.objects.create(
            title=title, network=network, release_date=release_date, desc=desc)

            # showId = show.id
            # # add , then redirect to /shows/<id>
            # context = {
            #         "show": Show.objects.get(id=showId)
            #     }
            #return render(request, 'readShow.html', context)
            return redirect(f"/shows/{show.id}")
    return redirect(f"/shows/{show.id}")


def updateShow(request, showId):
    show = Show.objects.get(id=showId)
    if request.method == "POST":
     # pass current instance to the validator
        errors = Show.objects.basic_validator(request.POST,show)
            # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect(f"/shows/{showId}/edit")
        else:
            #no errors cont.
            title = request.POST["title"]
            network = request.POST["network"]
            release_date = request.POST["releaseDate"]
            desc = request.POST["description"]
            #update using the show that has the current instance
            show.title = title
            show.network = network
            show.release_date=release_date
            show.desc=desc
            show.save()
            
            return redirect(f"/shows/{showId}")

    return redirect(f"/shows/{showId}")


def viewUpdateShow(request, showId):

    context = {
        "show": Show.objects.get(id=showId)
    }

    return render(request, "editShow.html", context)

# receive the id from url 
def viewShow(request, showId):

    context = {
        "show": Show.objects.get(id=showId)
    }
    return render(request, "readShow.html", context)

#delete post request
def deleteShow(request, showId):
    Show.objects.get(id=showId).delete()
    
    return redirect('/')

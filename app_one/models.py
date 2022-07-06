from datetime import datetime, timezone
from turtle import title
from django.db import models

import re  # the regex module
# 1.create anager class
# 2.create basic_validator function
# 3. create errore dic to store all errors
# 4.return the dic
# 5.call the manager in the other class to use it (like invoke a function to access it !)


class ShowManager(models.Manager):
    #3rd params is the current instance 
    def basic_validator(self, postData, show=None):
        # add keys and values to errors dictionary for each invalid field
        errors = {}

        # if title is empty
        if not postData["title"]:
            errors["title"] = "Please enter Show title"
        elif len(postData['title']) < 2:
            errors["title"] = "show title should be at least 2 characters"
        else:
            # if titlt is not empty , and the this.title is modified
            if show is None or show.title != postData["title"]:
                # check the duplication in DB
                if Show.objects.filter(title=postData["title"]).exists():
                    errors["title"] = "show title is already exist"

        if len(postData['network']) < 3:
            errors["network"] = "network name should be at least 3 characters"
        if postData["description"]:
            if len(postData['description']) < 10:
                errors["description"] = "show description should be at least 10 characters"
        if not postData["releaseDate"]:
            errors["releaseDate"] = "Please enter the Show release date"
        elif postData["releaseDate"] > str(datetime.now()):
            errors["releaseDate"] = "date cannot be later than today"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=60)
    network = models.CharField(max_length=30)
    release_date = models.DateField(blank=True, null=True)
    desc = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()
#Show.objects.create(title ="Stranger Things",network="Netflix",release_date="2016-2-16")

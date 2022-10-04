from django.db import models

STATE_CHOICE = ((
    ('Delhi', 'Delhi'),
    ('Mumbai', 'Mumbai'),
    ('Jaipur', 'Jaipur'),
    ('Kanpur', 'Kanpur'),
    ('Bhopal', 'Bhopal'),
))

class Profile(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE, max_length=20)
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    pimage = models.ImageField(upload_to='pimages', blank=True )
    rdoc = models.FileField(upload_to='rdocs', blank=True )

import os
from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.
class Achievements(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    image_id = models.IntegerField(null=True, blank=True)
    achievements = models.ManyToManyField(Achievements, blank=True)
    badges = models.ManyToManyField(Badge, blank=True)
    assessment_count = models.IntegerField(default=0)
    assessment_streak = models.IntegerField(default=0,null=True,blank=True)
    distance_traveled = models.IntegerField(default=0,null=True,blank=True)
    achievements_completed = models.IntegerField(default=0,null=True,blank=True)
    badges_earned = models.IntegerField(default=0,null=True,blank=True)
    mistery_boxes_earned = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return f'{self.username} ({self.email})'

    def get_formatted_phone_number(self):
        # Format the phone number as desired
        return f"{self.phone_number[:3]}-{self.phone_number[3:6]}-{self.phone_number[6:]}"

        
class BikeRackData(models.Model):
    the_geom = models.CharField(max_length=255)
    BoroCode = models.IntegerField()
    BoroName = models.CharField(max_length=50)
    BoroCD = models.IntegerField()
    CounDist = models.IntegerField()
    AssemDist = models.IntegerField()
    StSenDist = models.IntegerField()
    CongDist = models.IntegerField()
    Program = models.CharField(max_length=50)
    Site_ID = models.CharField(max_length=50)
    Group_ID = models.CharField(max_length=50)
    Borough = models.CharField(max_length=50)
    IFOAddress = models.CharField(max_length=100)
    OnStreet = models.CharField(max_length=100)
    FromStreet = models.CharField(max_length=100)
    ToStreet = models.CharField(max_length=100)
    Side_of_St = models.CharField(max_length=1)
    RackType = models.CharField(max_length=50)
    Date_Inst = models.DateField(null=True)
    X = models.FloatField()
    Y = models.FloatField()
    NTAName = models.CharField(max_length=100)
    FEMAFldz = models.CharField(max_length=50)
    FEMAFldT = models.CharField(max_length=50)
    HrcEvac = models.IntegerField(null=True, blank=True)
    Condition = models.CharField(max_length=50, null=True, blank=True)
    Updated_by = models.CharField(max_length=50, null=True, blank=True)
    Notes = models.CharField(max_length=120, null=True, blank=True)


    def __str__(self):
        return f"{self.Site_ID} - {self.IFOAddress}"

# class UserBadge(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
#     awarded_at = models.DateTimeField(auto_now_add=True)





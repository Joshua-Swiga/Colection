from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.room_name
    
class Messages (models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # This essentially means that if a room gets deleted, all the messages in that room will be deleted as well. 
    sender = models.CharField(max_length=225)
    messages = models.TextField()

    def __str__(self) -> str:
        return str(self.room)
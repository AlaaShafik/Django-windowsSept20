from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.song_title + ' - ' + self.file_type

class Picture(models.Model):
    photographer = models.CharField(max_length=250)
    pic_title = models.CharField(max_length=500)
    pic_type = models.CharField(max_length=100)
    pic_logo = models.CharField(max_length=1000)


    def __str__(self):
        return self.pic_title + ' - ' + self.pic_type


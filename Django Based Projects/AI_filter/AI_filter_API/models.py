from django.db import models

class HomePageContent(models.Model):
    burner_image = models.ImageField(upload_to='homepage/images', null=True, blank=True)
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title

class AboutPageContent(models.Model):
    burner_image = models.ImageField(upload_to='aboutpage/images', null=True, blank=True)
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

class ContactPageContent(models.Model):
    burner_image = models.ImageField(upload_to='contactpage/images', null=True, blank=True)
    title = models.CharField(max_length=300, blank=True)
    description = models.CharField(max_length=300, blank=True)
    paragraph = models.TextField()

    def __str__(self) -> str:
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    #subtitle = models.CharField(max_length=300, blank=True, null=True) # Provide a default subtitle phrase
    posted_by = models.CharField(max_length=100, default="Well Edited!")
    date = models.DateTimeField(auto_now=True, blank=True, null=True)
    content = models.TextField()

    def __str__(self) -> str:
        return f'{self.title}: \n{self.subtitle}'

class UserQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self) -> str:
        return f'{self.name}: {self.message}'

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
job_tybe =(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def img_upload(instance,filename):
    imagename , extension = filename.split(".")

    return "jobs/%s/%s.%s"%(instance.id,instance.id,extension)




class Job(models.Model):
    owner = models.ForeignKey(User,related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_tybe = models.CharField(max_length=15,choices=job_tybe)
    Description = models.TextField(max_length=1000)
    published_at= models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience= models.IntegerField(default=1)
    Catogery = models.ForeignKey('Catogery',on_delete=models.CASCADE)
    img = models.ImageField(upload_to=img_upload)

    slug=models.SlugField(null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
   

class Catogery(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey("job.Job",related_name='apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
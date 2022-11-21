from django.db import models

# Create your models here.
class JobPost(models.Model):
    jobtitle = models.CharField("Job Title", max_length =150)
    jobdescription = models.TextField ("Job Description", blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #company = models.ForeignKey('Company', on_delete = models.PROTECT,null=True , verbose_name = "published by company")
    companyprofile = models.TextField(blank=True)
    #logo = models.ImageField(upload_to = 'logo', blank = True)
    is_published  = models.BooleanField(default=True)
    category = models.ForeignKey('category', on_delete = models.PROTECT,null=True)

    def __str__(self):
        return self.jobtitle

class Category(models.Model):
    title = models.CharField(max_length = 150, db_index = True)

    def __str__(self):
        return self.title


class Company(models.Model):
    company_name = models.CharField("Company name", max_length =150)
    company_profile = models.TextField ("Company profile", blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
    
    

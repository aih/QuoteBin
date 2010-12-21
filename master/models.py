from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import hashlib
def hash(id):
    h = hashlib.new('ripemd160')
    h.update(str(id))
    return h.hexdigest()
# Create your models here.
DOC_CHOICES = (
		('NT', 'Note'),
                ('CO', 'Court Opinion'),
                ('ST', 'Statute'),
                ('RL', 'Regulation'),
                ('MM', 'Memo'),
                ('BR', 'Brief'),
                ('JO', 'Journal'),
                ('AR', 'Article'),
                ('WS', 'Website'),
                ('OT', 'Other'),
)

class Quote(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    link = models.CharField(max_length=255, blank = True, null=True)
    text = models.TextField()
    group = models.ForeignKey('EmailCode', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    doc_type = models.CharField(max_length=2, choices=DOC_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now = True)
    references = models.ManyToManyField("Reference")
    is_public = models.BooleanField()

    def save(self, force_insert=False, force_update=False):
        super(Quote, self).save(force_update=force_update, force_insert=force_insert)
        self.link = hash(self.id)
        super(Quote, self).save(force_update=True, force_insert=False)
        
class Reference(models.Model):
    url = models.URLField(blank=True, null=True)
    text = models.CharField(max_length=255,blank=True, null=True)

class EmailCode(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=100, unique = True)
    
class Tag(models.Model):
    text = models.CharField(max_length=100)
    quote = models.ForeignKey('Quote')

class QuoteBin(models.Model):
    user = models.ForeignKey(User)
    name = models.TextField()
    quote = models.ManyToManyField('Quote')

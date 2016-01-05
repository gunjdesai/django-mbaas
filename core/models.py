from __future__ import unicode_literals

from django.db import models
from hashlib import sha1
from mongoengine.document import Document
import uuid
import hmac
from mongoengine.fields import StringField, DateTimeField, LongField
from mongoengine.connection import connect
from datetime import datetime


connect("default_mbaas")
# Create your models here.
class App(Document):
    name = StringField(max_length=20, unique=True)
    key = StringField(max_length=40)
    created = DateTimeField()

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
            
        if not self.created:
            self.created = datetime.now()
            
        return super(App, self).save(*args, **kwargs)

    def generate_key(self):
        unique = uuid.uuid4()
        return hmac.new(unique.bytes, digestmod=sha1).hexdigest() 
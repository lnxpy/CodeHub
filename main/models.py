from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _

from django.urls import reverse
from django_jalali.db import models as jmodels

from account.models import User

from .constants import LANGUAGES, VERIFICATIONS
from .utils import generateUID


class Snippet(models.Model):

    id = models.CharField(
        verbose_name='ID',
        max_length=11,
        primary_key=True,
        editable=False,
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=50,
        default='',
    )
    description = models.TextField(
        verbose_name=_('Description'),
        blank=True
    )
    body = models.TextField(
        verbose_name=_('Script'),
    )
    lang = models.CharField(
        verbose_name=_('Programming Language'),
        max_length=250,
        choices=LANGUAGES,
    )
    created_on = jmodels.jDateTimeField(
        auto_now=True,
        editable=False,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
    )

    # TODO: Adding a view counter using django-hitcount pkg

    class Meta:
        indexes = [models.Index(fields=['id'])]

    def __str__(self): return self.title

    # TODO: Implementing get_absolute_url method

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generateUID(Snippet)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('snippet', args=[str(self.id)])


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
    )
    description = models.CharField(
        max_length=150,
    )
    created_on = jmodels.jDateTimeField(
        auto_now=True,
        editable=False,
    )

    def __str__(self): return self.name


class Ticket(models.Model):
    id = models.CharField(
        verbose_name='ID',
        max_length=11,
        primary_key=True,
        editable=False,
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=150,
    )
    description = models.TextField(
        verbose_name=_('Description')
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name=_('Tags'),
    )
    slug = models.SlugField(
        editable=False,
    )
    is_valid = models.CharField(
        verbose_name=_('Validation'),
        choices=VERIFICATIONS,
        default='pending',
        max_length=20,
    )
    created_on = jmodels.jDateTimeField(
        auto_now=True,
        editable=False,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        #        editable=False,
        null=True,
    )

    # TODO: Adding a view counter using django-hitcount pkg

    def __str__(self): return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)

        if not self.id:
            self.id = generateUID(Ticket)

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ticket', args=[str(self.id), str(self.slug)])


class Comment(models.Model):
    body = models.CharField(
        verbose_name=_('Comment Body'),
        max_length=250,
    )
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
    )
    created_on = jmodels.jDateTimeField(
        auto_now=True,
        editable=False,
    )

    def __str__(self):
        return f'{self.created_by} on {self.ticket}'

    def get_absolute_url(self):
        return reverse('ticket', args=[str(self.ticket.id), str(self.ticket.slug)])


class Event(models.Model):
    title = models.CharField(
        max_length=150,
    )
    body = models.TextField(blank=True)
    created_on = jmodels.jDateTimeField(
        auto_now=True,
        editable=False,
    )

    def __str__(self):
        return self.title

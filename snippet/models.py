from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
import jdatetime
from ckeditor.fields import RichTextField

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
COLOR_THEME = [
    ('suggest1','قرمز صورتی'),
    ('suggest2','قرمز زرد'),
    ('suggest3','زرد آبی'),
    ('suggest4','صورتی آبی ملایم'),
]

class Snippet(models.Model):
    SID = models.CharField(max_length=10, verbose_name='شناسه')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    detail = models.TextField(blank=True, verbose_name='توضیحات')
    script = models.TextField(verbose_name='اسکریپت')
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100, verbose_name='زبان برنامه نویسی')
    pub_date = models.CharField(max_length=50, verbose_name='تاریخ ثبت')
    link = models.URLField(verbose_name='آدرس')

    def __str__(self):
        return '%s ~~ %s ~~ %s'%(self.SID, self.title, self.pub_date)

class Suggest(models.Model):
    title = models.CharField(max_length=30, verbose_name='عنوان')
    content = RichTextField(verbose_name='محتوا')
    theme = models.CharField(choices=COLOR_THEME, max_length=100, verbose_name='نگارش', default='suggest1')

    def __str__(self):
        return self.title

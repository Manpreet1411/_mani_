import datetime
from django.template.defaulttags import register
from myapp.models import  Category

@register.filter(name="times")
def times(number):
    return range(number)

@register.filter(name="times")
def times(number):
    return range(number)

@register.simple_tag()
def currentdatetime():
    return datetime.datetime.now()

@register.inclusion_tag("fetchcategories.html")
def fetch_categories():
    categoriesdata=Category.objects.all()
    return {"categorydata":categoriesdata}

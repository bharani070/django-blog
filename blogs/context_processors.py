from .models import Category
from socialLinks.models import SocialLink

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_socialLinks(request):
    links = SocialLink.objects.all()
    return dict(links=links)
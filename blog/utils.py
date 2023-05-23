import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """Generate random string to be apppended to slug if the slug queried already exists"""
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance):
    """Generate a unique slug based on post title"""
    slug = slugify(instance.title)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        random_str = random_string_generator(size=4)
        slug = f"{slug}-{random_str}"

    return slug

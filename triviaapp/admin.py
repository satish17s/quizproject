from django.contrib import admin
from .models import Trivia, Option, Player

# Register your models here.
admin.site.register(Trivia)
admin.site.register(Option)
admin.site.register(Player)

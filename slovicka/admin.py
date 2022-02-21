from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import Cvicenie, Slovicko, Pokus, Odpoved

class SlovickoInLine(admin.StackedInline):
    model = Slovicko
    extra = 0
class CvicenieAdmin(admin.ModelAdmin):
    inlines = [SlovickoInLine]

class OdpovedInLine(admin.TabularInline):
    model = Odpoved
    fields = ['spravne', 'odpoved', 'jespravne']
    extra = 0

class PokusAdmin(admin.ModelAdmin):
    inlines = [OdpovedInLine]

class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('username', 'password1', 'password2', 'groups',)}
         ),

    )

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

admin.site.register(Cvicenie, CvicenieAdmin)
admin.site.register(Pokus, PokusAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from .models import *




class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name' , 'last_name',  'user_type', )


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    prepopulated_fields = {'username': ('first_name' , 'last_name', )}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'user_type', 'password1', 'password2', ),
        }),
    )

class ScienceAdmin(admin.ModelAdmin):
    list_display = ('__str__','ret_sem',)


admin.site.register(Science, ScienceAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Mark)




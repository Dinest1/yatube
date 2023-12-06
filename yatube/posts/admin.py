from django.contrib import admin
from .models import Post, CD, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'group', 'author')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    save_as = True


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')


class CDAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'artist', 'genre')
    list_filter = ('date', 'genre')


admin.site.register(Post, PostAdmin)
admin.site.register(CD, CDAdmin)
admin.site.register(Group, GroupAdmin)





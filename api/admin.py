from django.contrib import admin
from django import forms
from api.models import Blog, BlogPost, Author


class BlogForm(forms.ModelForm):
	body = forms.CharField( widget=forms.Textarea )

	class Meta:
		model = BlogPost

class BlogPostAdmin(admin.ModelAdmin):
	form = BlogForm


admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(BlogPost, BlogPostAdmin)
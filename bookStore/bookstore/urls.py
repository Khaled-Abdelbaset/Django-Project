"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from books.views import book_details, books_home, contact_us, about_us, books_index, book_show, book_delete, book_create, book_update, book_create_forms, book_edit_forms
from categories.views import create_category, category_index, editCategory, categoryDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<int:id>', book_details, name="detailspage"),
    path('home/', books_home, name="home"),
    path('homedatabase/', books_index, name="homedatabase"),
    path('homedatabase/<int:id>', book_show, name="detailsdatabase"),
    path('homedatabase/createform', book_create_forms, name="book.create.forms"),
    path('homedatabase/updateform/<int:id>', book_edit_forms, name="book.update.forms"),
    path('homedatabase/delete/<int:id>', book_delete, name="delete"),
    
    path('homedatabase/category', category_index, name='categoryIndex'),
    path('homedatabase/category/create', create_category, name='createCategory'),
    path('homedatabase/category/edit/<int:id>', editCategory, name='editCategory'),
    path('homedatabase/category/delete/<int:id>', categoryDelete, name='categoryDelete'),

    path('contactus/', contact_us, name="contactpage"),
    path('aboutus/', about_us, name="aboutpage"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

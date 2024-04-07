from django.shortcuts import render, reverse, redirect,get_object_or_404
from categories.forms import CategoryModelForm
from categories.models import Category
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_category(request):
  form= CategoryModelForm()
  if request.method == "POST":
    form = CategoryModelForm(request.POST)
    if form.is_valid():
      form.save()
      url =  reverse("categoryIndex")
      return redirect(url)
  return render(request,'categories/create.html',{'form':form})

@login_required
def category_index(request):
  categories=Category.get_all_categories()
  return render(request,'categories/index.html',{'categories':categories})

@login_required
def editCategory(req,id):
  category=Category.get_category_by_id(id)
  form=CategoryModelForm(instance=category)
  if req.method=="POST":
    form = CategoryModelForm(req.POST,instance=category)
    if form.is_valid():
      form.save()
      url =reverse("categoryIndex")
      return redirect(url)
  return render(req,'categories/edit.html',{'form':form})

@login_required
def categoryDelete(req,id):
  category=get_object_or_404(Category,pk=id)
  category.delete()
  url =reverse("categoryIndex")
  return redirect(url)
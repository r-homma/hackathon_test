from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView#class,djangoの標準ビュー,modelを単純にHTMLに表示させることができる
from django.http import HttpResponse
from .models import BlogModel#model
from django.urls import reverse_lazy

# Create your views here.
class BlogList(ListView):#BlogListがListViewclassを継承している
    template_name = 'list.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel#ユーザーが入力した情報をmodelテーブルに保存しているイメージ
    fields = ('title', 'question', 'answer', 'category')#create.htmlで表示させる項目を記載している
    success_url = reverse_lazy('list')#urls.pyの引数nameと紐づいている

class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class BlogUpdate(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title', 'question', 'answer', 'category')
    success_url = reverse_lazy('list')

class BlogChallenge(DetailView):
    template_name = 'challenge.html'
    model = BlogModel

def Hantei(request, pk):
    if request.method == 'POST':
        kaitouview = request.POST['kaitou']
        answerobject = BlogModel.objects.get(pk=pk)
        if kaitouview == answerobject.answer:
            return redirect('list')
        else:
            return redirect('fuseikai')

class BlogSeikai(DetailView):
    template_name = 'seikai.html'
    model = BlogModel
    
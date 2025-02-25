from django.shortcuts import render
from .models import Author,Article
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseNotFound

#------------------------------------------------------------------------------------
def show_articles(request):
    articles=Article.objects.all()
    articles_authors=Article.author.through.objects.all()
    authors=Author.objects.all()
    context={
        'articles':articles,
        'articles_authors':articles_authors,
        'authors':authors,
        'media_url':settings.MEDIA_URL
    }
    return render(request, 'articles_app/blog.html',context)

#------------------------------------------------------------------------------------
def show_blog_details(request,slug):
    article=Article.objects.get(slug=slug)
    image_List=os.listdir(settings.MEDIA_ROOT+'/images/articles/article_'+str(article.id))
    article.view_number+=1
    article.save()
    articles_authors=Article.objects.get(id=article.id).author.through.objects.all()
    authors=Author.objects.all()
    context={
        'article':article,
        'articles_authors':articles_authors,
        'authors':authors,
        'media_url':settings.MEDIA_URL,
        'image_List':image_List,
        # 'article.view_number':article.view_number,
    }
    return render(request, 'articles_app/blog_details.html',context)

#------------------------------------------------------------------------------------
def show_article_pdf(request,article_id):
    fs= FileSystemStorage()
    filename= 'article_'+str(article_id)+'.pdf'
    file_path= "pdf_files/"+filename
    if fs.exists(file_path):
        with fs.open(file_path) as pdf:
            response=HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition']="inline; filename="+filename
            return response
    else:
        return HttpResponseNotFound('The requested pdf file was not found in our server')

#------------------------------------------------------------------------------------
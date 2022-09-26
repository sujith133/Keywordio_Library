from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from KeywordioLib.forms import Signupform, loginform, book
from KeywordioLib.models import logins,book

def index(request):
    return HttpResponse("Hello Sujith!")

def Home(request):
  template = loader.get_template('homePage.html')
  return HttpResponse(template.render())

def Admin(request):
  if request.method == "POST":
    context=book.objects.all()
    if(request.POST.get('create')=='create'):
      print(request.POST.get('create'))
      return render(request, 'create.html')
    elif(request.POST.get('read')=='read'):
      print(request.POST.get('read'))
      return render(request, 'read.html',{'list':context})
    elif(request.POST.get('update')=='update'):
      print(request.POST.get('update'))
      return render(request, 'update.html')
    elif(request.POST.get('delete')=='delete'):
      print(request.POST.get('delete'))
      return render(request, 'delete.html')


def loginsignup(request):
  form=loginform()
  if request.method == "POST":
    print(request.POST)
    if(request.POST.get('login')=='login'):
      password=request.POST.get('password')
      email=request.POST.get('useremail')
      i=0
      for s in logins.objects.all():
        print(s.useremail+"   "+s.password)
        print(email+"   "+password)
        if(s.useremail==email and s.password==password):
          i=1
          break
      if(i==1):
        #return HttpResponse("Hello Sujith!")
        return render(request, 'AdminView.html')
      else:
        print("invalid credentials")
        context = {'form':form}
        return render(request, 'SignuporLogin.html', context)
    if(request.POST.get('StudentView')=='StudentView'):
      context=book.objects.all()
      print(request.POST.get('StudentView'))
      return render(request, 'StudentView.html',{'list':context})
    


def signup(request):
  form=Signupform()
  if request.method == "POST":
    print(request.POST)
    user_name=request.POST.get('username')
    user_password=request.POST.get('password')
    user_email=request.POST.get('useremail')
    i=0
    for s in logins.objects.all():
      if(s.useremail==user_email):
        i=1
        break
    
    if(i==0):
      print("data entered")
      record=logins(username=user_name , password=user_password , useremail=user_email)
      record.save()
      print("data entered")
    else:
      print("email already registered")

    
  context = {'form':form}
  return render(request, 'SignuporLogin.html', context)



def create(request):
  form=book()
  if request.method == "POST":
    print(request.POST)
    Bookid=int(request.POST.get('BookId'))
    Bookname=request.POST.get('BookName')
    Bookstatus=request.POST.get('BookStatus')
    i=0
    for s in book.objects.all():
      print(type(s.BookId),type(Bookid))
      print(s.BookName,Bookname)
      if(s.BookId==Bookid or s.BookName==Bookname):
        i=1
        break
    
    if(i==0):
      print("data entered")
      record=book(BookId=Bookid , BookName=Bookname , BookStatus=Bookstatus)
      record.save()
      print("data entered")
    else:
      print("Book already registered")

    
  context = {'form':form}
  return render(request, 'create.html', context)


def delete(request):
  form=book()
  if request.method == "POST":
    print(request.POST)
    Bookid=int(request.POST.get('BookId'))
    Bookname=request.POST.get('BookName')
    Bookstatus=request.POST.get('BookStatus')
    i=0
    for s in book.objects.all():
      if(s.BookId==Bookid and s.BookName==Bookname):
        s.delete()  
        i=1
        
        break
    
    if(i==0):
      print("records not found")
    else:
      print('records deleted')

  
  context = {'form':form}
  return render(request, 'delete.html', context)

def update(request):
  form=book()
  if request.method == "POST":
    print(request.POST)
    Bookid=int(request.POST.get('BookId'))
    Bookname=request.POST.get('BookName')
    Bookstatus=request.POST.get('BookStatus')
    i=0
    for s in book.objects.all():
      if(s.BookId==Bookid):
        
        s.BookName=Bookname
        s.BookStatus=Bookstatus
        s.save()
        print("data updated")

        i=1
        break
    
    if(i==0):
      print("Book not registered")

    
  context = {'form':form}
  return render(request, 'update.html', context)

def read(request):
  form=book()
  if request.method == "POST":
    print(request.POST)
    Bookid=request.POST.get('Bookid')
    Bookname=request.POST.get('Bookname')
    Bookstatus=request.POST.get('Bookstatus')
    
  context = {'form':form}
  return render(request, 'read.html', context)

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from AdminApp.models import Book,Category,Accounts,OrderMaster
from UserApp.models import userinfo,mycart
from .MySerializer import ProductSerializers
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import  APIView
from rest_framework.response import Response

# Create your views here.
def Mainpage(request):
    cats=Category.objects.all()
    book=Book.objects.all()
    return render(request,"Mainpage.html",{"cats":cats,"book":book})

def Viewdetails(request,id):
    cats=Category.objects.all()
    book=Book.objects.get(id=id)
    return render(request,"Viewdetails.html",{"cats":cats,"book":book})

def login(request):
    if(request.method == "GET"):
        return render(request,"login.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            user = userinfo.objects.get(username=uname,password=pwd)
        except:
            #return HttpResponse("User not present")
            return redirect(login)
        else:
            request.session["uname"]=uname
            return redirect(Mainpage)


def signup(request):
    if(request.method == "GET"):
        return render(request,"signup.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        email = request.POST["email"]
        try:
            user = userinfo.objects.get(username=uname)            
        except:
            #return HttpResponse("User not present")
            user = userinfo(uname,pwd,email)
            user.save()
            return redirect(Mainpage)
        else:
            return redirect(login)

def logout(request):
    request.session.clear()
    return redirect(Homepage)

def addtocart(request):
    if(request.method == "POST"):
        if("uname" in request.session):                    
            bid = request.POST["bid"]
            qty = request.POST["qty"]
            uname = request.session["uname"]
            item = mycart()
            item.user = userinfo.objects.get(username = uname)
            item.book = Book.objects.get(id=bid)
            item.qty = qty
            item.save()
            return redirect(showcart)
        else:
            return redirect(login)

def showcart(request):
    cats=Category.objects.all()
    items=mycart.objects.filter(user=request.session["uname"])
    total = 0 
    for item in items:
        total += item.qty * item.book.price

    request.session["total"] = total
    return render(request,"showcart.html",{"items":items,"cats":cats})


def modifycart(request):
    action=request.POST["action"]
    bid=request.POST["bid"]
    item=mycart.objects.get(user=request.session["uname"],Book=bid)
    if(action=="Remove"):
        item.delete()
    else:
        item.qty=request.POST["qty"]
        item.save()
    return redirect(showcart)

def showcakes(request,id):
    cat = Category.objects.get(id=id)
    book = Book.objects.filter(cat_fk = id)
    cats = Category.objects.all()
    return render(request,"Mainpage.html",{"book":book,"cats":cats,"cat":cat})


def makepayment(request):
    if(request.method == "GET"):
        return render(request,"makepayment.html",{})
    else:
        cardno = request.POST["cardno"]
        cvv  = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = Accounts.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)
        except:
            return redirect(makepayment)
        else:
            owner = Accounts.objects.get(cardno='222',cvv='222',expiry='12/2030')
            amount = request.session["total"]
            buyer.balance -= amount
            owner.balance +=amount
            buyer.save()
            owner.save()
            #delete all items from cart
            items = mycart.objects.filter(user = request.session["uname"])
            order = OrderMaster()
            order.user = userinfo.objects.get(username = request.session["uname"])
            order.amount = request.session["total"]
            details = []

def search(request):
    query = request.GET.get('q', '') 


    book = Book.objects.filter(Book_name__icontains=query).first()
    search = Book.objects.filter(Book_name__icontains=query)

    return render(request, 'search.html', {'book': book, 'search_results': search, 'query': query})

"""----------------------USING REST API------------------------------"""
class ProductDetails(APIView):    
    def get(self,request,id):
        try:
            prd = Book.objects.get(id=id)     
            serializers = ProductSerializers(prd)
            return Response(serializers.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):
        try:
            prd = Book.objects.get(id=id)     
            prd.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id):
        try:
            prd = Book.objects.get(id=id)     
            #prd is original data
            #request.data is the new modified data
            serializer = ProductSerializers(prd,data=request.data)
            if(serializer.is_valid()):
                serializer.save()
            return Response(serializer.data)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProductList(APIView):      
    def get(self,request) :
        #select * from Product
        prds = Book.objects.all()  #binary format
        serializers = ProductSerializers(prds,many=True)
        return Response(serializers.data)

    def post(self,request):        
        serializer = ProductSerializers(data=request.data)
        if(serializer.is_valid()):
            #Store in database
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


        
     

    

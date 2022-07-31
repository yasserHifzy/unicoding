from ninja import NinjaAPI
from ninja import Router
from django.shortcuts import get_object_or_404
from subacount.models import Account,AccountTyoeChoices,JournalEntery
from subacount.schema import AccountOut,FourOfourOut
from subacount.models import *
from typing import List
from django.db.models import Sum

api = NinjaAPI(

    title="Accounting for All",
    description="This My (Account) ",
    version="3.0.2",
)

router_api=Router()
from ninja.security import HttpBearer


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "yasser":
            return token

@router_api.get("/list_all",response=List[AccountOut],auth=AuthBearer())#هنا استخدمنة اليست حتى يرجع مجموعة بالكامل 
def add1(request):
    print(request.auth)
    return Account.objects.order_by("fullcode")

@router_api.get("/list_one /",response= {
    200:AccountOut,
    404:FourOfourOut
     })
def add2(request,account_id:int ):
    try :
        acconut=Account.objects.get(id=account_id)
        return acconut
    except Account.DoesNotExist:
        return  404,{"detail" : f" Account with id  {account_id} does  not exist"}

@router_api.get("/get_accont_type/")
def get_accont_type(request):
    return AccountTyoeChoices.choices

@router_api.get("ccont_balance/{account_id}")
def get_account_balance(request,account_id : int):
    account=get_object_or_404(Account,id=account_id)
    jes=JournalEntery.objects.filter(account=account)
    balance=jes.values("currency").annotate(sum=Sum("amount")).order_by()
    return 200,{"account":account.name,"balance":list(balance)}
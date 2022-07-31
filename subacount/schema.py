from decimal import Decimal
from ninja import Schema

class FourOfourOut(Schema):
        detail:str


class AccountOut(Schema):
        id : int
        parant : "AccountOut" = None 
        code : str 
        name : str 
        type : str 
        fullcode :str 

class AjounelE(Schema):
        account : int
        transaction_id : int 
        amount : Decimal
        currency : str 
class AjounelEOut(AjounelE):
       id : int

class AjounelEin(AjounelE):
        pass
class jet(Schema):
        account_creater : int 
        account_dibter :int 
        amount: Decimal
        currency : str


class TransactionIn(Schema):
    type:str
    discription : str
    je : jet




"""
from ninja import ModelSchema
from subacount.models import Account

class AccountOut(ModelSchema):
    class Config :
        model = Account
        model_fields=[
        "parant",   
        "code",
        "name",
        "type",
        "fullcode",
        ]
"""
'''

from ninja import schema
class AccountOut(Schema):
        parant : "AccountOut" = None ===> ترجع الكلاس الاب مع الكلاس الابن 
         parant_id : int = None ==> في حالة ارجعة نفسة 
        code : str =None
        name : str = None
        type : str = None
        fullcode :str =None




'''
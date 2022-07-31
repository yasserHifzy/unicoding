from http import server
from locale import currency
from pydoc import describe
from ninja import Router
from django.db import transaction as db_transaction
transcation_router=Router()
from subacount.schema import TransactionIn
from subacount.models import Transaction,JournalEntery
from subacount import serves
from subacount.exception import AtomicAccounttresactions,ZeroAmountEorrer


@transcation_router.post("/add-transactionIn")
def add_transcation(request,transaction_in :TransactionIn):
    oparetion=serves.account_transfer(transaction_in)
    try :
        if oparetion :
            return 200,True
    except AtomicAccounttresactions:
          return 404,{"details" :"Rorrer during trinsactions"}
    
    except ZeroAmountEorrer:
          return 403,{"details" :"the amount must be more (Zero) please"}
from django.db import transaction as db_transaction
from subacount.models import Transaction,JournalEntery
@db_transaction.atomic()
def account_transfer(data):
    t=Transaction.objects.create(
            type=data.type,
            discription=data.discription)
    jec=JournalEntery.objects.create(transaction=t,account_id=data.je.account_creater,amount=data.je.amount,currency=data.je.currency)
    ed=JournalEntery.objects.create(transaction=t,account_id=data.je.account_dibter,amount=data.je.amount * -1,currency=data.je.currency)
    return True
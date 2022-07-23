from ninja import Router
from django.shortcuts import get_object_or_404
from accounting.models import Account, AccountTypeChoices
from accounting.schemas import AccountOut, FourOFourOut, GeneralLedgerOut
from typing import List
from django.db.models import Sum, Avg

account_router = Router()


@account_router.get("/get_all", response=List[AccountOut])
def get_all(request):
    accounts = Account.objects.all()

    return accounts


@account_router.get('/get_one/{account_id}/', response={
    200: AccountOut,
    404: FourOFourOut,
})
def get_one(request, account_id: int):
    try:
        account = Account.objects.get(id=account_id)
        return account
    except Account.DoesNotExist:
        return 404, {'detail': f'Account with id {account_id} does not exist'}


@account_router.get('/get_account_types/')
def get_account_types(request):
    result = {}
    for t in AccountTypeChoices.choices:
        result[t[0]] = t[1]
    return result


@account_router.get('/account-balance/{account_id}', response=GeneralLedgerOut)
def get_account_balance(request, account_id: int):
    account = get_object_or_404(Account, id=account_id)

    balance = account.journal_entries.values('currency').annotate(sum=Sum('amount')).order_by()

    journal_entries = account.journal_entries.all()

    return 200, {'account': account.name, 'balance': list(balance), 'jes': list(journal_entries)}

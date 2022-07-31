from re import M
from django.db import models
'''
Account:
    -account(parant)
    -type
    -code 
    -fullcode
Transaction:
    -type
    -discraption
JournalEntery
    -account
    -transaction
    -amount
    -currency
*Account must support multi  curancy.
*Transaction must cosist two or more even numder JournalEntery.
'''
class AccountTyoeChoices(models.TextChoices):
    ASSTS="ASSTS","ASSTS"
    LIABLIIES="LIABLIIES","LIABLIIES"
    INCOME="INCOME","INCOME"
    EXPNSES="EXPNSES","EXPNSES"
   # this acount is return choices is 
class TransactionyoeChoices(models.TextChoices):
    invoice=  "invoice","invoice"
    income="income","income"
    expense="expense","expense"
    bill="bill","bill"
class JournalEnteryoeChoices(models.TextChoices):
    USD="USD","USD"
    IQD="IQD","IQD"

class Account(models.Model):
    name=models.CharField(max_length=255)
    parant=models.ForeignKey("self",null=True,blank=True,on_delete=models.SET_NULL)
    type=models.CharField(max_length=255,choices=AccountTyoeChoices.choices)
    code=models.CharField(max_length=20)
    fullcode=models.CharField(max_length=25)
    def __str__(self) :
        return f"{self.fullcode} -{self.name}"


class Transaction(models.Model):
    type=models.CharField(max_length=255,choices=TransactionyoeChoices.choices)
    discription=models.CharField(max_length=255)

class JournalEntery(models.Model):
    class Meta:
        verbose_name_plural="Journal Enteries"
        
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="journal_enter")
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=19,decimal_places=2)
    currency=models.CharField(max_length=3,choices=JournalEnteryoeChoices.choices)
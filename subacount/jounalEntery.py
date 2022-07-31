from ninja import Router
jaounal_router=Router()
from typing import List
from subacount.schema import AjounelEOut
from subacount.models import JournalEntery

@jaounal_router.get("get_all",response=List[AjounelEOut])
def get_all(request):
    jes=JournalEntery.objects.all()
    return jes
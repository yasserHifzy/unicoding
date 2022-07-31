from django.contrib import admin
from django.urls import path
from subacount.api import api
from subacount.api import router_api
from subacount.jounalEntery import jaounal_router
from subacount.transaction import transcation_router
api.add_router("uaser/",router_api)
api.add_router("je/",jaounal_router)
api.add_router("transction/",transcation_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]

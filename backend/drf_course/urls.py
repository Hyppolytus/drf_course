from django.urls import path
from django.contrib import admin

# This is new, its a way of directing routing traffic to the correct view
# When a request comes in to an endpoint that we specify, the router will direct it towards the view, it works well with the url patterns django supplies
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
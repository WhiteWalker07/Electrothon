from . import views
from django.urls import path

urlpatterns =  [
    path('borrow',views.borrow,name='borrow'),
    path('profile',views.profile,name='profile'),
    path('lend',views.lend,name='lend'),
    path('donate',views.donate,name='donate')
]
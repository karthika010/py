from django.urls import path
from .views import *


urlpatterns=[
    path('home/',homepage),
    path('student_form/',student_form,name='student_form'),
    path('signup/',signup_view,name='signup'),
    path('login/',login_view,name='login'),
    path('student_biodata/',student_biodata,name='student_biodata'),
    
]



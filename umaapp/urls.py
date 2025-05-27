from django.urls import path
from .views import *


urlpatterns=[
    path('home/',homepage),
    path('student_form/',student_form,name='student_form'),
    path('signup/',signup_view,name='signup'),
    path('login/',login_view,name='login'),
    path('student_biodata/',student_biodata,name='student_biodata'),
    path('edit_biodata/<int:pk>/',edit_biodata,name='edit_biodata'),

    path('delete_biodata/<int:pk>/', delete_biodata,name='delete_biodata'),



    
]

    


from django.urls import path, include
from learning_templates import basic_app


#Template tagging
app_name = 'basic_app'

urlpatterns = [
    path('relative/',basic_app.views.relative,name='relative'),
    path('other/',basic_app.views.other,name='other'),
]

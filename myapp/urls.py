from django.urls import path
from myapp.views import base_views


app_name = 'myapp'

urlpatterns = [
    path('index/', base_views.index, name='index'),
    path('icf/', base_views.icf_view, name='icf_view'),
    path('rcf/', base_views.rcf_view, name='rcf_view'),
    path('scrm/', base_views.scrm_view, name='scrm_view'),
]
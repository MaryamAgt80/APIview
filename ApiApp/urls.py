from django.urls import path
from . import views
urlpatterns=[
    path('get_all_data',views.GetAllData.as_view(),name='get_all_data'),
    path('get-special-data/', views.GetSpecialData.as_view()),
    path('update-data/<int:pk>', views.UpdateData.as_view()),
    path('create-data', views.CreateData.as_view()),
    path('get-search-data', views.GetSearchData.as_view()),
    path('delete-data/<int:pk>', views.DeleteData.as_view()),
    path('get-all-data2/', views.GetAllDataFunc),
]
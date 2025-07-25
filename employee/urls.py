from django.urls import path
from employee import views

urlpatterns = [
    path('create-department/', views.create_department),
    path('list-departments/', views.list_departments),
    path('get-department/<str:emp_id>/', views.get_department),
    path('update-department/<str:emp_id>/', views.update_department),
    path('delete-department/<str:emp_id>/', views.delete_department),
    path('create/', views.create_employee),
    path('list/', views.list_employees),
    path('get/<str:emp_id>/', views.get_employee),
    path('update/<str:emp_id>/', views.update_employee),
    path('delete/<str:emp_id>/', views.delete_employee),
]

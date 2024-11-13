from django.urls import path
from . import views 

urlpatterns = [
    path('', views.expense_list_view, name='expense_list'),  
    path('create/', views.create_expense_view, name='create_expense'),  
    path('update/<int:pk>/', views.update_expense_view, name='update_expense'),  
    path('delete/<int:pk>/', views.delete_expense_view, name='delete_expense'),  
]


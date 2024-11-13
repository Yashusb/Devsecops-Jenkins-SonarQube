"""
URL configuration for Daily_Earning_Expense_Tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from expense_tracker.views import expense_list_view
from expense_tracker.views import (
    expense_list_view,
    create_expense_view,
    update_expense_view,
    delete_expense_view,
)

# def simple_view(request):
#     return HttpResponse("This is a simple test view.")

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', simple_view, name='simple-view'),  # Change this temporarily
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', expense_list_view, name='expense-list'),
#     path('expense/create/', create_expense_view, name='create-expense'),  # Route to create expense
#     path('expense/update/<int:pk>/', update_expense_view, name='update-expense'),  # Route to update expense
#     path('expense/delete/<int:pk>/', delete_expense_view, name='delete-expense'),
    
# ]

from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', include('expense_tracker.urls')),  
]

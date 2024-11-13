from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm

# List all expenses (Read)
def expense_list_view(request):
    expenses = Expense.objects.all()
    # print("Expenses fetched: ", expenses)  # Print fetched expenses for debugging
    return render(request, 'expense_tracker/expense_list.html', {'expenses': expenses})

# Create a new expense
def create_expense_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expense_tracker/expense_form.html', {'form': form})

# Update an expense
def update_expense_view(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense_tracker/expense_form.html', {'form': form})

# Delete an expense
def delete_expense_view(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expense_tracker/expense_confirm_delete.html', {'expense': expense})

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.utils import timezone
from .models import Todo
from .forms import TodoForm

# Display all todos with enhanced features
class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        priority_filter = self.request.GET.get('priority', '')
        category_filter = self.request.GET.get('category', '')
        status_filter = self.request.GET.get('status', '')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        if priority_filter:
            queryset = queryset.filter(priority=priority_filter)

        if category_filter:
            queryset = queryset.filter(category=category_filter)

        if status_filter == 'completed':
            queryset = queryset.filter(completed=True)
        elif status_filter == 'pending':
            queryset = queryset.filter(completed=False)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todos = self.get_queryset()

        # Statistics
        context['total_count'] = todos.count()
        context['completed_count'] = todos.filter(completed=True).count()
        context['pending_count'] = todos.filter(completed=False).count()
        context['overdue_count'] = todos.filter(
            completed=False,
            due_date__lt=timezone.now().date()
        ).exclude(due_date__isnull=True).count()

        # Priority breakdown
        context['priority_stats'] = todos.values('priority').annotate(
            count=Count('priority')
        ).order_by('-count')

        # Category breakdown
        context['category_stats'] = todos.values('category').annotate(
            count=Count('category')
        ).order_by('-count')

        return context

# Create a new todo
class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')

# Update a todo
class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')

# Delete a todo
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')

# Mark a todo as completed/incomplete
def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')
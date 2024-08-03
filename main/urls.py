from django.urls import path
from . import views
from .views import AlunoCreateView, AlunoUpdateView

urlpatterns = [
    path('',views.alunoView, name='aluno-lista'),
    path('aluno/<int:id>', views.alunoIDview, name='aluno-detalhe'),
    path('aluno/create/', AlunoCreateView.as_view(), name='aluno-create'),
    path('aluno/<int:pk>/update/', AlunoUpdateView.as_view(), name='aluno-update'),
    path('aluno/<int:id>/delete/', views.deleteAluno, name='delete-aluno')
]
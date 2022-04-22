from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('detlahe/<int:id>/', views.detalhes, name="detalhe"),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('atualizar/<int:id>', views.atualizar, name="atualizar"), 
    path('form-tabela-classificaco/', views.tabela_classifiacao, name='form-tabela-classificaco'),
    path('form-tabela-classificaco/<int:id>', views.update_classificacao, name='form-tabela-classificaco'),
     path('info-equipe/<int:id>', views.info_equipe, name='info-equipe')
]

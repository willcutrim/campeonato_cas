from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('detlahe/<int:id>/', views.detalhes, name="detalhe"),
    path('/<int:id>', views.delete, name='delete')
]

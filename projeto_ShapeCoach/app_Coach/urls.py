from . import views
from django.urls import path

urlpatterns = [
    path('', views.pagina_login, name='login'),
    path('cadastro/', views.pagina_cadastro, name='cadastro'),
    path('dados/', views.pagina_dados, name='dados'),
    path('objetivo/', views.pagina_objetivo, name='objetivo'),
    path('local/', views.pagina_local, name='local'),
    path('home/', views.pagina_home, name='home'),
    path('receita/', views.pagina_receita, name='receita'),
    path('treinar/', views.pagina_treinar, name='treinar'),
    path('treino1/', views.pagina_treino1, name='treino1'),
    path('treino2/', views.pagina_treino2, name='treino2'),
    path('treino3/', views.pagina_treino3, name='treino3'),
    path('duvida/', views.pagina_duvida, name='duvida'),
    path('duvida2/', views.pagina_duvida2, name='duvida2'),
    path('duvida3/', views.pagina_duvida3, name='duvida3'),
]


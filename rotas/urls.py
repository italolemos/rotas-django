from django.urls import path

from .views import RotasListView, RotasDetailView, RotasCreateView, RotasUpdateView, RotasDeleteView

app_name = 'rotas'
urlpatterns = [
    path('', RotasListView.as_view(), name='rotas-list'),
    path('<int:pk>/', RotasDetailView.as_view(), name='rotas-detail'),
    path('nova/', RotasCreateView.as_view(), name='rotas-create'),
    path('editar/rota/<int:pk>', RotasUpdateView.as_view(), name='rotas-edit'),
    path('deletar/rota/<int:pk>', RotasDeleteView.as_view(), name='rotas-delete')

]
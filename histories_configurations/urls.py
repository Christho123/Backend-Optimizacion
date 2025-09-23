from django.urls import path
from .views.history import histories_list, history_create, history_delete, history_update  # Importar la nueva función
from .views.document_type import document_types_list, document_type_create, document_type_delete
from .views.payment_type import payment_types_list, payment_type_create, payment_type_delete, payment_type_edit
from .views.predetermined_price import predetermined_prices_list, predetermined_price_create, predetermined_price_update, predetermined_price_delete

urlpatterns = [
    # Rutas de histories
    path("histories/", histories_list, name="histories_list"),
    path("histories/create/", history_create, name="history_create"),
    path("histories/<int:pk>/update/", history_update, name="history_update"),  # Nueva ruta PUT
    path("histories/<int:pk>/delete/", history_delete, name="history_delete"),

    path("document_types/", document_types_list, name="document_types_list"),  # Para listar tipos de documento
    path("document_types/create/", document_type_create, name="document_type_create"),  # Para crear un tipo de documento
    path("document_types/<int:pk>/delete/", document_type_delete, name="document_type_delete"),  # Para eliminar un tipo de documento

    path("payment_types/", payment_types_list, name="payment_types_list"),  # Para listar tipos de pago
    path("payment_types/create/", payment_type_create, name="payment_type_create"),  # Para crear un tipo de pago
    path("payment_types/<int:pk>/delete/", payment_type_delete, name="payment_type_delete"),  # Para eliminar un tipo de pago
    path('payment_types/<int:pk>/edit/', payment_type_edit, name='payment_type_edit'),
    
    path("predetermined_prices/", predetermined_prices_list, name="predetermined_prices_list"),
    path("predetermined_prices/create/", predetermined_price_create, name="predetermined_price_create"),
    path("predetermined_prices/<int:pk>/edit/", predetermined_price_update, name="predetermined_price_update"),
    path("predetermined_prices/<int:pk>/delete/", predetermined_price_delete, name="predetermined_price_delete"),
]
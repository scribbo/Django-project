from django.urls import path
import ordershop.views as ordershop

app_name  = 'ordershop'

urlpatterns = [
    path("", ordershop.OrderListView.as_view(), name='list'),
    path("create", ordershop.create_order, name='create'),
    path("<int:pk>", ordershop.OrderUpdateView.as_view(), name='update'),
    path("<int:pk>/pay", ordershop.pay_for_order, name='pay'),
    path("<int:pk>/cancel", ordershop.cancel_order, name='cancel'),
]

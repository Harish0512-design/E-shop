from django.urls.conf import path
from django.views.generic.base import RedirectView
from products import views
urlpatterns = [
    path('cart/addquantity/<int:pk>',views.additemquantity),
    path('cart/removequantity/<int:pk>',views.removeitemquantity),
    path('cart/add/<int:pk>',views.cart),
    path('deliver/',views.deliverview),
    path('cart/',views.CartView.as_view()),
    path('contact/',views.ContactView.as_view()),
    path('about/',views.AboutView.as_view()),
    path('recents/<int:pk>',views.recentsView),
    path('sold/',views.OrderedView.as_view()),
    path('cart/remove/<int:pk>',views.cartdel),
    path('product_list/',views.ProductListView.as_view()),
    path('product_list/<int:pk>/',views.ProductDetailView.as_view()),
    path('profile/edit/<int:pk>/',views.ProfileEditView.as_view(success_url="/products/product_list")),
    path('',RedirectView.as_view(url="product_list/")),
]
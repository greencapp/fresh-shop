from django.conf.urls import url

from cart import views

urlpatterns = [
    # 加入购物车
    url(r'^add_cart/', views.add_cart, name='add_cart'),
    # 购物车
    url(r'^cart/', views.cart, name='cart'),
    # 结算
    url(r'^place_order/', views.place_order, name='place_order'),
    # 我的购物车数据
    url(r'^cart_count/', views.cart_count, name='cart_count'),
    # 修改购物车中商品的个数
    url(r'^cart_num/', views.cart_num, name='cart_num'),


]
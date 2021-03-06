from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<int:customer_pk>/', views.customer, name='customer'),
    path('create_order/<int:customer_id>', views.create_order, name="create_order"),
    path('update_order/<int:order_id>', views.update_order, name="update_order"),
    path('delete_order/<int:order_id>', views.delete_order, name="delete_order"),

    path('user/', views.user_page, name='user_page'),

    path('account/', views.account_settings, name="account"),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_user, name='register'),

    path(
        'password_reset/', 
        auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), 
        name="password_reset"
    ), 
    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
        name="password_reset_done"
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),
        name="password_reset_confirm"
    ),
    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name="password_reset_complete"
    )
]
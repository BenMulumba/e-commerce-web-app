from django.contrib import admin
from django.contrib.auth import views as auth_views # import default view from django to use for login and logout 
from django.urls import path, include
from user import views as user_views


urlpatterns = [
    path("", include("ecommerce.urls")),
    path("admin/", admin.site.urls),
    path("register/", user_views.register, name='registration'), 
    path("login/", auth_views.LoginView.as_view( template_name='user/template/user/login.html' ), name ='login'),    
    path("logout/", auth_views.LoginView.as_view( template_name= 'user/template/user/logout.html'), name ='logout'),
    # pat   h('ecommerce/', include('django.contrib.auth.urls'))
]

"""beejbazar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views #import this
# from beejbazar import ecommerce

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('account/',include('account.urls')),
    path('ecommerce/',include('ecommerce.urls')),
    path('weather/',include('weather.urls')),
    path('marketprice/',include('marketprice.urls')),
    path('crop_info/',include('cropinfo.urls')),
    path('socialmedia/',include('socialmedia.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'), name='password_reset_complete'),      
    # path('cont/',include('ecommerce.context_processors.add_variable_to_context')),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

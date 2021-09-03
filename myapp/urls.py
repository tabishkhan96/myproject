from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from.import views

app_name ='myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<int:id>', views.detail, name='detail'),
    path('new', views.add_new, name='add_new'),
    path('<int:id>/update/', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

    path('login/', views.login_req, name='login'),

    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.sign_up1, name='signup'),

]

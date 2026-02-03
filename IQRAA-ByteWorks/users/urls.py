from django.urls import path
from .views import FirstDashBoard,EmployeeLoginView,EmployeeRegistrationView,LogoutView

app_name = 'users'  # Must have this namespace


urlpatterns = [
        path('', FirstDashBoard.as_view(), name='main_dashboard'),  # main dshboard url
        path('login/', EmployeeLoginView.as_view(), name='login'),  # login url
        path('register/', EmployeeRegistrationView.as_view(), name='register'), # new user registraion url
        path('logout/', LogoutView.as_view(), name='logout'),






]
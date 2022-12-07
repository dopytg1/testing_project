from django.urls import path


from .views import test, home, test_passing

urlpatterns = [
    path('', test, name='test'),
    path('home', home, name='home'),
    path('test/<int:id>/<int:page>', test_passing, name='test_passing'),

]
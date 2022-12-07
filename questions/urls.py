from django.urls import path


from .views import home, test_passing, results

urlpatterns = [
    path('home', home, name='home'),
    path('test/<int:id>/<int:page>', test_passing, name='test_passing'),
    path('results/<int:correct>/<int:incorrect>', results, name='results')
]
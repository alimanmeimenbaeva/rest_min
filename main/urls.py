"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from tv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors', views.DirectorList.as_view()),
    path('api/v1/directors/<int:id>', views.DirectorDetail.as_view()),
    path('api/v1/movies', views.MovieList.as_view()),
    path('api/v1/movies/<int:id>', views.MovieDetail.as_view()),
    path('api/v1/revies', views.ReviewList.as_view()),
    path('api/v1/revies/<int:id>', views.ReviewDetail.as_view()),
    path('api/v1/movies/reviews/', views.MovieReviewList.as_view(), name='movie_review_list'),

]

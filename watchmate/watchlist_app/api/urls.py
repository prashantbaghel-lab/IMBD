from django.urls import path, include
from watchlist_app.api.views import movie_list, movie_detail
urlpatterns = [
    path('list/', movie_list, name='movie-list'),
    path('<int:pk>', movie_detail, name='movie_detail')
    #path('', views.index, name='index'),
    # path('upload', views.upload, name='upload'),
    # path('follow', views.follow, name='follow'),
    # path('search', views.search, name='search'),
    # path('profile/<str:pk>', views.profile, name='profile'),
    # path('like-post', views.like_post, name='like-post'),
    # path('setting', views.setting, name='setting'),
    # path('signup', views.signup, name='signup'),
    # path('signin', views.signin, name='signin'),
    # path('logout', views.logout, name='logout')

]

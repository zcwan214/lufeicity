from django.conf.urls import url
from api.views import course
from api.views import shoppingcar
# from api import views
#
#
# urlpatterns = [
#     # url(r'degreecourses/',views.Courses.as_view())
# ]
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'courses', views.Courses)
# urlpatterns += router.urls


urlpatterns = [
    url(r'courses/$',course.CoursesView.as_view()),
    url(r'courses/(?P<pk>\d+)/$',course.CourseDetailView.as_view()),
    url(r'degree/$',course.DegreeView.as_view()),
    url(r'shoppingcar/$',shoppingcar.ShoppingCarView.as_view({'get':'get'}))

]
from django.conf.urls import url

from review.views.review_view import ReviewViewset
from review.views.course import CourseViewset

urlpatterns = [
    url(r'^review/$', ReviewViewset.as_view(), name='review'),
    url(r'^review/(?P<pk>[0-9]+)/$',
        ReviewViewset.as_view(), name='review_pk'),
    url(r'^course/$', CourseViewset.as_view(), name='course'),
    url(r'^course/(?P<pk>[0-9]+)/$',
        CourseViewset.as_view(), name='course_pk')
]

from django.conf.urls import url

from review.views.review_view import ReviewViewset
from review.views.course import CourseViewset
from review.views.institute import InstituteViewset
from review.views.institute_course import InstituteCourseViewset

urlpatterns = [
    url(r'^review/$', ReviewViewset.as_view(), name='review'),
    url(r'^review/(?P<pk>[0-9]+)/$',
        ReviewViewset.as_view(), name='review_pk'),
    url(r'^course/$', CourseViewset.as_view(), name='course'),
    url(r'^course/(?P<pk>[0-9]+)/$',
        CourseViewset.as_view(), name='course_pk')
    url(r'^institute/$', InstituteViewset.as_view(), name='institute'),
    url(r'^institute/(?P<pk>[0-9]+)/$',
        InstituteViewset.as_view(), name='institute_pk')
    url(r'^institute_course/$', InstituteCourseViewset.as_view(), name='institute_course'),
    url(r'^institute_course/(?P<pk>[0-9]+)/$',
        InstituteCourseViewset.as_view(), name='institute_course_pk')
]

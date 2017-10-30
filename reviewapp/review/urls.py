from django.conf.urls import url

from review.views.review_view import ReviewViewset

urlpatterns = [
    url(r'^review/$', ReviewViewset.as_view(), name='review'),
    url(r'^review/(?P<pk>[0-9]+)/$',
        ReviewViewset.as_view(), name='review_pk'),
]

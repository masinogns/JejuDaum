from django.conf.urls import url

from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    # url(r'^$', IndexView.as_view(), name='index'),
    url(r'^$', BookList.as_view(), name='book_list'),
    url(r'^new$', BookCreate.as_view(), name='book_new'),
    url(r'^edit/(?P<pk>\d+)$', BookUpdate.as_view(), name='book_edit'),
    url(r'^delete/(?P<pk>\d+)$', BookDelete.as_view(), name='book_delete'),
    url(r'^detail/(?P<pk>\d+)$', BookDetail.as_view(), name='book_detail'),
    url(r'^change/$',BookChangeList.as_view(), name="book_change"),
]

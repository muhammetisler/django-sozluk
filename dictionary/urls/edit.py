from django.urls import path

from ..views.edit import CommentCreate, CommentUpdate, EntryUpdate
from ..views.reporting import GeneralReportView


urlpatterns_edit = [
    path('entry/update/<int:pk>/', EntryUpdate.as_view(), name="entry_update"),
    path("entry/<int:pk>/comment/", CommentCreate.as_view(), name="comment_create"),
    path("entry/comment/edit/<int:pk>", CommentUpdate.as_view(), name="comment_update"),
    path('contact/', GeneralReportView.as_view(), name="general-report"),
]

from django.urls import path
from .views import (
    GinListView,
    GinDetailView,
    CommentListView,
    CommentDetailView,
    GinLikeView
)

urlpatterns = [
    path('', GinListView.as_view()),
    path('<int:pk>/', GinDetailView.as_view()),
    path('<int:gin_pk>/comments/', CommentListView.as_view()),
    path('<int:gin_pk>/comments/<int:comment_pk>/', CommentDetailView.as_view()),
    path('<int:gin_pk>/like/', GinLikeView.as_view())
]

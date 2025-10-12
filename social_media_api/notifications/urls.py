# from django.urls import path
# from .views import NotificationListView

# urlpatterns = [
#     path('notifications/', NotificationListView.as_view(), name='notifications'),
# ]

from django.urls import path
from .views import NotificationListView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),  # empty string
]

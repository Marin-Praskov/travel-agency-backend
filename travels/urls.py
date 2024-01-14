from django.urls import path
from .views import LocationList, LocationDetail, HolidayList, HolidayDetail, ReservationList, ReservationDetail

urlpatterns = [
    path('locations/', LocationList.as_view(), name='location-list'),
    path('locations/<int:pk>/', LocationDetail.as_view(), name='location-detail'),
    path('holidays/', HolidayList.as_view(), name='holiday-list'),
    path('holidays/<int:pk>/', HolidayDetail.as_view(), name='holiday-detail'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', ReservationDetail.as_view(), name='reservation-detail'),
]

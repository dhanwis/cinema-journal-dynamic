from django.urls import path
from user_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('latest/release', latest_release, name='latest_release'),
    path('latest/release/<slug:latest_release_slug>/', latest_release_details, name='latest_release_details'),
    path('location/report', location_report, name='location_report'),
    path('location/report/<slug:location_report_slug>/', location_report_details, name='location_report_details'),
    path('meet/the/person', meet_the_person, name='meet_the_person'),
    path('meet/the/person/<slug:meet_the_person_slug>/', meet_the_person_details, name='meet_the_person_details'),
    path('teaser/and/promose', teaser_and_promose, name='teaser_and_promose'),
    path('teaser/and/promose/<slug:teaser_and_promose_slug>/', teaser_and_promose_details, name='teaser_and_promose_details'),
]
from django.urls import path
from admin_app.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    
    path('latest/release/list/', latest_release_list, name='latest_release_list'),
    path('latest/release/add/', latest_release_add, name='latest_release_add'),
    path('latest/release/<slug:latest_release_slug>/view/', latest_release_view, name='latest_release_view'),
    path('latest/release/<int:latest_release_id>/edit/', latest_release_edit, name='latest_release_edit'),
    path('latest/release/<int:latest_release_id>/delete/', latest_release_delete, name='latest_release_delete'),
    
    path('location/report/list/', location_report_list, name='location_report_list'),
    path('location/report/add/', location_report_add, name='location_report_add'),
    path('location/report/<int:location_report_id>/view/', location_report_view, name='location_report_view'),
    path('location/report/<int:location_report_id>/edit/', location_report_edit, name='location_report_edit'),
    path('location/report/<int:location_report_id>/delete/', location_report_delete, name='location_report_delete'),
    
    path('meet/the/person/list/', meet_the_person_list, name='meet_the_person_list'),
    path('meet/the/person/add/', meet_the_person_add, name='meet_the_person_add'),
    path('meet/the/person/<int:meet_the_person_id>/view/', meet_the_person_view, name='meet_the_person_view'),
    path('meet/the/person/<int:meet_the_person_id>/edit/', meet_the_person_edit, name='meet_the_person_edit'),
    path('meet/the/person/<int:meet_the_person_id>/delete/', meet_the_person_delete, name='meet_the_person_delete'),
    
    path('teaser/and/promose/list/', teaser_and_promose_list, name='teaser_and_promose_list'),
    path('teaser/and/promose/add/', teaser_and_promose_add, name='teaser_and_promose_add'),
    path('teaser/and/promose/<int:teaser_and_promose_id>/view/', teaser_and_promose_view, name='teaser_and_promose_view'),
    path('teaser/and/promose/<int:teaser_and_promose_id>/edit/', teaser_and_promose_edit, name='teaser_and_promose_edit'),
    path('teaser/and/promose/<int:teaser_and_promose_id>/delete/', teaser_and_promose_delete, name='teaser_and_promose_delete'),
]
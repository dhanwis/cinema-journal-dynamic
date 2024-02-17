from django.shortcuts import render, redirect
from admin_app.models import LatestRelease, LocationReport, MeetThePerson, TeaserAndPromose

# Create your views here.

def home(request):
    current_page = 'home'
    latest_releases_one = LatestRelease.objects.all().order_by('-id')[0:4]
    latest_releases_two = LatestRelease.objects.all().order_by('-id')[4:8]
    location_reports_one = LocationReport.objects.all().order_by('-id')[:1]
    location_reports_two = LocationReport.objects.all().order_by('-id')[1:5]
    meet_the_persons = MeetThePerson.objects.all().order_by('-id')[0:10]
    teaser_and_promoses = TeaserAndPromose.objects.all().order_by('-id')[0:10]
    
    context = {
        'current_page': current_page,
        'latest_releases_one' : latest_releases_one,
        'latest_releases_two' : latest_releases_two,
        'location_reports_one' : location_reports_one,
        'location_reports_two' : location_reports_two,
        'meet_the_persons' : meet_the_persons,
        'teaser_and_promoses' : teaser_and_promoses,
    }
    return render(request, 'user_app/pages/home.html', context)

def latest_release(request):
    current_page = 'latest_release'
    latest_releases = LatestRelease.objects.all().order_by('-id')
    context = {
        'current_page': current_page,
        'latest_releases' : latest_releases
    }
    return render(request, 'user_app/pages/latest_release.html', context)


def latest_release_details(request, latest_release_slug):
    current_page = 'latest_release_details'
    try:
        latest_release = LatestRelease.objects.get(slug=latest_release_slug)
    except LatestRelease.DoesNotExist:
        return redirect('home')
    context = {
        'current_page': current_page,
        'latest_release' : latest_release
    }
    return render(request, 'user_app/pages/latest_release_details.html', context)

def location_report(request):
    current_page = 'location_report'
    location_reports = LocationReport.objects.all().order_by('-id')
    context = {
        'current_page': current_page,
        'location_reports' : location_reports
    }
    return render(request, 'user_app/pages/location_report.html', context)


def location_report_details(request, location_report_slug):
    current_page = 'location_report_details'
    try:
        location_report = LocationReport.objects.get(slug=location_report_slug)
    except LocationReport.DoesNotExist:
        return redirect('home')
    context = {
        'current_page': current_page,
        'location_report' : location_report
    }
    return render(request, 'user_app/pages/location_report_details.html', context)

def meet_the_person(request):
    current_page = 'meet_the_person'
    meet_the_persons = MeetThePerson.objects.all().order_by('-id')
    context = {
        'current_page': current_page,
        'meet_the_persons' : meet_the_persons
    }
    return render(request, 'user_app/pages/meet_the_person.html', context)

def meet_the_person_details(request, meet_the_person_slug):
    current_page = 'meet_the_person_details'
    try:
        meet_the_person = MeetThePerson.objects.get(slug=meet_the_person_slug)
    except MeetThePerson.DoesNotExist:
        return redirect('home')
    context = {
        'current_page': current_page,
        'meet_the_person' : meet_the_person
    }
    return render(request, 'user_app/pages/meet_the_person_details.html', context)

def teaser_and_promose(request):
    current_page = 'teaser_and_promose'
    teaser_and_promoses = TeaserAndPromose.objects.all().order_by('-id')
    context = {
        'current_page': current_page,
        'teaser_and_promoses' : teaser_and_promoses
    }
    return render(request, 'user_app/pages/teaser_and_promose.html', context)


def teaser_and_promose_details(request, teaser_and_promose_slug):
    current_page = 'teaser_and_promose_details'
    try:
        teaser_and_promose = TeaserAndPromose.objects.get(slug=teaser_and_promose_slug)
    except TeaserAndPromose.DoesNotExist:
        return redirect('home')
    context = {
        'current_page': current_page,
        'teaser_and_promose' : teaser_and_promose
    }
    return render(request, 'user_app/pages/teaser_and_promose_details.html', context)
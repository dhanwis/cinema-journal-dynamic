from django.shortcuts import render, redirect
from django.contrib import messages
from admin_app.models import *
from admin_app.forms import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.


def handler404(request, exception):
    return render(request, '404.html', status=404)

@login_required(login_url='/auth/admin/login/')
def dashboard(request):
    current_page = 'dashboard'
    context = {
        'current_page': current_page,
    }
    return render(request, 'admin_app/pages/dashboard.html', context)

######################################### latest_release #####################################################

@login_required(login_url='/auth/admin/login/')
def latest_release_list(request):
    latest_releases = LatestRelease.objects.all()
    context = {
        'latest_releases': latest_releases
    }
    return render(request, 'admin_app/pages/latest_release_list.html', context)

@login_required(login_url='/auth/admin/login/')
def latest_release_add(request):
    if request.method == 'POST':
        form = LatestReleaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article added successfully')
            return redirect('latest_release_list')
        else:
            print(form.errors)  # Print form errors to console for debugging
    else:
        form = LatestReleaseForm()
    return render(request, 'admin_app/pages/latest_release_add.html', {'form': form})


@login_required(login_url='/auth/admin/login/')
def latest_release_edit(request, latest_release_id):
    latest_release = LatestRelease.objects.get(id=latest_release_id)
    if request.method == 'POST':
        form = LatestReleaseForm(request.POST, request.FILES, instance=latest_release)
        if form.is_valid():
            form.save()
            messages.success(request, 'Latest release updated successfully')
            return redirect('latest_release_list')
    else:
        form = LatestReleaseForm(instance=latest_release)
    
    return render(request, 'admin_app/pages/latest_release_edit.html', {'form': form})

@login_required(login_url='/auth/admin/login/')
# def latest_release_view(request, latest_release_id):
#     latest_release = LatestRelease.objects.get(id=latest_release_id)
#     context = {
#         'latest_release': latest_release
#     }
#     return render(request, 'admin_app/pages/latest_release_view.html', context)

@login_required(login_url='/auth/admin/login/')
def latest_release_view(request, latest_release_slug):
    latest_release = get_object_or_404(LatestRelease, slug=latest_release_slug)
    context = {
        'latest_release': latest_release
    }
    return render(request, 'admin_app/pages/latest_release_view.html', context)


@login_required(login_url='/auth/admin/login/')
def latest_release_delete(request, latest_release_id):
    latest_release = LatestRelease.objects.get(id=latest_release_id)
    latest_release.delete()
    return redirect('latest_release_list')
    
    
######################################### location_report #####################################################



@login_required(login_url='/auth/admin/login/')
def location_report_list(request):
    location_reports = LocationReport.objects.all()
    context = {
        'location_reports': location_reports
    }
    return render(request, 'admin_app/pages/location_report_list.html', context)

@login_required(login_url='/auth/admin/login/')
def location_report_add(request):
    if request.method == 'POST':
        form = LocationReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article added successfully')
            return redirect('location_report_list')
        else:
            print(form.errors)  # Print form errors to console for debugging
    else:
        form = LocationReportForm()
    return render(request, 'admin_app/pages/location_report_add.html', {'form': form})


@login_required(login_url='/auth/admin/login/')
def location_report_edit(request, location_report_id):
    location_report = LocationReport.objects.get(id=location_report_id)
    if request.method == 'POST':
        form = LocationReportForm(request.POST, request.FILES, instance=location_report)
        if form.is_valid():
            form.save()
            messages.success(request, 'Latest release updated successfully')
            return redirect('location_report_list')
    else:
        form = LocationReportForm(instance=location_report)
    return render(request, 'admin_app/pages/location_report_edit.html', {'form': form})

@login_required(login_url='/auth/admin/login/')
def location_report_view(request, location_report_id):
    location_report = LocationReport.objects.get(id=location_report_id)
    context = {
        'location_report': location_report
    }
    return render(request, 'admin_app/pages/location_report_view.html', context)

@login_required(login_url='/auth/admin/login/')
def location_report_delete(request, location_report_id):
    location_report = LocationReport.objects.get(id=location_report_id)
    location_report.delete()
    return redirect('location_report_list')

 
######################################### meet_the_person #####################################################


@login_required(login_url='/auth/admin/login/')
def meet_the_person_list(request):
    meet_the_persons = MeetThePerson.objects.all()
    context = {
        'meet_the_persons': meet_the_persons
    }
    return render(request, 'admin_app/pages/meet_the_person_list.html', context)

@login_required(login_url='/auth/admin/login/')
def meet_the_person_add(request):
    if request.method == 'POST':
        form = MeetThePersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article added successfully')
            return redirect('meet_the_person_list')
        else:
            print(form.errors)  # Print form errors to console for debugging
    else:
        form = MeetThePersonForm()
    return render(request, 'admin_app/pages/meet_the_person_add.html', {'form': form})


@login_required(login_url='/auth/admin/login/')
def meet_the_person_edit(request, meet_the_person_id):
    meet_the_person = MeetThePerson.objects.get(id=meet_the_person_id)
    if request.method == 'POST':
        form = MeetThePersonForm(request.POST, request.FILES, instance=meet_the_person)
        if form.is_valid():
            form.save()
            messages.success(request, 'Latest release updated successfully')
            return redirect('meet_the_person_list')
    else:
        form = MeetThePersonForm(instance=meet_the_person)
    return render(request, 'admin_app/pages/meet_the_person_edit.html', {'form': form})

@login_required(login_url='/auth/admin/login/')
def meet_the_person_view(request, meet_the_person_id):
    meet_the_person = MeetThePerson.objects.get(id=meet_the_person_id)
    context = {
        'meet_the_person': meet_the_person
    }
    return render(request, 'admin_app/pages/meet_the_person_view.html', context)

@login_required(login_url='/auth/admin/login/')
def meet_the_person_delete(request, meet_the_person_id):
    meet_the_person = MeetThePerson.objects.get(id=meet_the_person_id)
    meet_the_person.delete()
    return redirect('meet_the_person_list')



######################################### teaser_and_promose #####################################################


@login_required(login_url='/auth/admin/login/')
def teaser_and_promose_list(request):
    teaser_and_promoses = TeaserAndPromose.objects.all()
    context = {
        'teaser_and_promoses': teaser_and_promoses
    }
    return render(request, 'admin_app/pages/teaser_and_promose_list.html', context)

@login_required(login_url='/auth/admin/login/')
def teaser_and_promose_add(request):
    if request.method == 'POST':
        form = TeaserAndPromoseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article added successfully')
            return redirect('teaser_and_promose_list')
        else:
            print(form.errors)  # Print form errors to console for debugging
    else:
        form = TeaserAndPromoseForm()
    return render(request, 'admin_app/pages/teaser_and_promose_add.html', {'form': form})


@login_required(login_url='/auth/admin/login/')
def teaser_and_promose_edit(request, teaser_and_promose_id):
    teaser_and_promose = TeaserAndPromose.objects.get(id=teaser_and_promose_id)
    if request.method == 'POST':
        form = TeaserAndPromoseForm(request.POST, request.FILES, instance=teaser_and_promose)
        if form.is_valid():
            form.save()
            messages.success(request, 'Latest release updated successfully')
            return redirect('teaser_and_promose_list')
    else:
        form = TeaserAndPromoseForm(instance=teaser_and_promose)
    return render(request, 'admin_app/pages/teaser_and_promose_edit.html', {'form': form})

@login_required(login_url='/auth/admin/login/')
def teaser_and_promose_view(request, teaser_and_promose_id):
    teaser_and_promose = TeaserAndPromose.objects.get(id=teaser_and_promose_id)
    context = {
        'teaser_and_promose': teaser_and_promose
    }
    return render(request, 'admin_app/pages/teaser_and_promose_view.html', context)

@login_required(login_url='/auth/admin/login/')
def teaser_and_promose_delete(request, teaser_and_promose_id):
    teaser_and_promose = TeaserAndPromose.objects.get(id=teaser_and_promose_id)
    teaser_and_promose.delete()
    return redirect('teaser_and_promose_list')




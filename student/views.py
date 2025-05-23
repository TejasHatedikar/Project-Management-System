from django.shortcuts import render, redirect
from authentication.models import Faculty, Group
from django.http import JsonResponse
from django.conf import settings
import datetime

def homeView(request):
    if request.user.is_anonymous:
        return redirect('login')
    
    # now = datetime.datetime.now().date()
    # PS_days = (settings.PS_SUBMISSION - now).date()
    # midsem_days = (settings.MIDSEM_SUBMISSION - now).date()
    # endsem_days = (settings.ENDSEM_SUBMISSION - now).date()
    # print(PS_days, midsem_days, endsem_days)

    PS_submission_date = datetime.datetime.strptime(settings.PS_SUBMISSION, "%Y-%m-%d").date()
    midsem_submission_date = datetime.datetime.strptime(settings.MIDSEM_SUBMISSION, "%Y-%m-%d").date()
    endsem_submission_date = datetime.datetime.strptime(settings.ENDSEM_SUBMISSION, "%Y-%m-%d").date()

    # Get today's date
    now = datetime.datetime.now().date()

    # Calculate days remaining
    PS_days = (PS_submission_date - now).days
    midsem_days = (midsem_submission_date - now).days
    endsem_days = (endsem_submission_date - now).days

    group = Group.objects.get(email=request.user.username)

    if request.method == 'POST':
        if request.POST.get('project_title'):
            project_name = request.POST.get('project_title')
            description = request.POST.get('description')
            domain = request.POST.get('domain')
            guide = request.POST.get('guide')
            tags = request.POST.get('tags')

            group.pname = project_name
            group.description = description
            group.domain = domain.lower()
            group.guide = guide
            group.tags = tags
            group.submitted_PS = True
            group.save()
        elif request.POST.get('presentation'):
            group.PPT = request.FILES.get('presentation')
            group.midsem_conducted = True
            group.save()
        elif request.POST.get('working_model'):
            group.working_model = request.FILES.get('working_model')
            group.report = request.FILES.get('report')
            group.endsem_conducted = True
            group.save()
    return render(request, 'shome.html', {'group': group, 'PS_days': PS_days, 'midsem_days': midsem_days, 'endsem_days': endsem_days})

def timelineView(request):
    if request.user.is_anonymous:
        return redirect('login')
    return render(request, 'timelines.html', {'PS_date': settings.PS_SUBMISSION, 'midsem_date': settings.MIDSEM_SUBMISSION, 'endsem_date': settings.ENDSEM_SUBMISSION})

def groupView(request):
    if request.user.is_anonymous:
        return redirect('login')

    group = Group.objects.get(email=request.user.username)
    try:
        faculty = Faculty.objects.get(email=group.guide)
    except:
        faculty = None

    if request.method == 'POST':
        if request.POST.get('guide-email'):
            try:
                faculty = Faculty.objects.get(email=request.POST.get('guide-email'))
                group.guide = faculty.email
            except:
                faculty = None
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            prn = request.POST.get('prn')
            roll = request.POST.get('roll')
            
            if group.memName1 == 'Name of the member':
                group.memName1 = name
                group.memEmail1 = email
                group.memPRN1 = prn
                group.memRoll1 = roll
            elif group.memName2 == 'Name of the member':
                group.memName2 = name
                group.memEmail2 = email
                group.memPRN2 = prn
                group.memRoll2 = roll
            elif group.memName3 == 'Name of the member':
                group.memName3 = name
                group.memEmail3 = email
                group.memPRN3 = prn
                group.memRoll3 = roll
        group.save()
    return render(request, 'groupmate_data.html', {'group': group, 'faculty': faculty})

def domainView(request):
    if request.user.is_anonymous:
        return redirect('login')

    if request.method == 'POST':
        domain = request.POST.get('domain')
        
        if domain == "All":
            groups = Group.objects.all()
        else:
            groups = Group.objects.filter(domain=domain.lower())
        return render(request, 'project_overview.html', {'groups': groups})
    return render(request, 'domain.html')

def deleteMember(request):
    if request.user.is_anonymous:
        return redirect('login')

    group = Group.objects.get(email=request.user.username)
    if request.method == 'POST':
        val = request.POST.get('email')

        if val == "1":
            print(group.memEmail1)
            group.memName1 = 'Name of the member'
            group.memEmail1 = ''
            group.memPRN1 = 0
            group.memRoll1 = 0
        elif val == "2":
            print(group.memEmail2)
            group.memName2 = 'Name of the member'
            group.memEmail2 = ''
            group.memPRN2 = 0
            group.memRoll2 = 0
        elif val == "3":
            print(group.memEmail3)
            group.memName3 = 'Name of the member'
            group.memEmail3 = ''
            group.memPRN3 = 0
            group.memRoll3 = 0
        elif val == "4":
            group.guide = 'Guide of the project'
        else:
            print("Invalid value")
            return redirect('groupmate')
        group.save()
        print("Saved")
        return redirect('groupmate')

def viewProject(request):
    if request.user.is_anonymous:
        return redirect('login')

    if request.method == 'POST':
        email = request.POST.get('email')
        group = Group.objects.get(email=email)
        return render(request, 'project.html', {'group': group})
    return render(request, 'domain.html')

from django.shortcuts import render, get_object_or_404, redirect
from authentication.models import Faculty, Group

def homeView(request):
    if request.user.is_anonymous:
        return redirect('login')

    faculty = get_object_or_404(Faculty, email=request.user.username)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        qualification = request.POST.get('qualification')
        department = request.POST.get('department')
        date_joined = request.POST.get('date_joined')

        if name:
            faculty.fname = name
        if email:
            faculty.email = email
        if phone:
            faculty.contact_num = phone
        if qualification:
            faculty.qualification = qualification
        if department:
            faculty.dept = department
        if date_joined:
            faculty.joining_date = date_joined

        faculty.save()

    return render(request, 'fhome.html', {'faculty': faculty})

def domainView(request):
    if request.user.is_anonymous:
        return redirect('login')

    if request.method == 'POST':
        domain = request.POST.get('domain')
        
        if domain == "All":
            groups = Group.objects.all()
        else:
            groups = Group.objects.filter(domain=domain.lower())
        return render(request, 'fproject_overview.html', {'groups': groups, 'title': domain.title() + " Projects"})
    return render(request, 'fdomain.html')

def viewProject(request):
    if request.user.is_anonymous:
        return redirect('login')

    if request.method == 'POST':
        email = request.POST.get('email')
        group = Group.objects.get(email=email)

        if group.guide == request.user.username:
            grade = True
        else:
            grade = False
        return render(request, 'fproject.html', {'group': group, 'grade': grade})
    return render(request, 'fdomain.html')

def myProjects(request):
    if request.user.is_anonymous:
        return redirect('login')
    # faculty = get_object_or_404(Faculty, email=request.user.username)
    groups = Group.objects.filter(guide=request.user.username)
    return render(request, 'fproject_overview.html', {'groups': groups, 'title': "My Projects"})

def gradeProject(request):
    if request.user.is_anonymous:
        return redirect('login')

    if request.method == 'POST':
        email = request.POST.get('email')
        group = Group.objects.get(email=email)
        group.remarks = request.POST.get('remarks')

        if request.POST.get('grade'):
            group.grade = request.POST.get('grade')

        group.save()
        return render(request, 'fproject.html', {'group': group, 'grade': True})
    return render(request, 'fdomain.html')

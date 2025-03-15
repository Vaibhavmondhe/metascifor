from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Resume, Education, Experience, Skill, Project, Certification
from django.forms import modelformset_factory

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, 'Registration successful!')
        return redirect('home')

    return render(request, 'builder/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')

    return render(request, 'builder/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

def home(request):
    resumes = Resume.objects.all().order_by('-created_at')
    return render(request, 'builder/home.html', {'resumes': resumes})

def create_resume(request):
    if request.method == 'POST':
        resume = Resume.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            linkedin=request.POST.get('linkedin', ''),
            education_level=request.POST['education_level'],
            summary=request.POST['summary'],
            objective=request.POST['objective']
        )
        messages.success(request, 'Resume created and saved successfully! You can now view or edit your resume.')
        return redirect('view_resume', resume_id=resume.id)
    return render(request, 'builder/create_resume.html')

def edit_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    if request.method == 'POST':
        resume.name = request.POST['name']
        resume.email = request.POST['email']
        resume.phone = request.POST['phone']
        resume.address = request.POST['address']
        resume.linkedin = request.POST.get('linkedin', '')
        resume.education_level = request.POST['education_level']
        resume.summary = request.POST['summary']
        resume.objective = request.POST['objective']
        resume.save()

        # Handle education
        if 'education-institution' in request.POST:
            Education.objects.create(
                resume=resume,
                institution=request.POST['education-institution'],
                degree=request.POST['education-degree'],
                field_of_study=request.POST['education-field'],
                graduation_year=request.POST['education-year'],
                start_year=request.POST['education-start-year'],
                location=request.POST['education-location'],
                gpa=request.POST.get('education-gpa', None),
                current_education=request.POST.get('education-current', False),
                achievements=request.POST.get('education-achievements', '')
            )

        # Handle experience
        if 'experience-company' in request.POST:
            Experience.objects.create(
                resume=resume,
                company=request.POST['experience-company'],
                position=request.POST['experience-position'],
                location=request.POST['experience-location'],
                start_date=request.POST['experience-start'],
                end_date=request.POST.get('experience-end', None),
                description=request.POST['experience-description'],
                achievements=request.POST.get('experience-achievements', '')
            )

        # Handle projects
        if 'project-title' in request.POST:
            Project.objects.create(
                resume=resume,
                title=request.POST['project-title'],
                description=request.POST['project-description'],
                technologies=request.POST['project-technologies'],
                start_date=request.POST['project-start'],
                end_date=request.POST.get('project-end', None),
                url=request.POST.get('project-url', '')
            )

        # Handle certifications
        if 'certification-name' in request.POST:
            Certification.objects.create(
                resume=resume,
                name=request.POST['certification-name'],
                issuing_organization=request.POST['certification-org'],
                issue_date=request.POST['certification-issue-date'],
                expiry_date=request.POST.get('certification-expiry-date', None),
                credential_id=request.POST.get('certification-id', ''),
                url=request.POST.get('certification-url', '')
            )

        messages.success(request, 'Resume updated successfully!')
        return redirect('view_resume', resume_id=resume.id)
    return render(request, 'builder/edit_resume.html', {'resume': resume})

def view_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    return render(request, 'builder/view_resume.html', {'resume': resume})

def delete_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    resume.delete()
    messages.success(request, 'Resume deleted successfully!')
    return redirect('home')

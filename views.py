from django.shortcuts import render

from .models import recruiter  ,salarys,Job_Position,projects, certificate,Contacts
# Create your views here.


def home(request):
    return render(request, 'index.html')

def my_page(request):
    return render(request, 'my_site/My_page.html')

def about_BCA(request):
    return render(request,'about_bca/about_bca.html')

def adout_mca(request):
    return render(request,'about_bca/mca.html')

def subject(request):
    return render(request,'COURSE/Subjects.html')

def syllabus(request):
    return render(request,'COURSE/Syllabus.html')

def opp_bca(request):
    return render(request,'opp__bca/opp.html')

def eligibility(request):
    return render(request,'ELIGIBILITY/eligibility.html')

def job(request):
    return render(request,'Job/job.html')

def career(request):
    return render(request,'Career/career.html')

def recruiters(request):
    var_1 =recruiter.objects.all()
    return render(request,'Recruiters/recruiters.html',{'var' : var_1})

def academic(request):
    return render(request,'Academic/academic.html')

def contact(request):
    if request.method == 'POST':
         Your_name = request.POST['Name']
         Email_address = request.POST['Email']
         Subject_name = request.POST['Subject']
         Your_Meassage = request.POST['Message']
         var_contact = Contacts(Name = Your_name,Email=Email_address,subject=Subject_name,Messages=Your_Meassage)
         var_contact.save()   
         
         return render(request, 'Contact/Thanks_page.html')
    else:
        return render(request, 'Contact/contact_us.html')
  
     

def salary(request):
    var_2 =salarys.objects.all()
    var_3 =Job_Position.objects.all()
    return render(request,'Salary/sal.html',{'vars': var_2 ,'num' : var_3} )

def certificates(request):
    cer =certificate.objects.all()
    return render(request,'my_site/Certificates.html',{'blog': cer})

def project(request):
    num = projects.objects.all()
    return render(request, 'my_site/Projects.html',{'nums': num})

          
def thank(request):
    return render(request,'Contact/Thanks_page.html')

        

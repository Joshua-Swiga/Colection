from django.shortcuts import render, HttpResponse, redirect
from .models import Home_Page, About_Page, Services_Page, Events_Page, Inquiries_and_Messages, Blog_Posts
from django.contrib import messages

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def index(request):
    
    if request.method=='POST':
        name=request.POST.get('name', " ")
        email=request.POST.get('email', " ")
        phone_number=request.POST.get('phone', " ")
        message=request.POST.get('message', " ")

        if not name.strip() or not email.strip() or not phone_number.strip() or not message.strip():
            messages.info(request, 'Please fill all the fields!')
            return redirect('index') #+'#contact'
        
        else:
            try:

                Inquiries_and_Messages.objects.create(
                    sender_name=name, 
                    sender_email=email, 
                    sender_phone_number=phone_number, 
                    sener_message=message,
                    )
                

                message = MIMEMultipart()
                message['From'] = 'testemailsender987@gmail.com'
                message['To'] = 'joshuajuniorswiga@gmail.com'
                message['Subject'] = 'Test Email'
                body = 'Function Worked.'
                message.attach(MIMEText(body, 'plain'))

                try:
                    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  
                    smtp_server.starttls()
                    smtp_server.login('testemailsender987@gmail.com', 'pema ibqw emvh lnht')
                except Exception as e:
                    print(f"Failed: {e}")
                    return

                try:
                    smtp_server.sendmail('testemailsender987@gmail.com', 'joshuajuniorswiga@gmail.com', message.as_string())
                    print("Email sent")
                except Exception as e:
                    print(f"Failed to send email: {e}")


                smtp_server.quit()


            except Exception as e:
                print(f'Failed{e}')
                messages.error(request, 'Failed to submit message. Please try again later.')
                return redirect('index') #+'#contact'
            
            
            messages.success(request, 'Your message has been submited')            
            return redirect('sucess') #+'#contact'


    elif request.method=='GET':

        home_page_data=Home_Page.objects.all()
        about_page_data=About_Page.objects.all()
        services_page_data=Services_Page.objects.all()
        event_page_data= Events_Page.objects.all()


        return render(request, 'index.html', {
            'home_data':home_page_data,
            'about_data':about_page_data,
            'services_data':services_page_data,
            'event_data':event_page_data,
    
        })
    
    
    else:
        pass #Include error message if method is not post or get...
    
    



def login_view(request):

    return render(request, 'login.html')



def calender(request):
    return render(request, 'calender.html')





def individual_event(request, pk):
    event=Events_Page.objects.get(id=pk)

    return render(request, 'event.html', {
        'event_content':event
    })


def sucess(request):
    blogs=Blog_Posts.objects.all()

    return render(request, 'sucess.html', {
        'blog_content':blogs,
    })

def individual_post(request, pk):
    individual_posts=Blog_Posts.objects.get(id=pk)

    return render(request, 'blog_post.html', {
        'content':individual_posts,
    })

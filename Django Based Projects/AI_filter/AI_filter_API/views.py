from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User

from .models import BlogPost, AboutPageContent, ContactPageContent, HomePageContent, UserQuery

#from AI_filter_API.__init__ import submit_data

import time
import requests
import json
import sys

# Create your views here.

#sys.stdout = open('logfile.txt', 'w/a', encoding='utf-8')

def post(request, pk):

    if request.method == 'GET':
        individual_content = BlogPost.objects.get(id=pk)

        return render(request, 'post.html', {
            'individual_content':individual_content,
        })

def contact (request):
    if request.method =="GET":
        contact_page_context = ContactPageContent.objects.all()
        return render(request, 'contact.html', {
            contact_page_context: "C_context"
        })
    
    else:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            message = request.POST.get('message')

            if name is not None and email is not None and phone_number is not None and message is not None:
                UserQuery.objects.create(
                    name = name,
                    email = email,
                    phone_number = phone_number,
                    message = message,
                )
                messages.info(request, "Message Sent Sucessfully!")
                return redirect('index.html')


def about(request):
    if request.method == "GET":
        about_page_context = AboutPageContent.objects.all()
        
        return render(request, 'about.html',{
            about_page_context:'A_contect'
        })


def index(request, strength: str = 'Balanced', url: str= "https://api.undetectable.ai/submit", api_key ='1710536494338x699896943833058400', document_url : str ="https://api.undetectable.ai/document"):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content', None)
        input_complexity = request.POST.get('complexity_user_input', 'Marketing') # Collects from radio buttons
        input_purpose = request.POST.get('purpose_user_input', 'Marketing Material') # Collects from radio buttons
        strength = request.POST.get('', 'Balanced')

        list_of_complexity_level = {
            1: "HighSchool", 
            2: "University", 
            3: "Doctorate", 
            4: "Journalist", 
            5: "Marketing",
            }
        
        list_of_purpose = {
            1: "GeneralWriting", 
            2: "Essay", 
            3: "Article", 
            4: "MarketingMaterial", 
            5: "Story", 
            6: "CoverLetter", 
            7: "Report", 
            8: "BusinessMaterial", 
            9: "LegalMaterial"
            }

        
        for item in list_of_complexity_level.values():
            if item == input_complexity:
                complexity = item
                break
                

        for element in list_of_purpose.values():
            if element == input_purpose:
                purpose = element
                break

        try:
            if content is not None and complexity is not None and purpose is not None:
                
                payload = json.dumps({
                    "content" : content,  
                    "readability" : complexity,
                    "purpose" : purpose,
                    "strength" : strength,
                })

                headers = {
                    'api-key' : api_key,
                    'Content-Type' : 'application/json'
                }

                response = requests.post(url, headers=headers, data=payload)

                if response.status_code == 200:
                    response_json = response.json()

                    id_output = response_json.get('id')
                    status_output = response_json.get('status')

                    if id_output is not None and status_output is not None:
                        print(f"Submission successful. ID: {id_output}, Status: {status_output}")

                        # Wait for the document to be processed
                        time.sleep(5)

                        document_payload = json.dumps({"id": id_output})

                        document_headers = {
                            'api-key': api_key,
                            'Content-Type': 'application/json',
                        }

                        document_response = requests.post(document_url, headers=document_headers, data=document_payload)

                        if document_response.status_code == 200:
                            document_response_json = document_response.json()
                            document_status = document_response_json.get('status')

                            # Checks whether the statuse of complition is done
                            while document_status != 'done':
                                time.sleep(2)

                                # sending and recieving request
                                document_response = requests.post(document_url, headers=document_headers, data=document_payload)

                                # Recieves the document and parses it to read the statuse
                                document_response_json = document_response.json()
                                document_status = document_response_json.get('status')

                            # If statuse evaluates to True, retrieve the parsed json document
                            document_output = document_response_json.get('output')

                            print("Document processing completed:")
                            #messages.info(request, f"Document processing statuse: {document_status.capitalize()}. \nID: {id_output}")
                            
                            humanized_content = document_output # Contains the humanized information (Pass as context)
            
                            try:
                                # Saves the data to the database after processing
                                BlogPost.objects.create(
                                    title = title,
                                    content = humanized_content,
                                )

                                # Retrieves the data from the database
                                H_post = BlogPost.objects.all()
                                decorator = HomePageContent.objects.all()
                                
                                # Renders the information on the frontpage
                                return render (request, 'index.html', {
                                    'H_post':H_post,
                                    'decorator':decorator,
                                    })
                            
                            except Exception as e:
                                print("There was an issue: {e}")
                                messages.info(request, 'There was an issue!')
                                return redirect('index')

                        # Running Exceptions...
                        else:
                            print(f"Failed to retrieve document. Status code: {document_response.status_code}")
                            messages.info(request, "Failed to retrieve document.")

                            return redirect ('index')
                    else:
                        print("Invalid response received from the server.")
                        messages.info(request, "Invalid response received from the server.")
                        return redirect('index')
                else:
                    print(f"Error: {response.status_code}. Failed to submit data.")
                    messages.info(request, f"Error: {response.status_code}. Failed to submit data.")
                    return redirect('index')

        except Exception as e:
            print(f"An error occurred: {e}")
            messages.info(request, f"An error occurred: {e}")
            
            return redirect('index')
    
    else:
        if request.method == "GET":
            H_post = BlogPost.objects.all()
            H_decorator = HomePageContent.objects.all() 


            return render (request, 'index.html',{ 
                        'H_post':H_post,
                        'decorator':H_decorator,
                        })
        
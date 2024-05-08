import requests
import json
#from content import data
import time

def commandline():
    complexity_level = {
        1: "High School", 
        2: "University", 
        3: "Doctorate", 
        4: "Journalist", 
        5: "Marketing",
    }

    purpose = {
        1: "General Writing", 
        2: "Essay", 
        3: "Article", 
        4: "Marketing Material", 
        5: "Story", 
        6: "Cover Letter", 
        7: "Report", 
        8: "Business Material", 
        9: "Legal Material"
    }

    try:
        print("Welcome!")

        for number, complexity in complexity_level.items():
            print(f"{number}: {complexity}")

        complexity_user_input = int(input("Please pick the level of complexity: "))

        if complexity_user_input not in complexity_level.keys():
            print("Please select a valid option!")
            return None

        for purpose_number, individual_purpose in purpose.items():
            print(f"{purpose_number}: {individual_purpose}")

        purpose_user_input = int(input("Please pick the purpose of the project: "))

        if purpose_user_input not in purpose:
            print("Please select a valid option!")
            return None
        else:
            options = [
                complexity_level[complexity_user_input], 
                purpose[purpose_user_input],
            ]
            return options

    except Exception as e:
        print(f"There was an issue with: {commandline}, {e}")

def submit_data(strength: str = 'Balanced', url="https://api.undetectable.ai/submit", api_key='1710536494338x699896943833058400', document_url="https://api.undetectable.ai/document"):
    try:
        selected_output = commandline()
        if not selected_output:
            print("Invalid input. Please try again.")
            return None
        
        complexity_user_input = selected_output[0]
        purpose_user_input = selected_output[1]

        payload = json.dumps({
            "content": data,  
            "readability": complexity_user_input,
            "purpose": purpose_user_input,
            "strength": strength,
        })

        headers = {
            'api-key': api_key,
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            response_json = response.json()
            id_output = response_json.get('id')
            status_output = response_json.get('status')

            if id_output and status_output:
                print(f"Submission successful. ID: {id_output}, Status: {status_output}")

                # Wait for the document to be processed
                time.sleep(15)

                document_payload = json.dumps({"id": id_output})
                document_headers = {
                    'api-key': api_key,
                    'Content-Type': 'application/json',
                }

                document_response = requests.post(document_url, headers=document_headers, data=document_payload)

                if document_response.status_code == 200:
                    document_response_json = document_response.json()
                    document_status = document_response_json.get('status')

                    while document_status != 'done':
                        time.sleep(10)

                        document_response = requests.post(document_url, headers=document_headers, data=document_payload)

                        document_response_json = document_response.json()
                        document_status = document_response_json.get('status')

                    document_output = document_response_json.get('output')

                    print("Document processing completed:")
                    print(document_output)
                    
                else:
                    print(f"Failed to retrieve document. Status code: {document_response.status_code}")
            else:
                print("Invalid response received from the server.")
                return None
        else:
            print(f"Error: {response.status_code}. Failed to submit data.")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

#test1 = submit_data()

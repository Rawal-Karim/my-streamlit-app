import requests

# Replace with actual values
api_key = '<gD8g6wyV3tWcpJ78s70hdBJz53XJoSBf>'
external_user_id = '<6791397f03ff04d58aa7ed47>'
query = 'Put your query here'

# Step 1: Create Chat Session
create_session_url = 'https://api.on-demand.io/chat/v1/sessions'
create_session_headers = {'apikey': api_key}
create_session_body = {"pluginIds": [], "externalUserId": external_user_id}

response = requests.post(create_session_url, headers=create_session_headers, json=create_session_body)

if response.status_code == 201:
    session_id = response.json()['data']['id']
    
    # Step 2: Submit Query
    submit_query_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
    submit_query_headers = {'apikey': api_key}
    submit_query_body = {
        "endpointId": "predefined-openai-gpt4o",
        "query": query,
        "pluginIds": ["plugin-1712327325", "plugin-1713962163", "plugin-1716334779"],
        "responseMode": "sync"
    }

    response = requests.post(submit_query_url, headers=submit_query_headers, json=submit_query_body)

    if response.status_code == 200:
        print('Query submitted successfully.')
        print('Response:', response.json())
    else:
        print('Failed to submit query. Status code:', response.status_code)
else:
    print('Failed to create session. Status code:', response.status_code)

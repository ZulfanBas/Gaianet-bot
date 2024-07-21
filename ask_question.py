import requests

def ask_question(question):
    url = "https://knowledge2.gaianet.network/v1/chat/completions"
    payload = {
        "messages": [
            {"role": "system", "content": "You are an AI assistant designed to provide clear, concise, and accurate answers to user queries. Your primary functions include retrieving relevant information from the provided RAG (Retrieval-Augmented Generation) data and utilizing your pre-training data when necessary. Make your answer as short as possible that suitable for the length of a tweet. If no relevant information is found, you will inform the user that you are not familiar with the knowledge."},
            {"role": "user", "content": question}
        ]
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response content: {response.content}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    
    return None

def save_response_to_file(response, filename):
    try:
        # Extract the assistant's answer from the response
        answer = response['choices'][0]['message']['content']
        with open(filename, 'w') as file:
            file.write(answer)
        print(f"Response saved to {filename}")
    except Exception as e:
        print(f"Failed to save response to file: {e}")

if __name__ == "__main__":
    question = input("Enter your question: ")
    response = ask_question(question)
    if response:
        save_response_to_file(response, "response.txt")
    else:
        print("Failed to get a response from the API.")

# Rule-Based Chatbot with Twilio Sandbox Integration

I have created a rule-based chatbot and integrated it with the Twilio API to send custom WhatsApp messages to verified numbers.

The project requires Twilio credentials to interact with the Twilio service.

## Features

- Rule-based chatbot for predefined responses
- Integration with Twilio API for WhatsApp messaging
- Custom messages to verified numbers

## Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Create a Virtual Python Environment:
    ```bash
    python -m venv venv # For Mac/Linux/Unix
    .\venv\Scripts\activate # For Windows
    ```
    
3. Install the required dependencies:
    ```bash
    pip install twilio
    ```
4.Set Twilio credentials for use in the Python script
    (Replace with your actual Twilio SID and Auth Token)
'''
    export TWILIO_ACCOUNT_SID="your_account_sid_here"
    export TWILIO_AUTH_TOKEN="your_auth_token_here"
'''
## Usage

1. Run the chatbot:
    ```bash
    python chatbot.py
    ```
2. Interact with the chatbot and send custom WhatsApp messages.

## License

This project is licensed under the MIT License.

# Rule-Based Chatbot with Twilio Sandbox Integration

This is a rule-based chatbot integrated with the Twilio API to send custom WhatsApp messages to verified numbers.

## Features

- Rule-based chatbot with predefined responses
- Twilio API integration for WhatsApp messaging
- Ability to send custom messages to verified numbers

---

## *Setup and Installation (Terminal Commands)*

### *1. Clone the Repository*
Open a terminal and run:

```bash
git clone https://github.com/Sanjay1712KSK/Python
```
### *2. Change the directory*
Open a terminal and run:
```bash
cd Python
```

### *3. Create a Virtual Environment*
Open a terminal and run:
```bash
python3 -m venv venv
source venv/bin/activate # For Mac/Linux

python -m venv venv
venv\Scripts\activate # For Windows
```

### *4. Install Required Dependencies*
Open a terminal and run:
```bash
pip install twilio
```

### *5. Set Up Twilio Credentials*
Open a terminal and run:
```bash
export TWILIO_ACCOUNT_SID="your_account_sid_here"
export TWILIO_AUTH_TOKEN="your_auth_token_here" #For Mac/Linux

set TWILIO_ACCOUNT_SID="your_account_sid_here"
set TWILIO_AUTH_TOKEN="your_auth_token_here" # For Windows - (cmd)

$env:TWILIO_ACCOUNT_SID="your_account_sid_here"
$env:TWILIO_AUTH_TOKEN="your_auth_token_here" # For Windows - (Powershell)

```
### *6. Verify Your Number in Twilio Sandbox*
  Before sending messages via WhatsApp, ensure your number is verified.
Open a terminal and run:

```bash
xdg-open "https://www.twilio.com/console"  # Linux
open "https://www.twilio.com/console"      # macOS
start https://www.twilio.com/console       # Windows

```
Go to Messaging → Try It Out → WhatsApp Sandbox.
Follow Twilio’s instructions to verify your number.

### *7. Running the Chatbot*
  Once everything is set up, run the chatbot
Open a terminal and run:
```bash
python chatbot.py
```

The chatbot will now: ✅ Listen for user inputs
✅ Sends custom WhatsApp messages using Twilio Sandbox number to the verified numbers


### *8. Stopping the Chatbot*
Open a terminal and run:
```bash
CTRL + C  # Stop the script in the terminal
```
To deactivate the virtual environment:
```bash
deactivate
```

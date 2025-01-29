def chatbot(usr_in):
    usr_in=usr_in.lower()
    if usr_in in ["hello","hi","hey","yo"]:
        return "Hare! Bhaiyaa vaanga vaanga!!!"
    elif usr_in =="epdi iruka":
        return "Nala iruken da"
    elif usr_in =="hey yo yo puduchathu naan thaan":
        return "hey hey muduchathu naan thaan sirutha"
    elif usr_in =="nee yaaru da":
        return "naan thaan da leo... Leo das..... RATATA RATATA ....."
    elif usr_in == "dei sombu":
        return "dei sombu illa da... Naan thaan da Leo...."
    elif usr_in == "i need to send a whatsapp message":
        return "Number sollu da."
    elif usr_in == "how to send whatsapp message":
        return "ask me - i need to send a whatsapp message"
    elif usr_in == "help":
        return "Enna help pannanum?? seri seri the questions that you can ask me are how to send whatsapp message,hello,hi,hey,yo,epdi iruka,hey yo yo puduchathu naan thaan,nee yaaru da,dei sombu,bye..."
    else:
        return "Enna da etho soldra ennaku thaan sariya puriyala... Naan thaan da Leo.... thirupi soldriya da olunga??"
print("LEO DAS: Vannakam di mapla na thaan rule based chatbot... help nu search pannu enna pathi therunjuko!!...")

import bot
import twc
while True:
    usr_in = input("User: ")
    if usr_in.lower() == "bye":
        print("LEO DAS: Poitu varen da mapla... Bye bye")
        break
    elif usr_in == "i need to send a whatsapp message":
        print("LEO DAS: Number sollu da.")
        nu = input('Whatsapp number:')
        num='whatsapp:'+nu
        msg = input("msg: ")
        twc.t(msg,num)
        print("LEO DAS: Message sent!")
        break
    resp=bot.chatbot(usr_in)
    print("LEO DAS:",resp)

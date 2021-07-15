# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

#class ActionSubmit(Action):
#    def name(self) -> Text:
#        return "action_submit"

#    def run(
#        self,
#        dispatcher,
#        tracker: Tracker,
#        domain: "DomainDict",
#    ) -> List[Dict[Text, Any]]:

#        SendEmail(
#            tracker.get_slot("email"),
#            tracker.get_slot("subject"),
#            tracker.get_slot("message")
#        )
#        dispatcher.utter_message("Thanks for providing the details. We have sent you a mail at {}".format(tracker.get_slot("email")))
#        return []



# def SendEmail(toaddr,subject,message):
 #   fromaddr = "xyzinternational.s@gmail.com"
    # instance of MIMEMultipart
 #   msg = MIMEMultipart()

    # storing the senders email address
#    msg['From'] = fromaddr

    # storing the receivers email address
#    msg['To'] = toaddr

    # storing the subject
#    msg['Subject'] = subject

    # string to store the body of the mail
#    body = message

    # attach the body with the msg instance
#    msg.attach(MIMEText(body, 'plain'))

#    # open the file to be sent
#    # filename = "/home/ashish/Downloads/webinar_rasa2_0.png"
#    # attachment = open(filename, "rb")
#    #
#    # # instance of MIMEBase and named as p
#    # p = MIMEBase('application', 'octet-stream')
#    #
#    # # To change the payload into encoded form
#    # p.set_payload((attachment).read())
#    #
#    # # encode into base64
#    # encoders.encode_base64(p)
#    #
#    # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#    #
#    # # attach the instance 'p' to instance 'msg'
#    # msg.attach(p)
#
#    # creates SMTP session
#    s = smtplib.SMTP('smtp.gmail.com', 587)

#    # start TLS for security
#    s.starttls()
#

#    # Authentication
#    try:
#        s.login(fromaddr, "internationalschool")
#
#        # Converts the Multipart msg into a string
#        text = msg.as_string()
#
#        # sending the mail
#        s.sendmail(fromaddr, toaddr, text)
#    except:
#        print("An Error occured while sending email.")
#    finally:
#        # terminating the session
#        s.quit()

class zoom(Action):
    def name(self) -> Text:
        return "show_zoom"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("class")
        D={"11A":"https://i.imgur.com/w5Zjzcx.jpeg","11B":"https://i.imgur.com/QfTXIXb.jpeg","11C":"https://i.imgur.com/z8RjKyL.jpeg","11D":"https://i.imgur.com/itgvPS0.jpeg","11E":"https://i.imgur.com/dTYhTSH.jpeg","12A":"https://i.imgur.com/FBZjOkU.jpeg","12B":"https://i.imgur.com/wjPFf7b.jpeg","12C":"https://i.imgur.com/gvcKsf1.jpeg","12D":"https://i.imgur.com/23tVRBO.jpeg","12E":"https://i.imgur.com/n0Znsa2.jpeg"}
        for dict in D.keys():
            print(name)
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(image=val)

        return[]

class email(Action):
    def name(self) -> Text:
        return "show_email"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("class")
        D={"11A":"https://i.imgur.com/Miol4XI.jpeg","11B":"https://i.imgur.com/Miol4XI.jpeg","11C":"https://i.imgur.com/Miol4XI.jpeg","11D":"https://i.imgur.com/Miol4XI.jpeg","11E":"https://i.imgur.com/Miol4XI.jpeg","12A":"https://i.imgur.com/Miol4XI.jpeg","12B":"https://i.imgur.com/Miol4XI.jpeg","12C":"https://i.imgur.com/Miol4XI.jpeg","12D":"https://i.imgur.com/Miol4XI.jpeg","12E":"https://i.imgur.com/Miol4XI.jpeg"}
        for dict in D.keys():
            print(name)
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(image=val)

        return[]

class syllabus(Action):
    def name(self) -> Text:
        return "show_syllabus"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("class")
        D={"11":"utter_exam","12":"utter_exam","11A":"utter_exam","11B":"utter_exam","11C":"utter_exam","11D":"utter_exam","11E":"utter_exam","12A":"utter_exam","12B":"utter_exam","12C":"utter_exam","12D":"utter_exam","12E":"utter_exam"}
        for dict in D.keys():
            print(name)
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(response=val)

        return[]

class exam(Action):
    def name(self) -> Text:
        return "show_exam"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("exam")
        if tracker.get_slot("class") in ["11","11A", "11B", "11C", "11D", "11E"]:
            D={"periodic":"utter_subject_11","half yearly":"utter_subject_11","preboard":"utter_subject_11","final":"utter_subject_11"}
            for dict in D.keys():
                print(name)            
                if name==dict:
                    val=D[dict]
                    print(val)
                    dispatcher.utter_message(response=val)

        elif tracker.get_slot("class") in ["12","12A", "12B", "12C", "12D", "12E"]:
            D={"periodic":"utter_subject_12","half yearly":"utter_subject_12","preboard":"utter_subject_12","final":"utter_subject_12"}
            for dict in D.keys():
                print(name)
                if name==dict:
                    val=D[dict]
                    print(val)
                    dispatcher.utter_message(response=val)  

            return[]

class subject(Action):
    def name(self) -> Text:
        return "show_final_11"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("subject")
        D={"maths":"https://i.imgur.com/h4Hcf6Z.jpeg","phy":"https://i.imgur.com/rcV7Hs2.jpeg","chem":"https://i.imgur.com/osH6KCz.jpeg","eng":"https://i.imgur.com/Aht65uG.jpeg","cs":"https://i.imgur.com/Uy3yrlm.jpeg"}
        for dict in D.keys():
            print(name)
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(image=val)

class subject(Action):
    def name(self) -> Text:
        return "show_final_12"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("subject")
        D={"maths":"https://i.imgur.com/h4Hcf6Z.jpeg","phy":"https://i.imgur.com/rcV7Hs2.jpeg","chem":"https://i.imgur.com/osH6KCz.jpeg","eng":"https://i.imgur.com/Aht65uG.jpeg","cs":"https://i.imgur.com/Uy3yrlm.jpeg"}
        for dict in D.keys():
            print(name)
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(image=val)

class event(Action):
    def name(self) -> Text:
        return "show_event"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("event")
        D={"mun":"https://i.imgur.com/FTeMwT4.jpeg","fest":"https://i.imgur.com/l5wKsMm.jpeg","quiz":"https://i.imgur.com/RtIGTI5.jpeg","art":"https://i.imgur.com/JE21Mej.jpeg"}
        for dict in D.keys():
            print(name)
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(image=val)

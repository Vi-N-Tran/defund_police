# for i in range(1, 4):
#     try:
#         password = input("input a number")
#         break
#     except:
#         print("Error with inputting password. Try again. This is your try " + str(i) + "/3")
# print(password)
# if len(password) <= 0:
#     quit()
# else:
#     print("342")

# res = "NNN"
# print(res.lower())
# def file():
#     response = ""
#     message = ""
#     while response.lower() != "y" and response.lower() != "n":
#         response = input("Would you like mailbot to write emails for you? (y/n): ")
#         if response == 'n':
#             for i in range(50):
#                 filename = input("What is the name of your txt file?: ")
#                 try:
#                     with open(filename, 'r', encoding = 'utf-8-sig') as fd:
#                         message = fd.read()
#                         break
#                 except:
#                     print("Incorrect file name. Please try again")
#                     if input("Enter any key to try again. Enter 'q' to quit") == "q":
#                         quit()
#
#     return message
#
# print(file())
# file = open("/Users/vitran/PycharmProjects/ignore/test/example", "r")
import messages, recipients, states, smtplib, ssl, sys, time
from email.message import EmailMessage

# def ask_rep():
#     recv = set()
#     cart = set()
#     more_state = True
#
#     # Choose a state
#     while more_state:
#         more_city = True
#         print("Which state officials do you want to send emails to?")
#         state_options = { v:k for v,k in enumerate(recipients.get_states()) }
#         for idx, opt in state_options.items():
#             print(idx, "->", opt)
#         print("Enter blank (nothing) when done. \n")
#
#         if len(cart) > 0:
#             print(f'Cities chosen: {cart}')
#         state_idx = input("\nType the number corresponding to the state here: ")
#
#         if len(str(state_idx)) == 0:
#             more_state = False
#         else:
#             # 0 -> All States
#             if int(state_idx) == 0:
#                 recv.update(recipients.get_all())
#             # (1 to N) -> Individual States
#             elif int(state_idx) in state_options.keys():
#                 state = state_options[int(state_idx)]
#                 subcart = set()
#
#                 # Choose a city
#                 while more_city:
#                     city_options = { v:k for v,k in enumerate(recipients.get_cities(state)) }
#
#                     # Print question for city
#                     print("Which city officials do you want to send emails to?")
#                     for idx, opt in city_options.items():
#                         print(idx, "->", opt)
#                     print("Enter blank (nothing) when done. \n")
#
#                     # Ask user and print confirmation of cities
#                     if subcart:
#                         print(f'Cities chosen: {subcart}')
#                     city_idx = input("\nType the number corresponding to the city here: ")
#
#                     # get out of loop or get the city
#                     if len(str(city_idx)) == 0:
#                         print("get out")
#                         more_city = False
#                     else:
#                         if int(city_idx) == 0:
#                             subcart.update(recipients.get_cities(state))
#                             subcart.remove('Select All')
#                             recv.update(recipients.get_state(state))
#                         elif int(city_idx) in city_options.keys():
#                             subcart.add(city_options[int(city_idx)])
#                             recv.update(recipients.get_city(state, city_options[int(city_idx)]))
#                         else:
#                             print("\033[1;31;48mWe don't have that CITY number. Please input the correct number")
#                             print("\033[1;37;48m")
#                         for city in subcart:
#                             cart.add("%s, %s" % (city, states.abbreviate(state)))
#                         print(f'{len(recv)} recipients selected.\n')
#             else:
#                 print("\033[1;31;48mWe don't have that STATE number. Please input the correct number")
#                 print("\033[1;37;48m")
#     print("\nYou have chosen " + str(len(recv)) + " recipients")
#     print("Thank you for choosing you recipients")
#
#     return recv
#
#
# reps = ask_rep()
#
# for item in reps:
#     print(item)

# def prompt_email():
#
#     print("\nWhat would you like the subject (title) of your email to be?")
#     subject = input("Type here and press enter (if blank, a random one will be generated): ")
#     if len(subject) == 0:
#         subject = messages.gen_subject()
#
#     print("\nMailbot can write unique emails addressed personally to each lawmaker.")
#     print(
#         "However, if you would like to write your own message, please save it in a .txt file. The easiest way to do this is to just write your message in example.txt.\n")
#     response = ""
#     msg = ""
#     while response.lower() != "y" and response.lower() != "n":
#         response = input("Would you like mailbot to write emails for you? (y/n): ")
#         if response.lower() == "y":
#             with open("template.txt", 'r', encoding='utf-8-sig') as fd:
#                 msg = fd.read()
#         elif response == 'n':
#             for i in range(50):
#                 filename = input("What is the name of your txt file?: ")
#                 try:
#                     with open(filename, 'r', encoding='utf-8-sig') as fd:
#                         msg = fd.read()
#                         break
#                 except:
#                     print("Incorrect file name. Please try again")
#                     if input("Enter 'n' to try again. Enter 'q' to quit") == "q":
#                         quit()
#
#     return subject, msg
#
#
#
#
# def send():
#     port = 465  # standard port for SMTP over SSL
#     smtp_server = "smtp.gmail.com"
#
#     send = 0
#     recv = {('Name of rep', 'location rep resides', 'Vi.n.tran23@dartmouth.edu')}
#     subject, message = prompt_email()
#     src_email, password = "Vi.n.tran1212@gmail.com", "Ivnartivnart12"
#
#     while True:
#         try:
#             # create a secure SSL context
#             context = ssl.create_default_context()
#
#             with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#                 server.login(src_email, password)
#                 while recv:
#                     recipient = recv.pop()
#                     dst_name = recipient[0]
#                     location = recipient[1]
#                     dst_email = recipient[2]
#
#                     msg = EmailMessage()
#
#                     msg['Subject'] = subject if subject else messages.gen_subject()
#                     msg['From'] = src_email
#                     msg['To'] = dst_email
#
#                     body = messages.attach_greeting(dst_name, message) if message else messages.gen_body(src_name, dst_name,
#                                                                                                          location)
#                     msg.set_content(body)
#                     print(msg.as_string())
#
#                     server.send_message(msg)
#                     send += 1
#             break
#         except smtplib.SMTPException:
#             print("Unexpected error... trying again in 10 seconds.")
#             time.sleep(10)

# with open("template.txt", 'r', encoding='utf-8-sig') as fd:
#     residency = "California"
#     msg = fd.read()
#     msg = msg.replace("My name is", "name")
#     msg = msg.replace("[RESIDENCY]", "California")
#     msg = msg.replace(" and I am from " + residency, "")
#
#
# print(msg)

police_budget = "1,318,447,965"
police_budget_int = int(police_budget.replace(",",""))
print(police_budget)
print(police_budget_int)
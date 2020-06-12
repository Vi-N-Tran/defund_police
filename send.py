#!/usr/bin/env python3
import messages, recipients, smtplib, ssl, states, sys, time
from getpass import getpass
from email.message import EmailMessage


def print_barrier():
    print("======================================================")


def prompt_name():
    name = ""
    # Validate name is not blank
    while len(name) <= 0:
        name = input("Type your name and press enter: ")
    return name

def prompt_residency():
    city = ""
    while len(city) <= 0:
        city = input("Type your residency (city where you live) and press enter: ")
    return city


def prompt_login():
    print_barrier()

    # Get email
    email = input("Type your email and press enter: ")
    while "@gmail" not in email:
        print("Please enter a GMAIL username")
        email = input("Type your email and press enter: ")

    # Get password
    password = ""
    for i in range(1, 4):
        try:
            password = getpass("Type your password and press enter: ")
            break
        except:
            print("Error with inputting password. Try again. This is your try " + str(i) + "/3")
    if len(password) <= 0:
        quit()
    else:
        print_barrier()
        return email, password


def prompt_email(name, residency):
    print("\nWhat would you like the subject (title) of your email to be?")
    subject = input("Type here and press enter (if blank, a random one will be generated): ")
    if len(subject) == 0:
        subject = messages.gen_subject()

    print("\nMailbot can write emails addressed personally to each lawmaker.")
    print(
        "However, if you would like to WRITE YOUR OWN message, please save it in a .txt file.\nThe easiest way to do this is to just write your message in example.txt.\n")
    response = ""
    msg = ""
    while response.lower() != "y" and response.lower() != "n":
        response = input("Would you like mailbot to write emails for you? (y/n): ")
        if response.lower() == "y":
            with open("template.txt", 'r', encoding='utf-8-sig') as fd:
                msg = fd.read()
                msg = msg.replace("[PERSON-NAME]", name)
                msg = msg.replace("[RESIDENCY]", residency)
        elif response == 'n':
            for i in range(50):
                filename = input("What is the name of your txt file?: ")
                try:
                    with open(filename, 'r', encoding='utf-8-sig') as fd:
                        msg = fd.read()
                except:
                    print("Incorrect file name. Please try again")
                    if input("Enter 'n' to try again. Enter 'q' to quit") == "q":
                        quit()

    return subject, msg


def prompt_recipients():
    recv = set()
    cart = set()
    more_state = True

    # Choose a state
    while more_state:
        more_city = True
        print("Which state officials do you want to send emails to?")
        state_options = {v: k for v, k in enumerate(recipients.get_states())}
        for idx, opt in state_options.items():
            print(idx, "->", opt)
        print("Enter blank (nothing) when done. \n")

        if len(cart) > 0:
            print(f'Cities chosen: {cart}')
        state_idx = input("\nType the number corresponding to the state here: ")

        if len(str(state_idx)) == 0:
            more_state = False
        elif int(state_idx) == 0:
            cart.update(recipients.get_states())
            cart.remove('Select All')
            for state in cart:
                recv.update(recipients.get_state(state))
            more_state = False
        else:
            # 0 -> All States
            if int(state_idx) == 0:
                recv.update(recipients.get_all())
            # (1 to N) -> Individual States
            elif int(state_idx) in state_options.keys():
                state = state_options[int(state_idx)]
                subcart = set()

                # Choose a city
                while more_city:
                    city_options = {v: k for v, k in enumerate(recipients.get_cities(state))}

                    # Print question for city
                    print("Which city officials do you want to send emails to?")
                    for idx, opt in city_options.items():
                        print(idx, "->", opt)
                    print("Enter blank (nothing) when done. \n")

                    # Ask user and print confirmation of cities
                    if subcart:
                        print(f'Cities chosen: {subcart}')
                    city_idx = input("\nType the number corresponding to the city here: ")

                    # get out of loop or get the city
                    if len(str(city_idx)) == 0:
                        more_city = False
                    else:
                        if int(city_idx) == 0:
                            subcart.update(recipients.get_cities(state))
                            subcart.remove('Select All')
                            recv.update(recipients.get_state(state))
                        elif int(city_idx) in city_options.keys():
                            subcart.add(city_options[int(city_idx)])
                            recv.update(recipients.get_city(state, city_options[int(city_idx)]))
                        else:
                            print("\033[1;31;48mWe don't have that CITY number. Please input the correct number")
                            print("\033[1;37;48m")
                        for city in subcart:
                            cart.add("%s, %s" % (city, states.abbreviate(state)))
                        print(f'{len(recv)} recipients selected.\n')
            else:
                print("\033[1;31;48mWe don't have that STATE number. Please input the correct number")
                print("\033[1;37;48m")
    print("\nYou have chosen " + str(len(recv)) + " recipients")
    print("Thank you for choosing you recipients")

    return recv


# Main

def send():
    port = 465  # standard port for SMTP over SSL
    smtp_server = "smtp.gmail.com"

    send = 0
    name = prompt_name()
    residency = prompt_residency()
    recv = prompt_recipients()
    subject, message = prompt_email(name, residency)
    src_email, password = prompt_login()

    while True:
        try:
            # create a secure SSL context
            context = ssl.create_default_context()

            # open smtplib, a client object to send emails. -> take in server and port to send from
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(src_email, password)

                # Take info from recipients file
                while recv:
                    recipient = recv.pop()
                    recv_name = recipient[0]
                    location = recipient[1]
                    dst_email = recipient[2]
                    police_budget = recipient[3]
                    total_budget = recipient[4]

                    police_budget_int = int(police_budget.replace(",", ""))
                    total_budget_int = int(total_budget.replace(",", ""))
                    percent = round(100*(police_budget_int/total_budget_int), 2)


                    msg = EmailMessage()

                    if len(subject) >0:
                        msg['Subject'] = subject
                    else:
                        msg['Subject'] = messages.gen_subject()
                    msg['From'] = src_email
                    msg['To'] = dst_email

                    message = message.replace("[POLICE-BUDGET]", police_budget)
                    message = message.replace("[TOTAL-BUDGET]", total_budget)
                    message = message.replace("[PERCENT]", str(percent))
                    message = message.replace("[CITY-NAME]", location)
                    if residency.lower() != location.lower():
                        message = message.replace(" and I am from " + residency + ".", " and")
                        message = message.replace("member of this community", "citizen")
                    body = "Dear " + recv_name + " of " + location + ",\n\n" + message

                    msg.set_content(body)
                    print(msg.as_string())

                    server.send_message(msg)
                    send += 1
            break
        except smtplib.SMTPException:
            print("Unexpected error... trying again in 10 seconds.")
            print("Are you running this program in terminal?")
            time.sleep(10)

    print_barrier()
    print(f'\nSuccessfully sent {send} emails!\n')
    print_barrier()

send()
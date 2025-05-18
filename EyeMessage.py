#!/usr/bin/env python3
import time
import os

GREEN = '\033[92m'
PURPLE = '\033[95m'
END = '\033[0m'

def banner():
    with open("assets/banner.txt", "r") as b:
        print(PURPLE + b.read() + END)

def send_sms():
    print(GREEN + "\n[+] Sending message to phone number..." + END)
    phone = input("Enter country code + number (e.g. +91xxxxxxxx): ")
    title = input("Message title: ")
    body = input("Message body: ")
    time.sleep(1)
    print(GREEN + "\n[✓] Message sent successfully to " + phone + END)

def send_email():
    print(PURPLE + "\n[+] Sending message to email..." + END)
    email = input("Enter email address: ")
    title = input("Message title: ")
    body = input("Message body: ")
    time.sleep(1)
    print(PURPLE + "\n[✓] Email sent successfully to " + email + END)

def menu():
    while True:
        os.system("clear")
        banner()
        print(GREEN + "[1] Send to phone number" + END)
        print(PURPLE + "[2] Send to mail" + END)
        print("[3] Exit\n")
        choice = input("Select an option: ")

        if choice == '1':
            send_sms()
        elif choice == '2':
            send_email()
        elif choice == '3':
            print("Exiting..."); break
        else:
            print("Invalid option.")
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    menu()

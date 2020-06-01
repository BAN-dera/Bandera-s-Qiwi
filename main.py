from SimpleQIWI import *
import sys

token = input("\nQIWI Token: ")
phone = input("Phone number: ")

api = QApi(token = token, phone = phone)

while True:
	print("\n-------------------------------------------------------------------------")
	print("[1] Balance [2] Change token and phone number [3] Payments [4] Send money")
	print("-------------------------------------------------------------------------\n")

	command = input("$")

	if command == "1" or command.lower() == "balance":
		print("")
		print(api.balance)

	elif command == "2" or command.lower() == "change" or command.lower() == "change parametres":
		token = input("\nQIWI Token: ")
		phone = input("Phone number: ")

	elif command == "3" or command.lower() == "payments":
		print(api.payments)

	elif command == "4":
		pphone = input("\nPhone number: ")
		pamount = input("How many money: ")
		pcomment = input("Comment: ")

		api.pay(account = pphone, amount = pamount, comment = pcomment)

	elif command.lower() == "exit":
		sys.exit()

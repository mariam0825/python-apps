#Nokia 3310 Menu Functions.

def phone_book():
	while True:
		phone_book_menu = """
		Press 1 : Search
		Press 2 : Service Nos
		Press 3 : Add name
		Press 4 : Erase
		Press 5 : Edit
		Press 6 : Assign
		Press 7 : Send b'card
		Press 8 : Options
		Press 9 : Speed dials
		Press 10 : Voice tags
	Press 0 to Go Back
		"""
		print(phone_book_menu)
		phone_book_choice = int(input("Press a number: "))

		match phone_book_choice:
			case 8:
				phone_book_options()
			case 0:
				return
			case _:
				print("Invalid choice.")


def phone_book_options():
	while True:
		print("Options")
		options_choice = """
			Press 1 : Type of view
			Press 2 : Memory Status
	Press 0 to go Back
		"""
		print(options_choice)
		options_choice_pick = int(input("Press a number: "))

		match options_choice_pick:
			case 0:
				return
			case _:
				print("Invalid choice.")


def messages():
	print("Messages")
	while True:
		messages_menu = """
			Press 1 : Write messages
			Press 2 : Inbox
			Press 3 : Outbox
			Press 4 : Picture messages
			Press 5 : Templates
			Press 6 : Smileys
			Press 7 : Message settings
			Press 8 : Info service
			Press 9 : Voice mailbox number
			Press 10 : Service command editor
	Press 0 to Go Back
		"""
		print(messages_menu)
		messages_settings_choice = int(input("Press a number: "))

		match messages_settings_choice:
			case 7:
				messages_settings()
			case 0:
				return
			case _:
				print("Invalid choice.")


def messages_settings():
	while True:
		print("Message settings")
		messages_settings_menu = """
			Press 1 : Set 1
			Press 2 : Common
	Press 0 to Go Back
		"""
		print(messages_settings_menu)
		messages_settings_choice_choices = int(input("Press a number: "))

		match messages_settings_choice_choices:
			case 1:
				messages_set_one()
			case 2:
				messages_common()
			case 0:
				return
			case _:
				print("Invalid choice.")


def messages_set_one():
	while True:
		print("Set 1")
		messages_set_one_settings = """
			Press 1 : Message centre number
			Press 2 : Messages sent as
			Press 3 : Messages validity
	Press 0 to Go Back
		"""
		print(messages_set_one_settings)
		messages_set_one_choice = int(input("Press a number: "))

		match messages_set_one_choice:
			case 0:
				return
			case _:
				print("Invalid choice.")


def messages_common():
	while True:
		print("Common")
		messages_common_settings = """
			Press 1 : Delivery reports
			Press 2 : Reply via same centre
			Press 3 : Character support
	Press 0 to Go Back
		"""
		print(messages_common_settings)
		messages_common_choice = int(input("Press a number: "))

		match messages_common_choice:
			case 0:
				return
			case _:
				print("Invalid choice.")


def chat():
	print("Chat")


def call_register():
	while True:
		print("Call register")
		call_register_menu = """
			Press 1 : Missed calls
			Press 2 : Received calls
			Press 3 : Dialed numbers
			Press 4 : Erase recent call lists
			Press 5 : Show call duration
			Press 6 : Show call costs
			Press 7 : Call cost settings
			Press 8 : Prepaid credits
	Press 0 to Go Back
		"""
		print(call_register_menu)
		show_call_duration = int(input("Press a number: "))

		match show_call_duration:
			case 5:
				call_register_show_duration()
			case 6:
				call_register_show_costs()
			case 7:
				call_register_cost_settings()
			case 8:
				print("Prepaid credit")
			case 0:
				return
			case _:
				print("Invalid choice.")


def call_register_show_duration():
	while True:
		print("Show call duration")
		show_call_duration_choice = """
			Press 1 : last call duration
			Press 2 : All calls' duration
			Press 3 : Received calls' duration
			Press 4 : Dialled calls' duration
			Press 5 : Clear timers
	Press 0 to Go Back
		"""
		print(show_call_duration_choice)
		show_call_duration_pick = int(input("Press a number: "))

		match show_call_duration_pick:
			case 0:
				return
			case _:
				print("Invalid choice.")


def call_register_show_costs():
	while True:
		print("Show call costs")
		show_call_costs_choice = """
			Press 1 : last call cost
			Press 2 : All calls' cost
			Press 3 : Clear counters
	Press 0 to Go Back
		"""
		print(show_call_costs_choice)
		show_call_costs_pick = int(input("Press a number: "))

		match show_call_costs_pick:
			case 0:
				return
			case _:
				print("Invalid choice.")


def call_register_cost_settings():
	while True:
		print("Call cost settings")
		call_cost_settings = """
			Press 1 : Call cost limit
			Press 2 : Show costs in
	Press 0 to Go Back
		"""
		print(call_cost_settings)
		call_cost_settings_pick = int(input("Press a number: "))

		match call_cost_settings_pick:
			case 0:
				return
			case _:
				print("Invalid choice.")


def tones():
	while True:
		print("Tones")
		tones_menu = """
			Press 1 : Ringing tone
			Press 2 : Ringing volume
			Press 3 : Incoming call alert
			Press 4 : Composer
			Press 5 : Message alert tone
			Press 6 : Keypad tones
			Press 7 : Warning and game tones
			Press 8 : Vibration alert
			Press 9 : Screen saver
	Press 0 to Go Back
		"""
		print(tones_menu)
		tones_choice = int(input("Press a number: "))

		match tones_choice:
			case 0:
				return
			case _:
				print("Invalid choice.")


def settings():
	while True:
		print("Settings")
		settings_choice = """
			Press 1 : Call settings
			Press 2 : Phone settings
			Press 3 : Security settings
			Press 4 : Restore factory settings
	Press 0 to Go Back
		"""
		print(settings_choice)
		settings_choice_choices = int(input("Press a number: "))

		match settings_choice_choices:
			case 1:
				call_settings()
			case 2:
				phone_settings()
			case 3:
				security_settings()
			case 4:
				print("Restore factory settings")
			case 0:
				return
			case _:
				print("Invalid choice.")


def call_settings():
	while True:
		print("Call settings")
		call_settings_menu = """
			Press 1 : Automatic redial
			Press 2 : Speed dialing
			Press 3 : Call waiting options
			Press 4 : Own number sending
			Press 5 : Phone line in use
			Press 6 : Automatic answer
	Press 0 to Go Back
		"""
		print(call_settings_menu)
		call_settings_pick = int(input("Press a number: "))

		match call_settings_pick:
			case 0:
				return
			case _:
				print("Invalid choice.")


def phone_settings():
	while True:
		print("Phone settings")
		phone_settings_menu = """
			Press 1 : Language
			Press 2 : Cell info display
			Press 3 : Welcome note
			Press 4 : Network selection
			Press 5 : Lights
			Press 6 : Confirm SIM service actions
	Press 0 to Go Back
		"""
		print(phone_settings_menu)
		phone_settings_pick = int(input("Press a number: "))

		match phone_settings_pick:
			case 0:
				return
			case _:
				print("Invalid choice.")


def security_settings():
	while True:
		print("Security settings")
		security_settings_menu = """
			Press 1 : PIN code request
			Press 2 : Call barring service
			Press 3 : Fixed dialing
			Press 4 : Closed user group
			Press 5 : Phone security
			Press 6 : Change access codes
	Press 0 to Go Back
		"""
		print(security_settings_menu)
		security_settings_pick = int(input("Press a number: "))

		match security_settings_pick:
			case 0:
				return
			case _:
				print("Invalid choice.")


def call_divert():
	print("Call divert")


def games():
	print("Games")


def calculator():
	print("Calculator")


def remainders():
	print("Remainders")


def clock():
	while True:
		print("Clock")
		Clock = """
		Press 1 : Alarm clock
		Press 2 : Clock settings
		Press 3 : Date settings
			Press 4 : Stop watch
			Press 5 : Countdown timer
			Press 6 : Auto update of date and time
	Press 0 to Go Back
		"""
		print(Clock)
		clock_choice = int(input("Press a number: "))

		match clock_choice:
			case 0:
				return
			case _:
				print("Invalid choice.")


def profiles():
	print("Profiles")


def sim_services():
	print("SIM services")


def main():
	while True:
		list_of_menu_functions = """
	Welcome to Nokia3310 Menu functions

		Press 1 : Phone book
		Press 2 : Messages
		Press 3 : Chat
		Press 4 : Call register
		Press 5 : Tones
		Press 6 : Settings
		Press 7 : Call divert
		Press 8 : Games
		Press 9 : Calculator
		Press 10 : Remainders
		Press 11 : Clock
		Press 12 : Profiles
		Press 13 : SIM services
Press 0 to Exit
		"""

		print(list_of_menu_functions)
		menu_function_numbers = int(input("Press a number: "))

		match menu_function_numbers:
			case 1:
				phone_book()
			case 2:
				messages()
			case 3:
				chat()
			case 4:
				call_register()
			case 5:
				tones()
			case 6:
				settings()
			case 7:
				call_divert()
			case 8:
				games()
			case 9:
				calculator()
			case 10:
				remainders()
			case 11:
				clock()
			case 12:
				profiles()
			case 13:
				sim_services()
			case 0:
				print("Bye!!!")
				break
			case _:
				print("Invalid choice.")


if __name__ == "__main__":
	main()

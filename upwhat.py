import datetime

def current_time_to_str():
    time = datetime.datetime.now()
    return time.strftime("%H:%M:%S")

def is_member(username:str, conversation_members:tuple):
	flag=True
	while flag:
		if username in conversation_members:
			return True
			flag=False
		else:return False
		
def enough_space(msg_content, conversation_size, max_conversation_size):
	#TODO
	return
		
def conversation_is_empty(conversation):
	#TODO
	return

def msg_to_string(msg):
	msg_str = "("+str(msg[0])+") "+msg[3]+" "+msg[1]+": "+msg[2]+"\n"
	return msg_str

def conversation_to_string(conversation):
	#TODO
	return
		
def show_conversation(conversation):
	print(conversation_to_string(conversation))
	
	
def send_msg(username, msg_content, msg_last_id, conversation_size, max_conversation_size, conversation):
	#TODO
	return

def find_msg_index(msg_id, conversation):
	#TODO
	return
	
def delete_msg(msg_id, conversation_size, conversation):
	#TODO
	return

def star_marking(msg_id, conversation):
	#TODO
	return
		
def print_starred_messages(conversation):
	#TODO
	return

def file_fixing(filename):
	#TODO
	return

def internal_check(conversation):
	#TODO
	return

def interactive_system(conversation_members = ("Steve", "Bill"), max_conversation_size = 300):
	conversation_size = 0
	conversation = []
	msg_last_id = 0
	while True:
		print("##################################################\nWelcome to UpWhats! What would you like to do?\n\
[0] End conversation\n[1] Show full conversation\n[2] Send new message\n[3] Remove existing message\n\
[4] Star a message\n[5] Show starred messages\n[6] Internal check")
		username = input("Please enter username (only conversation's members are allowed to send/read messages.)\n")
		if is_member(username, conversation_members):
			choice = input("Please type your choice and press ENTER\n")
			if choice not in ["0", "1", "2", "3", "4", "5", "6"]:
				print("Invalid choice")
				continue
			if choice == '0':
				print("Thank you for using UpWhats! See you soon. Bye.")
				break
			elif choice == '1':
				if conversation_is_empty(conversation):
					print("Conversation is empty")
				else:
					show_conversation(conversation)
			elif choice == '2':
				msg_content = input("Please type your message.\n")
				prev_msg_last_id, prev_conversation_size = msg_last_id, conversation_size
				msg_last_id, conversation_size = send_msg(username, msg_content, msg_last_id, conversation_size, max_conversation_size, conversation)
				if prev_msg_last_id == msg_last_id and prev_conversation_size == conversation_size:
					print("There is not enough space in the storage!")
				else:
					print("Message was sent successfully!")
			elif choice == '3':
				msg_id = input("Please enter message id.\n")
				new_size = delete_msg(int(msg_id), conversation_size, conversation)
				if new_size == -1:
					print("There is no message with this identifier")
				else:
					conversation_size = new_size
					print("Message was removed successfully!")
			elif choice == '4':
				msg_id = input("Please enter message id.\n")
				marked = star_marking(int(msg_id), conversation)
				if marked == -1:
					print("There is no message with this identifier")
			elif choice == '5':
				starred_concat = print_starred_messages(conversation)
				if starred_concat == -1:
					print("There are no starred messages")
				else:
					print(starred_concat)
			elif choice == '6':
				internal_check_tuple = internal_check(conversation)
				print("The number of messages that contains all the alphabet is {0}, and the most common char is '{1}' \
which appeared {2} times".format(str(internal_check_tuple[0]), internal_check_tuple[1], internal_check_tuple[2]))
		else:
			print("You're not a member of this group!")

if __name__ == "__main__":
    interactive_system()

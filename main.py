class User:
    def __init__(self,username,id):
        self.username=username
        self.id=id
    def join_chat_room(self):
        print("You have joined a Chat room!")
    def Leave_chat_room(self):
        print("Left the Chat Room!")
class Message:
    def __init__(self):
        print("This is a Message Room!")
    def message_the_bot(self,msg):
        self.msg=msg
    def display_message(self):
        print(self.msg)
class ChatRoom:
    def __init__(self,room_name,users_collection):
        
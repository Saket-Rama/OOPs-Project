class User:
    def __init__(self,username,id):
        self.username=username
        self.id=id
    def join_chat_room(self):
        print("You have joined a Chat room!")
    def leave_chat_room(self):
        print("Left the Chat Room!")
class Message:
    def __init__(self,msg):
        self.msg=msg
    def message_the_bot(self):
        print(f"{self.msg}")
    def display_message(self):
        print(self.msg)
class ChatRoom:
    user_collection=[]
    messages_collection=[]
    def __init__(self,room_name):
        self.room_name=room_name
    def join_user(self):
        User.join_chat_room()
    def leave_user(self):
        User.Leave_chat_room()
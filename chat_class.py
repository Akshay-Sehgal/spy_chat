from datetime import datetime
class Chat:
    def __init__(self,msg,sender,fn):
        self.friend_name=fn
        self.message=msg
        self.timestamp=datetime.now()
        self.send_by_me=sender

from datetime import datetime
class Chat:
    def __init__(self,msg,sender):
        self.message=msg
        self.timestamp=datetime.now()
        self.send_by_me=sender

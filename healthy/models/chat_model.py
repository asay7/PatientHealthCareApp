from datetime import datetime


class ChatModule:
    def __init__(self):
        # Needs to get this from the server
        self.userlist = {"Tony": ["Admin", "Doctor"]}

    def generateMessage(self, contents, sender, recipient):
        if sender not in self.userlist or recipient not in self.userlist:
            return False

        msg = {
            "Sender": sender,
            "Recipient": recipient,
            "Timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "Contents": contents,
            "Read": False
        }
        return


def messageOK(msg) -> bool:
    pass

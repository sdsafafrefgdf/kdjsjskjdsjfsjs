from telethon import TelegramClient, events
from telethon.tl.functions.users import GetFullUserRequest
import os

api_id = int(os.environ["api_id"])
api_hash = os.environ["api_hash"]
bot_token = os.environ["bot_token"]
developer = int(os.environ["developer"])
support_group = int(os.environ["support_group"])

ridogramassistant = TelegramClient('ridogramassistant', api_id, api_hash).start(bot_token=bot_token)

@ridogramassistant.on(events.NewMessage(chats=support_group))
async def runridogramassistant(event):
    try:
        usermessage = event.message.message
        featurekey = "#Feature_Request"
        bugkey = "#Bug_Report"
        fromthisid = event.from_id.user_id
        fetchinfo = await event.client(GetFullUserRequest(fromthisid))
        fromthisuser = fetchinfo.users[0].first_name
        getgroupinformation = await event.get_chat()
        notificationlocation = event.id
        if featurekey in usermessage:
            await ridogramassistant.send_message(developer, f"From: {getgroupinformation.title}\nUser: {fromthisuser}\nInformation: {usermessage}")
            await ridogramassistant.send_message(support_group, f"Dear {fromthisuser},\nFeature Request Submitted Successfully.\n\nThanks,\nRidogram's Assistant", reply_to=notificationlocation)
        elif bugkey in usermessage:
            await ridogramassistant.send_message(developer, f"From: {getgroupinformation.title}\nUser: {fromthisuser}\nInformation: {usermessage}")
            await ridogramassistant.send_message(support_group, f"Dear {fromthisuser},\nBug Report Submitted Successfully.\n\nThanks,\nRidogram's Assistant", reply_to=notificationlocation)
        else:
            pass
    except:
        pass

print("Ridogram's Assistant Started")
ridogramassistant.run_until_disconnected()
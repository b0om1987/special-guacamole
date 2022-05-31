# Èìïîðòèðóåì íóæíûå êëàññû äëÿ ðàçðàáîòêè ñâîèõ ôèëüòðîâ
from vkwave.bots.core.dispatching.filters.base import BaseFilter, BaseEvent, FilterResult
from vkwave.bots import SimpleLongPollBot, SimpleBotEvent

bot = SimpleLongPollBot(tokens='a0511bfbe584e545bceb42855ed6d3931e455d67f74afb84d18935c6bdbb48e69cf273977521613986b85', group_id=213635999)

# ìû èñïîëüçóåì ôèëüòð äëÿ êîìàíä. îí ôèëüòðóåò âñå ñîîáùåíèÿ êîòîðûå íå âûãëÿäèò êàê `/<íàøà êîìàíäà>`. ìîæíî çàäàòü ñâîè ïðåôèêñû, à òàêæå ïåðåäàòü ñïèñîê êîìàíä
@bot.message_handler(bot.command_filter("ñîôèÿ"))
def echo(event: SimpleBotEvent) -> str:
    args = event.object.object.message.text.split()
    if len(args) < 2:
        return "Íàïèøè êàêîé-íèáóäü òåêñò!"
    textz = event.object.object.message.text
    return textz[7:]


bot.run_forever() 

# Импортируем нужные классы для разработки своих фильтров
from vkwave.bots.core.dispatching.filters.base import BaseFilter, BaseEvent, FilterResult
from vkwave.bots import SimpleLongPollBot, SimpleBotEvent

bot = SimpleLongPollBot(tokens='a0511bfbe584e545bceb42855ed6d3931e455d67f74afb84d18935c6bdbb48e69cf273977521613986b85', group_id=213635999)

# мы используем фильтр для команд. он фильтрует все сообщения которые не выглядит как `/<наша команда>`. можно задать свои префиксы, а также передать список команд
@bot.message_handler(bot.command_filter("софия"))
def echo(event: SimpleBotEvent) -> str:
    args = event.object.object.message.text.split()
    if len(args) < 2:
        return "Напиши какой-нибудь текст!"
    textz = event.object.object.message.text
    return textz[7:]


bot.run_forever()
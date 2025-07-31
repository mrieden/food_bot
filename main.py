from bot1.bot_class import bot
import time

with bot() as bot:
    bot.land_first_page()
    bot.refresh()
    bot.report_items()
    time.sleep(20)




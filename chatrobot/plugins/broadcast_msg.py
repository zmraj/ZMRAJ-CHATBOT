
#    Copyright (C) DevsExpo 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
# 
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from chatrobot.plugins.sql.checkuser_sql import get_all_users

@chatbot_cmd("broadcast", is_args=True)
@god_only
async def sedlyfsir(event):
    msgtobroadcast = event.text
    msgtobroadcast = event.text.split(" ", maxsplit=1)[1]
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for starkcast in userstobc:
        try:
            await chatbot.send_message(int(starkcast.chat_id), msgtobroadcast)
        except Exception as e:
            error_count += 1
    sent_count = error_count - len(userstobc)
    await chatbot.send_message(
        event.chat_id,
        f"<b>Broadcast Done in <u>{sent_count}</u> Group/Users and I got <u>{error_count}</u> Error and Total Number Was <u>{len(userstobc)}</u></b>",
        parse_mode="HTML"
    )
    await chatbot.send_message(Config.DUMB_CHAT, f"You BroadCasted A New Message. \nMessage - {msgtobroadcast} \nSent Count - {sent_count}")

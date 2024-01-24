from aiogram.enums import ChatType
from aiogram.types import Message


class SuperGroupTopicFilter:
    def __init__(self, topic_name: str):
        self.topic_name = topic_name

    async def __call__(self, message: Message) -> bool:
        if message.chat.type != ChatType.SUPERGROUP:
            return False
        chat_topic_name = message.reply_to_message.forum_topic_created.name
        if chat_topic_name == self.topic_name:
            return True
        return False

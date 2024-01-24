from typing import NoReturn

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, Chat, MessageReactionUpdated
from aiogram.filters import Command
from filters.super_group_filter import SuperGroupTopicFilter
from loguru import logger

from keyboards.main import inline_builder

chat_router = Router()



@chat_router.message(Command('mute'))
async def test_2(message: Message):
    who_vote = message.from_user.username
    kovo_vote = message.reply_to_message.from_user.username
    id_for_mute = message.reply_to_message.from_user.id
    if id_for_mute is None:
        return
    pattern = dict(
        text=f"@{who_vote} хочет замутить пользователя {kovo_vote}. Согласен? Поддериваешь?",
        reply_markup=inline_builder(
            [f'Да!'],
            ['da_hand_{id_for_mute}']
        )
    )
    await message.answer(**pattern)


@chat_router.callback_query(
    F.data.startswith('da_hand_')
)
async def vote_ban(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"А по итогу 'Да' нажал(а): @{call.from_user.username}")

@chat_router.message(
    SuperGroupTopicFilter(topic_name="БотоСтройка"),
    F.text == '..test'
)
async def test_handler(message: Message) -> NoReturn:
    topic_name = message.reply_to_message.forum_topic_created.name
    message.reply_to_message.from_user.id
    pattern = dict(
        text="Будут ли у меня кнопки",
        reply_markup=inline_builder(
            ['DA'],
            ['da_hand']
        )
    )

    await message.answer(**pattern)


@chat_router.message(
    F.text.startswith('@Сашка-сашенька')
)
async def sasha_sashenka(message: Message) -> NoReturn:
    text = message.text[len('@Сашка-сашенька'):]
    await message.answer(f'@Leggendada {text}')


@chat_router.message(
    F.text.startswith('@Волонтеры')
)
async def sasha_sashenka(message: Message) -> NoReturn:
    text = message.text[len('@Волонтеры'):]
    await message.answer(f'{text}'
                         f'\n\n@Волонтер1 @Волонтер2 @Волонтер3 ...')

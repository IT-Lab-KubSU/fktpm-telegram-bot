from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardBuilder, ReplyKeyboardBuilder, ReplyKeyboardMarkup
from typing import List, Union
from itertools import zip_longest


def inline_builder(
        text: Union[str, List[str]],
        callback_data: Union[str, List[str]],
        sizes: Union[int, List[int]] = None
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    if isinstance(text, str):
        text = [text]
    if isinstance(callback_data, str):
        callback_data = [callback_data]
    if isinstance(sizes, int):
        sizes = [sizes]

    if len(text) != len(callback_data):
        raise ValueError("Длина текстра и колбэк дата должны совпадать")

    for txt, cb in zip_longest(text, callback_data):
        if txt is not None and cb is not None:
            builder.button(text=txt, callback_data=cb)
        else:
            raise ValueError()

    if sizes is not None:
        builder.adjust(*sizes)
        return builder.as_markup()
    else:
        return builder.as_markup(resize_keyboard=True)


def reply_builder(
        text: Union[str, List[str]],
        sizes: Union[int, List[int]] = 1
) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    if isinstance(text, str):
        text = [text]
    if isinstance(sizes, int):
        sizes = [sizes]

    for txt in text:
        builder.button(text=txt)

    builder.adjust(*sizes)
    return builder.as_markup()

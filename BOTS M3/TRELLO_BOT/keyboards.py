from psycopg2.extras import RealDictCursor
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from db import connection, queries


def get_inline_boards_btn(user_id, action):
    inline_boards_btn = InlineKeyboardMarkup()
    with connection.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(queries.GET_USER_BOARDS, (user_id,))
        boards = cur.fetchall()
    if len(boards) % 2 == 0:
        last_board = None
    else:
        last_board = boards.pop()
    for board_index in range(0, len(boards) - 1, 2):
        inline_boards_btn.add(
            InlineKeyboardButton(
                boards[board_index].get("name"),
                callback_data=f'{action}_{boards[board_index].get("board_id")}'
            ),
            InlineKeyboardButton(
                boards[board_index + 1].get("name"),
                callback_data=f'{action}_{boards[board_index + 1].get("board_id")}'
            )
        )
    if last_board:
        inline_boards_btn.add(
            InlineKeyboardButton(
                last_board.get("name"), callback_data=f'{action}_{last_board.get("board_id")}'
            )
        )
    return inline_boards_btn
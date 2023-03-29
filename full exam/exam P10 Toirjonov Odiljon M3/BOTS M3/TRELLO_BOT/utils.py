import csv
import os


def write_chat_to_csv(file_path, message):
    header = ["chat_id", "first_name", "last_name", "trello_username"]
    row = {
        "chat_id": message.chat.id,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "trello_username": message.text
    }
    with open(file_path, "a+", newline="\n") as f:
        csv_writer = csv.DictWriter(f, header)
        if os.path.getsize(file_path) == 0:
            csv_writer.writeheader()
        csv_writer.writerow(row)
    print("Chat add successfully.")


def check_chat_id_from_csv(file_path, chat_id):
    with open(file_path, encoding="utf-8") as f:
        csv_reader = csv.DictReader(f)
        return chat_id in [int(row.get("chat_id")) for row in csv_reader]


def get_trello_username_by_chat_id(file_path, chat_id):
    with open(file_path, encoding="utf-8") as f:
        csv_reader = csv.DictReader(f)
        users = [
            row.get("trello_username")
            for row in csv_reader
            if int(row.get("chat_id")) == chat_id
        ]
        return users[0] if users else None


def get_user_tasks_message(cards):
    msg = ""
    for index, card in enumerate(cards):
        msg += f"{index + 1}. <a href=\"{card.get('url')}\">{card.get('card_name')}</a>\n"

    return msg
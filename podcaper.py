from bot_config import BOTCONFIG
import random
import nltk
import pandas as pd
#import telebot

users = pd.DataFrame()


# cleaning
def phrase_cleaner(replica):
    replica = replica.lower()
    replica = replica.split()
    replica = ' '.join(replica)
    alphabet = 'йцукенгшщзхъфывапролджэячсмитьбюё- '
    result = ''.join(letter for letter in replica if letter in alphabet)
    return result


# классификация намерения
def classify_intent(replica):
    for intent, intent_data in BOTCONFIG['intents'].items():
      for example in intent_data['examples']:
        if get_distance(replica, example) < 0.4:
          return intent


# ответ по определенному намерению
def get_answer_by_intent(intent):
    if intent in BOTCONFIG['intents']:
      responses = BOTCONFIG['intents'][intent]['responses']
      if intent == 'get_phrase':
          return phrase_answer()
    return random.choice(responses)


# генеративная модель ответа
def generate_answer(replica):
    get_failure_phrase()



# заглушка
def get_failure_phrase():
    failure_phrases = BOTCONFIG['failure_phrases']
    return random.choice(failure_phrases)


# добавить фразу
def add_phrase(category, phrase):
    pass


# расстояние левенштейна
def get_distance(phrase, compare_phrase):
    distance = nltk.edit_distance(phrase, compare_phrase)
    return distance / len(phrase)


# собирает статистику пользователей
def get_user_info(message):
    text = message.text
    id = message.chat.id
    name = message.from_user.first_name
    username = message.from_user.username
    message_id = message.message_id
    info_dict = {
        "text": text,
        'id': id,
        'name': name,
        'username': username,
        'message_id': message_id
    }
    print(info_dict)
    # ser = pd.Series(info_dict)
    # add_to_df(ser)

# Добавляет строку в таблицу и формирует csv-файл
def add_to_df(series, users = users):
    users.append(series)
    df = users.copy()
    df.to_csv()

# ответ подкатом
def phrase_answer(kind = 'blunty'):
    responses = BOTCONFIG['phrases'][kind]['examples']
    return random.choice(responses)
# print("ПОДКАТИК")
# вызвать меню

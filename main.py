import podcaper
import bot_config


def __init__(BOTCONFIG=bot_config.BOTCONFIG, sex='male', user_id=0):
    BOTCONFIG = BOTCONFIG
    sex = sex
    user_id = user_id


def bot(replica):

    # cleaning
    replica = podcaper.phrase_cleaner(replica)

    # классифицировать намерение
    intent = podcaper.classify_intent(replica)

    # выбор заготовленной реплики
    if intent is not None:
        answer = podcaper.get_answer_by_intent(intent)
        if answer:  # is not None:
            return answer

    # вызов генеративной модели
    answer = podcaper.generate_answer(replica)
    if answer:
        return answer

    # заглушка
    answer = podcaper.get_failure_phrase()
    return answer

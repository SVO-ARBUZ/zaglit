import random
import json
import random
import os
from gradio_client import Client
# def getRandomMessage():
#     msg = random.choice(messages)
#     if msg.startswith("http"):
#         return random.choice(messages)
#     else:
#         return msg
#
# for i in range(100):
#     print(getRandomMessage())





def add_to_save(link, file_path='save.json'):
    # Проверяем существование указанного файла
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding="utf8") as fp:
            try:
                existing_links = json.load(fp)
            except json.JSONDecodeError:
                existing_links = []
    else:
        existing_links = []

    # # Проверяем, не содержится ли ссылка уже в списке
    # if link in existing_links:
    #     print("Ссылка уже существует в списке")
    #     return

    # Добавляем новую ссылку в список существующих
    existing_links.append(link)

    # Записываем обновленный список обратно в файл
    with open(file_path, 'w', encoding="utf8") as fp:
        json.dump(existing_links, fp, ensure_ascii=False, indent=4)

    print(f"'{link}' успешно добавлен в файл {file_path}")

# Пример использования метода для добавления ссылки с указанием пути к файлу

def randomMessage():
    with open('messages.json', 'r', encoding="utf8") as fp:
        return random.choice(json.load(fp))

ps = ["""""",
      ]

def bandit(p):
    client = Client("Qwen/Qwen1.5-110B-Chat-demo")
    result = client.predict(
        query=p,
        history=[],
        system=''.join(ps),
        api_name="/model_chat"
    )
    return result[1][0][1]

rnd = randomMessage()
gen = bandit(rnd)
print(rnd, "\n\n")
print(gen,"\n\n")
print(rnd + " " + gen)




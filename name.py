from vkbottle.api import API
import asyncio
import os

TOKEN = os.environ.get("USER_TOKEN")
USER_ID = os.environ.get("USER")  # 588927739
api = API(tokens=TOKEN)  # Получать токен через https://vkhost.github.io/ | Kate Mobile


async def set():
    while True:
        comments = await api.wall.get_comments(owner_id=int(USER_ID),
                                               post_id=30)  # {'count': 0, 'items': [], 'can_post': True, 'groups_can_post': True, 'current_level_count': 0}
        online = await api.friends.get_online(user_id=USER_ID)
        await api.status.set(text=f"Провожу сделки. Отзывов - {comments.count}💬")  # Текст статуса
        await asyncio.sleep(30)


if __name__ == '__main__':
    asyncio.run(set())

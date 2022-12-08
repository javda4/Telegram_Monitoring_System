import camera.image as cam_image
import camera.video as curr_video
from aiogram import Bot, Dispatcher, types, executor
from API import API as api


API_KEY = api.API_MAIN_KEY
bot = Bot(token=API_KEY)
msgbot = Dispatcher(bot)


@msgbot.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Commands are /image (takes image of current environment) /video (takes video of current "
                        "environment)")


@msgbot.message_handler(commands=['image', 'help'])
async def img(message: types.Message):
    cam_image.image_monitor()
    picture = open("image.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=picture)


@msgbot.message_handler(commands=['video', 'help'])
async def vid(message: types.Message):
    curr_video.video_monitor()
    curr_video_cap = open("video.mp4", "rb")
    await bot.send_video(message.chat.id, video=curr_video_cap)

executor.start_polling(msgbot)

import utils.ch
import utils.regex

handler_list = [utils.ch.simple_reply(
    "start",
    "Привет! На связи alterpy - быстрый, потому что никому не нужный телеграм-бот!\n" +
    "\n" +
    "Пока что я нахожусь в стадии разработки. Если вы нашли баги - вы можете сообщить разработчикам или присоединиться в ряды тестеров.\n" +
    "Как catpy и forkpy, только по-другому\n" +
    "Разработано для t.me/theyukichat\n" +
    "Список команд _пока не поддерживается_\n" +
    "Пинг до бота: `/ping`\n" +
    "\n" +
    "В разработке принимали участие: t.me/yuki\_the\_girl",
    "start",
    utils.regex.raw("/start(@alterpy_bot)?")
)]


import util

handlers = [
    util.get_handler_simple_reply('да', util.rand_or_null_fun('пизда', 1, 3), pattern="(?i)\\bда$"),
    util.get_handler_simple_reply('нет', util.rand_or_null_fun('солнышка ответ', 1, 3), pattern="(?i)\\bнет$"),
    util.get_handler_simple_reply('дура', util.rand_or_null_fun('а может ты 🤨?', 1, 3), pattern="(?i)\\bдура$"),

    util.get_handler_simple_reply('спокойной ночи', 'Cладких снов 🥺', pattern="(?i)^((всем ){0,1}спокойной ночи)")
]


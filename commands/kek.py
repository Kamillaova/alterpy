import util

handlers = [
    util.get_handler_simple_reply(
        'да',
        util.weighted_random_fun([
            (1, 'сковорода'),
            (1, 'лабуда'),
            (1, 'винда'),
            (1, 'ерунда'),
            (5, '')
        ]),
        ["кеки", "kek"],
        pattern="(?i)\\bда$"
    ),
    util.get_handler_simple_reply(
        'нет',
        util.weighted_random_fun([
            (1, 'солнышка ответ'),
            (1, 'лунышка ответ'),
            (3, '')
        ]),
        ["кеки", "kek"],
        pattern="(?i)\\bнет$"
    ),
    util.get_handler_simple_reply('дура', util.rand_or_null_fun('а может ты 🤨?', 1, 3),
        ["кеки", "kek"], pattern="(?i)\\bдура$"),

    util.get_handler_simple_reply('спокойной ночи', 'Cладких снов 🥺',
        ["кеки", "kek"], pattern="(?i)^((всем ){0,1}спокойной ночи)")
]


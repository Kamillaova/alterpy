import utils.cm
import utils.ch
import utils.regex
import utils.str
import utils.lang.ru

import random

handler_list = []


async def xi(cm: utils.cm.CommandMessage):
    if cm.arg:
        await cm.int_cur.reply(utils.str.escape(''.join(random.choice(utils.lang.ru.morph.parse(part)).normal_form for part in utils.regex.split_by_word_border(cm.arg))))


handler_list.append(
    utils.ch.CommandHandler(
        name='ru_xi',
        pattern=utils.regex.ignore_case(utils.regex.pat_starts_with(utils.regex.prefix() + utils.regex.unite('кси'))),
        help_page=['кси'],
        handler_impl=xi,
        is_prefix=True
    )
)

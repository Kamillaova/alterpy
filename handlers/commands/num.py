import utils.cm
import utils.ch
import utils.regex

handler_list = []


async def on_bmi(cm: utils.cm.CommandMessage) -> None:
    try:
        h, m = map(float, cm.arg.split())
    except:
        await cm.int_cur.reply("Can't parse size")
        return

    _bmi = int((1000000 * m) / (h * h))

    text = ["underweight", "normal", "overweight", "obesity"][[_bmi < 1850, _bmi < 2500, _bmi < 3000, True].index(True)]

    bmi = '000' + str(_bmi)
    bmi = bmi[:-2].lstrip('0') + '.' + bmi[-2:]
    if bmi[0] == '.':
        bmi = '0' + bmi

    await cm.int_cur.reply(f"Your BMI is {bmi} ({text})")


handler_list.append(utils.ch.CommandHandler(
    name="bmi",
    pattern=utils.regex.cmd(utils.regex.unite('bmi', 'имт')),
    help_page="bmi",
    handler_impl=on_bmi,
    is_prefix=True
))

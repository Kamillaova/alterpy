import util

import asyncio
import re
import telethon
import importlib
import traceback

log = util.get_log("main")
log.info("AlterPy")


telethon_config = util.get_config("telethon_config.toml")
client = telethon.TelegramClient("alterpy", telethon_config['api_id'], telethon_config['api_hash'])
client.start(bot_token=telethon_config['bot_token'])
log.info("Started telethon instance")

the_bot_id = int(telethon_config['bot_token'].split(':')[0])
del telethon_config


handlers = []


async def on_command_version(cm: util.CommandMessage):
    await cm.int_cur.reply("AlterPy on Feb 1 of 2023 by Yuki the girl")


handlers.append(util.CommandHandler(
    name='ver',
    pattern=util.re_ignore_case(util.re_pat_starts_with(util.re_only_prefix() + 'ver')),
    help_message='Show AlterPy version',
    author='@yuki_the_girl',
    handler_impl=on_command_version,
    is_elevated=False
))


async def on_list_commands(cm: util.CommandMessage):
    await cm.int_cur.reply("Available command handlers:\n" + ', '.join(f"`{handler.name}`" for handler in handlers))


handlers.append(util.CommandHandler(
    name='handler-list',
    pattern=util.re_ignore_case(util.re_pat_starts_with(util.re_only_prefix() + 'hl')),
    help_message='Show all handlers',
    author='@yuki_the_girl',
    handler_impl=on_list_commands,
    is_elevated=True
))


async def on_exec(cm: util.CommandMessage):
    try:
        shifted_arg = cm.arg.replace('\n', '\n    ')
        code = '\n'.join([
            f"import asyncio",
            f"async def func():",
            f"    {shifted_arg}",
            f"task = asyncio.create_task(func())",
        ])
        code_locals = dict()
        exec(code, globals() | locals(), code_locals)
        await asyncio.wait([code_locals['task']])
    except:
        await cm.int_cur.reply(f"```{traceback.format_exc()}```")
        if 'code' in locals():
            code_lines = code.split('\n')
            lined_code = '\n'.join(f"{i+1}  {code_lines[i]}" for i in range(len(code_lines)))
            await cm.int_cur.reply(f"While executing following code:\n```{lined_code}```")


handlers.append(util.CommandHandler(
    name="exec",
    pattern=util.re_ignore_case(util.re_pat_starts_with(util.re_prefix() + "exec")),
    help_message="Execute python code",
    author="@yuki_the_girl",
    handler_impl=on_exec,
    is_prefix=True,
    is_elevated=True
))

initial_handlers = handlers[:]


def load_commands():
    global handlers
    handlers = initial_handlers[:]
    commands_filenames = list(filter(lambda filename: filename[-3:] == ".py", sorted(util.list_files("commands/"))))
    log.info(f"commands: {commands_filenames}")
    for filename in commands_filenames:
        try:
            mod = importlib.import_module(f"commands.{filename[:-3]}")
            handlers.extend(mod.handlers)
        except:
            util.log_fail(log, f"Loading {filename} failed")


async def process_command_message(cm: util.CommandMessage):
    tasks = [
        asyncio.create_task(handler.invoke(
            util.cm_apply(cm, handler.pattern) if handler.is_prefix else cm
        ))
        for handler in filter(
            lambda handler:
            bool(re.search(handler.pattern, cm.arg)),
            handlers
        )
    ]
    if tasks:
        await asyncio.wait(tasks)


load_commands()


@client.on(telethon.events.NewMessage)
async def event_handler(event: telethon.events.NewMessage):
    if event.message.sender_id == the_bot_id:  # Ignore messages from self
        return

    cm = await util.to_command_message(event)
    await process_command_message(cm)


log.info("Started!")
with client:
    client.run_until_disconnected()

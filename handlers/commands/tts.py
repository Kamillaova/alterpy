import utils.cm
import utils.ch
import utils.file
import utils.regex
import utils.log

import gtts


def on_tts_wrapper(lang: str):
    async def on_tts(cm: utils.cm.CommandMessage):
        filename = f"{utils.file.temp_filename()}.mp3"
        if not cm.arg:
            await cm.int_cur.reply("Empty messages can't be TTSd")
            return
        if len(cm.arg) > 250:
            await cm.int_cur.reply("Please wait while message is being processed...")
        try:
            # https://github.com/pndurette/gTTS/issues/353
            # `0xA0` character sometimes breaks TTS
            # workaround: replace with space
            gtts.gTTS(cm.arg.replace(chr(0xA0), ' '), lang=lang).save(filename)
            await cm.int_cur.send_file(filename, as_reply=True, voice_note=True)
        except:
            utils.log.get("tts").exception("TTS error")
    return on_tts


def tts_handler(name: str, lang: str) -> utils.ch.CommandHandler:
    return utils.ch.CommandHandler(f"tts-{lang}", utils.regex.command(name), ["tts", "озвучка"], on_tts_wrapper(lang), is_prefix=True)


handler_list = [
    tts_handler("tts", "en"),
    tts_handler("озвучь", "ru"),
    tts_handler("мова божія", "uk"),
    tts_handler("vnsay", "ja"),
    tts_handler("sayccp", "zh"),
    tts_handler("kosay", "ko")
]

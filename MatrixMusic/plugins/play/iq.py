import asyncio
import random
from pyrogram import filters, Client
from pyrogram.types import Message
from MatrixMusic import app
import config



txt = [
    "**- اسرع واحد يدز الكلمة** ~ ( بارده )",
    "**- اسرع واحد يدز الكلمة** ~ ( اجيت )",
    "**- اسرع واحد يدز الكلمة** ~ ( جبان )",
    "**- اسرع واحد يدز الكلمة** ~ ( مافهمت )",
    "**- اسرع واحد يدز الكلمة** ~ ( ميت )",
    "**- اسرع واحد يدز الكلمة** ~ ( وصخ )",  
    "**- اسرع واحد يدز الكلمة** ~ ( جوعان )",
    "**- اسرع واحد يدز الكلمة** ~ ( زين )",
    "**- اسرع واحد يدز الكلمة** ~ ( قوي )",
    "**- اسرع واحد يدز الكلمة** ~ ( بطيء )",
    "**- اسرع واحد يدز الكلمة** ~ ( ذكي )",
    "**- اسرع واحد يدز الكلمة** ~ ( خائف )",
    "**- اسرع واحد يدز الكلمة** ~ ( حزين )",
    "**- اسرع واحد يدز الكلمة** ~ ( مستمتع )",
    "**- اسرع واحد يدز الكلمة** ~ ( فرحان )",
    "**- اسرع واحد يدز الكلمة** ~ ( ذو شخصية قوية )",
    "**- اسرع واحد يدز الكلمة** ~ ( واثق )",
    "**- اسرع واحد يدز الكلمة** ~ ( متوتر )",
    "**- اسرع واحد يدز الكلمة** ~ ( مندهش )",
    "**- اسرع واحد يدز الكلمة** ~ ( فائق الذكاء )",
    "**- اسرع واحد يدز الكلمة** ~ ( ذكي للغاية )",
    "**- اسرع واحد يدز الكلمة** ~ ( متسرع )",
    "**- اسرع واحد يدز الكلمة** ~ ( متفائل )",
    "**- اسرع واحد يدز الكلمة** ~ ( متشائم )",
    "**- اسرع واحد يدز الكلمة** ~ ( متفائل جداً )",
    "**- اسرع واحد يدز الكلمة** ~ ( مكتئب )",
    "**- اسرع واحد يدز الكلمة** ~ ( مبتهج )",
    "**- اسرع واحد يدز الكلمة** ~ ( مغمض العينين )",
    "**- اسرع واحد يدز الكلمة** ~ ( مستنكر )",
    "**- اسرع واحد يدز الكلمة** ~ ( مرتبك )",
    "**- اسرع واحد يدز الكلمة** ~ ( متحمس )",
    "**- اسرع واحد يدز الكلمة** ~ ( متعب )",
    "**- اسرع واحد يدز الكلمة** ~ ( مفاجأ )",
    "**- اسرع واحد يدز الكلمة** ~ ( محبوب )",
    "**- اسرع واحد يدز الكلمة** ~ ( مكره )",
    "**- اسرع واحد يدز الكلمة** ~ ( معجب )",
    "**- اسرع واحد يدز الكلمة** ~ ( متواضع )",
    "**- اسرع واحد يدز الكلمة** ~ ( متكبر )",
    "**- اسرع واحد يدز الكلمة** ~ ( متفائل جداً )",
    "**- اسرع واحد يدز الكلمة** ~ ( محبوب للغاية )",
    "**- اسرع واحد يدز الكلمة** ~ ( معفن )",
    "**- اسرع واحد يدز الكلمة** ~ ( محترم )",
    "**- اسرع واحد يدز الكلمة** ~ ( مشاغب )",
    "**- اسرع واحد يدز الكلمة** ~ ( متسلط )",
    "**- اسرع واحد يدز الكلمة** ~ ( متواضع جداً )",
    "**- اسرع واحد يدز الكلمة** ~ ( متهور )",
    "**- اسرع واحد يدز الكلمة** ~ ( مبتكر )",
    "**- اسرع واحد يدز الكلمة** ~ ( ملهم )",
    "**- اسرع واحد يدز الكلمة** ~ ( مضحك )",
    "**- اسرع واحد يدز الكلمة** ~ ( مكتئب جداً)",
    "**- اسرع واحد يدز الكلمة** ~ ( مهتم )",
    "**- اسرع واحد يدز الكلمة** ~ ( محطم )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالحياة )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالحماس )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالتفاؤل )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالسعادة )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالحزن )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالرغبة )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالحب )",

    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالحنان )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالكراهية )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالامتنان )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالرضا )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالخيبة )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالحزن )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالفرح )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالندم )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالنجاح )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالفشل )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالتحدي )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالحكمة )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالجنون )",
    "**- ( اسرع واحد يدز الكلمة** ~ ( مليء بالسكون",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالحركة )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالفكاهة )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالعقلانية )",
    "**- اسرع واحد يدز الكلمة** ~ ( مليء بالجمال )",
]

correct_answers = [
    "بارده",
    "اجيت",
    "جبان",
    "مافهمت",
    "ميت",
    "وصخ",  
    "جوعان",
    "زين",
    "قوي",
    "بطيء",
    "ذكي",
    "خائف",
    "حزين",
    "مستمتع",
    "فرحان",
    "ذو شخصية قوية",
    "واثق",
    "متوتر",
    "مندهش",
    "فائق الذكاء",
    "ذكي للغاية",
    "متسرع",
    "متفائل",
    "متشائم",
    "متفائل جداً",
    "مكتئب",
    "مبتهج",
    "مغمض العينين",
    "مستنكر",
    "مرتبك",
    "متحمس",
    "متعب",
    "مفاجأ",
    "محبوب",
    "مكره",
    "معجب",
    "متواضع",
    "متكبر",
    "متفائل جداً",
    "محبوب للغاية",
    "معفن",
    "محترم",
    "مشاغب",
    "متسلط",
    "متواضع جداً",
    "متهور",
    "مبتكر",
    "ملهم",
    "مضحك",
    "مكتئب جداً",
    "مهتم",
    "محطم",
    "مليء بالحياة",
    "مليء بالحماس",
    "مليء بالتفاؤل",
    "مليء بالسعادة",
    "مليء بالحزن",
    "مليء بالرغبة",
    "مليء بالحب",

    "مليء بالحنان",
    "مليء بالكراهية",
    "مليء بالامتنان",
    "مليء بالرضا",
    "مليء بالخيبة",
    "مليء بالحزن",
    "مليء بالفرح",
    "مليء بالندم",
    "مليء بالنجاح",
    "مليء بالفشل",
    "مليء بالتحدي",
    "مليء بالحكمة",
    "مليء بالجنون",
    "مليء بالسكون",
    "مليء بالحركة",
    "مليء بالفكاهة",  
    "مليء بالعقلانية",  
    "مليء بالجمال",  
]

current_question_index = 0

@app.on_message(filters.command(["كلمة"], ""))
async def game_handler(client: Client, message: Message):
    global current_question_index

    if current_question_index >= len(txt):
        await message.reply("- تم انتهاء الأسئلة .")
        return

    current_question = txt[current_question_index]
    correct_answer = correct_answers[current_question_index]

    if message.text.lower() == correct_answer:
        await message.reply("- الإجابة صحيحة يا ذكي!")
        current_question_index += 1

        if current_question_index < len(txt):
            await message.reply(f"-السؤال الحالي: {txt[current_question_index]}")
        else:
            await message.reply("- تم انتهاء الأسئلة. شكرًا للمشاركة .")
    else:
        await message.reply("- إجابة خاطئة. حاول مرة أخرى .")

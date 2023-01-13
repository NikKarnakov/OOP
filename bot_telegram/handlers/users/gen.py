import re

import torch
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from transformers import (AutoConfig, AutoModelForSequenceClassification,
                          AutoTokenizer, GPT2LMHeadModel, GPT2Tokenizer)

label2id= {
    "negative":0,
    "positive":1,
}
id2label= {
    0:"negative",
    1:"positive",
}
config = AutoConfig.from_pretrained("./horoscopes_rugpt3_final", label2id=label2id, id2label=id2label)
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = AutoTokenizer.from_pretrained("./horoscopes_rugpt3_final")
model = GPT2LMHeadModel.from_pretrained("./horoscopes_rugpt3_final",config=config).to(DEVICE)


from loader import dp
from states import gen


@dp.message_handler(Command('gen'))
async def gen_ (message: types.Message):
    await message.answer ('Добрый день!\nВведите Ваш знак зодиака')
    await gen.test1.set()

@dp.message_handler(state=gen.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test1 = answer)
    await message.answer('Пожалуйста, подождите')
    text1 = await state.get_data('test1')
    text2 = '[SJ] - ' + text1.get('test1')
    input_ids = tokenizer.encode(text2, return_tensors="pt").to(DEVICE)
    model.eval()
    with torch.no_grad():
        out = model.generate(input_ids, 
                        do_sample=True,
                        num_beams=2,
                        temperature=1.5,
                        top_p=0.9,
                        max_length=100, pad_token_id=tokenizer.eos_token_id,
                        )
    generated_text = list(map(tokenizer.decode, out))[0]
    print (generated_text)
    generated_text = generated_text.replace('[SJ]', '').split("[")[0]
    await message.answer(generated_text)

    await state.finish()

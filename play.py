'''
Personal playground for playing with an instance of GPT4ALL.cpp
'''
from pyllamacpp.model import Model

def new_text_callback(text: str):
    print(text, end="", flush=True)

def ask(message, n=70):
    outline = model.generate(message, 
               n_predict=n, 
               new_text_callback=new_text_callback, 
               n_threads=8)
    return outline

model = Model(ggml_model='./ggjt-model.bin', n_ctx=1024)
prompt="Write a story about a girl and her love of sewing."

print("===================")
# print(outline)
# outline=outline.replace(prompt,"")
q = "{}".format( prompt)#, " ###Instruction: What happens next?")
ask(q,n=200)

'''
TODO:
- this is: llama.cpp running gpt4all (https://github.com/nomic-ai/gpt4all#gpt4all-compatibility-ecosystem)
- lo-ra train on storytelling data
- lo-ra train via TattleTale
- generate RP pddl data (via self instruct)
- generate Pathfinder 2E specific data
- generate rolling pddl data
- lo-ra train on pathfinder+rp+roll data combo

== for personal assistant
TODO: 
- find previous checkpoint(guaranteed: ) (dream: )(or make custom ones??)
- instruction train
- lo-ra train on code
- lo-ra train on wikipedia
- re-quantize with new llama.cpp quantize (https://github.com/ggerganov/llama.cpp#using-gpt4all)
- write bash script that takes a model name param, 
  changes it to the right name, and starts up chat (and has a default)
'''
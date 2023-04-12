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


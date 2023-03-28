import subprocess
import time
import sys

bot = subprocess.Popen('./chat', stdin=subprocess.PIPE, stdout=subprocess.PIPE)


def parse_to_prompt(bot):
    they_say = ['']
    point = b''
    while True:
        point += bot.stdout.read(1)
        try:
            character = point.decode("utf-8")
            if character == "\f":
                return "\n".join(they_say)
            if character == "\n":
                they_say.append('')
                sys.stdout.write('\n')
            else:
                they_say[-1] += character
                sys.stdout.write(character)
                sys.stdout.flush()
            point = b''

        except UnicodeDecodeError:
            if len(point) > 4:
                point = b''

prompts = [
    'Write me a letter from the perspective of a cat',
    'Write me a short poem',
    'Tell me how to hard boil an egg',
    'Come up with the vacation destinations.'
]

import random
    
while True:
    they_say = parse_to_prompt(bot)
    print("THEY SAY\n-------")
    print(they_say)
    print("------")
    prompt = random.choice(prompts).replace("\n", "\\\n").encode('utf-8')
    time.sleep(2)
    bot.stdin.write(prompt)
    bot.stdin.write(b"\n")
    bot.stdin.flush()
    
# Send a message to the bouncer process and read its response
message = 'Hello, bouncer!'
bouncer_process.stdin.write(message.encode())
response = bouncer_process.stdout.readline().decode().strip()

# Print the response from the bouncer process
print('Bouncer said:', response)

# Close the input stream to the bouncer process
bouncer_process.stdin.close()

# Wait for the bouncer process to finish and get its return code
return_code = bouncer_process.wait()
print('Bouncer exited with return code:', return_code)

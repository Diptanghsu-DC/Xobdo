import openai

openai.api_key = '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'

messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

while True: 
    message = input("User : ") 
    if message: 
        messages.append( 
            {"role": "user", "content": message}, 
        ) 
        chat = openai.ChatCompletion.create( 
            model="babage", messages=messages 
        ) 
    reply = chat.choices[0].message.content 
    print(f"ChatGPT: {reply}") 
    messages.append({"role": "assistant", "content": reply}) 
from openai import OpenAI

def ChatDBX(token, url, question, model, max_tokens=256):

  client = OpenAI(
    api_key=token,
    base_url=url
  )
        
  chat_completion = client.chat.completions.create(
    messages=[
    {
      "role": "system",
      "content": "You are an AI assistant"
    },
    {
      "role": "user",
      "content": question
    }
    ],
    model=model,
    max_tokens=max_tokens
  )
  
  return chat_completion.choices[0].message.content
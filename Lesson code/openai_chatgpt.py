from openai import OpenAI
client = OpenAI()


def complete_chat(user_message, pre_prompt="你是一個公平公正的記者，請根據以下內容，摘要一段30字以內的新聞摘要。"):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": pre_prompt
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return completion.choices[0].message.content

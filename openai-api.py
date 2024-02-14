from openai import OpenAI

client = OpenAI()

assistant = client.beta.assistants.create(
    name="Utah Bill AI",
    instructions="You are a personal expert in the Utah State Law Code",
    tools=[{"type": "retrieval"}],
    model="gpt-4-turbo-preview"
)
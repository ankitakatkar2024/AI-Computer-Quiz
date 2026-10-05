from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Give me one simple computer science multiple-choice question with 4 options and the correct answer."
)

print(response.text)
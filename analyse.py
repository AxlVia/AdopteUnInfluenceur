
from openai import OpenAI

text_test="dans la liste de sentiments suivant uniquement: (tristesse, bonheur, heine, désespoir, espoire, optimist, pissimiste, rage, colère, heureux, dessus, satisfé), donnez moi la liste des sentiments (parmis ceux cités) que vous voupez identifier dans le texte suivant: Docteur je me sens beaucoup mieux, je crois que je vais bietôt guérir. dans votre réponse soyez précis, n'ajoutez pas des sentiments hors la liste de sentiments proposés et la réponse doit contenir uniquement les sentiments détéctés"


client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
    
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": text_test,
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)
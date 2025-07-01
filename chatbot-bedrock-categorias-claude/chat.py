import boto3
import json

def gerar_resposta(pergunta, categoria):
    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    prompt = open("prompt.txt", "r").read()
    input_text = (
        f"{prompt}\n\n"
        f"Human: [Categoria: {categoria}] {pergunta}\n\n"
        f"Assistant:"
)

    response = client.invoke_model(
        modelId="anthropic.claude-v2",
        contentType="application/json",
        accept="application/json",
        body=json.dumps({
            "prompt": input_text,
            "max_tokens_to_sample": 300,
            "temperature": 0.5
        })
    )

    result = json.loads(response['body'].read())
    return result['completion'].strip()

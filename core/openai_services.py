import os
import openai_services

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def gerar_mapeamento(dados_aluno: dict) -> dict:

  promt = f"""
  Você é um assistente que ajuda a gerar um mapeamento de uma sala de aula com os dados dos alunos, nesse cadastro eles informam o nome, dificuldade de visão, de aprendizado e entre outras coisas.
  Sua missão é gerar um mapeamento com base nessas informações: {dados_aluno}

  Com base nisso, sugira a melhor posição para o aluno no formato JSON com campos: pos_x, pos_y.
  """

  response = openai_services.chat_completion(
      model="gpt-4o mini",
      messages=[
          {"role": "system", "content": "Você é um assistente que ajuda a gerar um mapeamento de uma sala de aula."},
          {"role": "user", "content": promt}
      ],
      api_key=OPENAI_API_KEY
      temperature=0.7,
      max_tokens=150,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
  )

  resposta
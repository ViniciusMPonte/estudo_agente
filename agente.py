from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from buscador import Buscador


class Agente:

    def __init__(self, buscador: Buscador) -> None:
        self.buscador = buscador
        self.llm = ChatOllama(model="qwen2.5", temperature=0)

    def criar_ferramentas(self) -> list:

        @tool
        def buscar_documentos(query: str) -> str:
            """Busca informações nos documentos locais. Use SEMPRE que o usuário fizer qualquer pergunta. As informações retornadas são a fonte principal de conhecimento."""
            docs = self.buscador.buscar(query, quantidade=5)
            return "\n\n".join([doc.page_content for doc in docs])

        return [buscar_documentos]

    def executar(self) -> None:
        ferramentas = self.criar_ferramentas()
        agente = create_agent(
            self.llm,
            tools=ferramentas,
            system_prompt=(
                "Você é um assistente especializado no ProgressoFit — uma plataforma web para monitoramento e evolução de treinos, "
                "que permite registrar exercícios, cargas, tempos e métricas, gerando relatórios, gráficos de evolução e recomendações "
                "personalizadas com apoio de inteligência artificial.\n\n"
                "Regras:\n"
                "- Sempre use a ferramenta buscar_documentos antes de responder qualquer pergunta\n"
                "- Responda APENAS com as informações contidas nos documentos\n"
                "- Responda APENAS o que foi perguntado, de forma concisa\n"
                "- NÃO reformate nem despeje o documento inteiro na resposta\n"
                "- Sintetize com suas próprias palavras\n"
                "- Se a pergunta for simples, a resposta deve ser curta e direta\n"
                "- Não use linguagem técnica se não for necessário, responda de forma simples e acessível\n"
            ),
        )

        while True:
            pergunta = input("\nVocê: ").strip()
            if not pergunta:
                continue

            resultado = agente.invoke({
                "messages": [{"role": "user", "content": pergunta}]
            })

            resposta = resultado["messages"][-1].content
            print(f"\nAgente: {resposta}")
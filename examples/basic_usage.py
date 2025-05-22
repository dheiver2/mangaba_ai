#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exemplo básico de uso do Mangaba.AI com protocolos A2A e MCP
"""
import asyncio
from mangaba_ai.main import MangabaAI
import os

async def main():
    """Função principal do exemplo."""
    try:
        # Chave de API do Gemini
        api_key = os.getenv("GEMINI_API_KEY")
        
        # Inicializa o Mangaba.AI
        mangaba = MangabaAI(api_key)
        
        # Cria agentes com diferentes papéis
        researcher = mangaba.create_agent(
            name="pesquisador",
            role="Pesquisador",
            goal="Realizar pesquisas detalhadas sobre tópicos específicos"
        )
        
        analyst = mangaba.create_agent(
            name="analista",
            role="Analista",
            goal="Analisar dados e informações"
        )
        
        writer = mangaba.create_agent(
            name="escritor",
            role="Escritor",
            goal="Escrever relatórios e resumos"
        )
        
        # Demonstra comunicação A2A
        print("\nDemonstrando comunicação entre agentes (A2A):")
        
        # Pesquisador envia mensagem para o analista
        print("\nPesquisador -> Analista: 'Analise estes dados sobre IA'")
        await researcher.a2a.send_message(
            researcher.name,
            analyst.name,
            "Analise estes dados sobre IA: [dados de pesquisa]"
        )
        
        # Analista processa a mensagem e responde
        messages = await analyst.a2a.receive_messages(analyst.name)
        for msg in messages:
            print(f"\nAnalista recebeu: {msg['content']}")
            response = await analyst.execute(msg["content"])
            print(f"Analista responde: {response}")
            
            # Analista envia para o escritor
            await analyst.a2a.send_message(
                analyst.name,
                writer.name,
                f"Escreva um relatório baseado nesta análise: {response}"
            )
        
        # Escritor processa a mensagem
        messages = await writer.a2a.receive_messages(writer.name)
        for msg in messages:
            print(f"\nEscritor recebeu: {msg['content']}")
            response = await writer.execute(msg["content"])
            print(f"Escritor responde: {response}")
        
        # Demonstra uso do MCP
        print("\nDemonstrando fusão de contexto (MCP):")
        
        # Executa tarefas sequenciais para demonstrar o contexto
        tasks = [
            {
                "type": "researcher",
                "description": "Pesquise sobre os últimos avanços em IA generativa"
            },
            {
                "type": "analyzer",
                "description": "Analise os impactos desses avanços na indústria"
            },
            {
                "type": "writer",
                "description": "Escreva um relatório sobre os resultados da análise"
            }
        ]
        
        print("\nExecutando tarefas sequenciais com contexto:")
        results = await mangaba.execute(tasks)
        
        # Exibe os resultados
        print("\nResultados:")
        for task, result in results.items():
            print(f"\nTarefa: {task}")
            print(f"Resultado: {result}")
            
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main()) 

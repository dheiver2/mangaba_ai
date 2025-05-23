#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exemplo simples do Mangaba.AI demonstrando o uso básico de um agente
"""
import asyncio
from mangaba_ai.main import MangabaAI
import os

async def main():
    """Função principal do exemplo."""
    try:
        # Inicializa o Mangaba.AI com sua chave de API
        api_key = os.getenv("GEMINI_API_KEY")
        mangaba = MangabaAI(api_key)
        
        # Cria um agente assistente
        assistant = mangaba.create_agent(
            name="assistente",
            role="Assistente Virtual",
            goal="Ajudar usuários com suas dúvidas e tarefas"
        )
        
        # Lista de tarefas simples para o assistente
        tasks = [
            "Explique o que é inteligência artificial em 3 frases",
            "Quais são as principais aplicações de IA hoje em dia?",
            "Dê 3 dicas para começar a estudar IA"
        ]
        
        print("\nExecutando tarefas com o assistente:")
        print("-" * 50)
        
        # Executa cada tarefa e mostra o resultado
        for i, task in enumerate(tasks, 1):
            print(f"\nTarefa {i}: {task}")
            response = await assistant.execute(task)
            print(f"Resposta: {response}")
            print("-" * 50)
            
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main()) 
"""
Módulo principal do Mangaba.AI
"""
import asyncio
import logging
import os
from .core.models import Agent, Task, GeminiModel

logger = logging.getLogger(__name__)

class MangabaAI:
    """Classe principal do Mangaba.AI."""
    
    def __init__(self, api_key: str):
        """Inicializa o sistema Mangaba.AI."""
        self.api_key = api_key
        self.model = GeminiModel(api_key)
    
    def create_agent(self, name: str, role: str, goal: str) -> Agent:
        """Cria um novo agente."""
        return Agent(
            name=name,
            role=role,
            model=self.model,
            goal=goal
        )
    
    def create_task(self, description: str, agent: Agent) -> Task:
        """Cria uma nova tarefa."""
        return Task(
            description=description,
            agent=agent
        )
    
    async def execute(self, tasks: list) -> dict:
        """Executa uma lista de tarefas."""
        results = {}
        
        try:
            for task in tasks:
                task_description = None
                try:
                    if isinstance(task, dict):
                        task_description = task["description"]
                        agent = self.create_agent(
                            name=f"agent_{task['type']}",
                            role=task["type"],
                            goal=task["description"]
                        )
                        task_obj = self.create_task(
                            description=task_description,
                            agent=agent
                        )
                    else:
                        task_description = task.description
                        task_obj = task
                    
                    result = await task_obj.agent.execute(task_obj.description)
                    results[task_description] = result
                
                except Exception as e:
                    logger.error(f"Erro ao executar tarefa: {e}")
                    if task_description:
                        results[task_description] = f"Erro: {str(e)}"
                    else:
                        results["unknown_task"] = f"Erro: {str(e)}"
            
            return results
        
        except Exception as e:
            logger.error(f"Erro geral na execução: {e}")
            raise

async def main():
    """Função principal de execução."""
    try:
        # Inicializa o Mangaba.AI
        mangaba = MangabaAI(os.getenv("GEMINI_API_KEY"))
        
        # Cria agentes com diferentes modelos
        researcher = mangaba.create_agent(
            name="pesquisador",
            role="Pesquisador",
            goal="Realizar pesquisas"
        )
        
        analyst = mangaba.create_agent(
            name="analista",
            role="Analista",
            goal="Analisar dados"
        )
        
        writer = mangaba.create_agent(
            name="escritor",
            role="Escritor",
            goal="Escrever resumos"
        )
        
        # Cria tarefas
        task1 = mangaba.create_task(
            description="Pesquisar sobre IA generativa",
            agent=researcher
        )
        
        task2 = mangaba.create_task(
            description="Analisar os resultados da pesquisa",
            agent=analyst
        )
        
        task3 = mangaba.create_task(
            description="Escrever um resumo dos resultados",
            agent=writer
        )
        
        # Executa tarefas
        results = await mangaba.execute([task1, task2, task3])
        
        # Exibe resultados
        for task, result in results.items():
            logger.info(f"Tarefa: {task}")
            logger.info(f"Resultado: {result}\n")
            
    except Exception as e:
        logger.error(f"Erro durante a execução: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main()) 
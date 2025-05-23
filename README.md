# 🚀 Mangaba.AI

<p align="center">
  <img src="assets/img2.png" width="400" alt="Mangaba.AI logo">
</p>

> Framework para desenvolvimento de equipes de agentes de IA autônomos.

---

## 🎯 O que é o Mangaba.AI?

O Mangaba.AI é um framework que permite criar e gerenciar equipes de agentes de IA que trabalham juntos para resolver tarefas complexas. Com ele, você pode:

- ✅ Criar agentes especializados (pesquisadores, analistas, escritores, etc.)
- ✅ Permitir que os agentes se comuniquem entre si
- ✅ Executar tarefas sequenciais com contexto compartilhado
- ✅ Integrar com diferentes modelos de IA (Gemini, OpenAI, Anthropic)

---

## ⚡ Instalação e primeiros passos

### 1️⃣ Configure suas credenciais

- Crie uma chave de API no [Google AI Studio](https://makersuite.google.com/app/apikey).
- Copie o arquivo de exemplo:

```bash
cp env.example .env
````

* Edite o arquivo `.env` e insira sua chave de API:

```env
GEMINI_API_KEY=SuaApiKeyAqui
```

---

### 2️⃣ Configure o ambiente Python (recomendado)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate      # Windows
```

---

### 3️⃣ Instale as dependências e o Mangaba.AI

```bash
# Instale as dependências
pip install -r requirements.txt

# Instale o Mangaba.AI
pip install -e .
```

---

### 4️⃣ Execute seu primeiro exemplo

```bash
python examples/basic_usage.py
```

Você verá três agentes colaborando:

* 🔍 Um pesquisador buscando informações
* 📊 Um analista processando os dados
* ✍️ Um escritor gerando relatórios

---

## 🛠️ Funcionalidades principais

* 🤖 **Agentes Autônomos** — Crie agentes com papéis e objetivos específicos
* 🔗 **Comunicação entre agentes (A2A)**
* 🧠 **Memória e Contexto Persistente (MCP)**
* 🌐 **Suporte a múltiplos modelos:** Gemini, OpenAI, Anthropic
* 🔌 **Integrações prontas:** Slack, GitHub, Jira, Discord

---

## 📚 Documentação

A documentação completa está na pasta [`docs/`](docs/):

* [Agentes](docs/agents.md)
* [Tarefas](docs/tasks.md)
* [Comunicação](docs/communication.md)
* [Memória](docs/memory.md)
* [Modelos](docs/models.md)
* [Fluxo de Trabalho](docs/workflow.md)
* [Configuração](docs/configuration.md)

---

## 🧪 Exemplos

Veja mais exemplos na pasta [`examples/`](examples/):

* [Exemplo completo](examples/full_system_example.py)
* [Integrações](examples/platform_integrations/)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja o arquivo [`CONTRIBUTING.md`](CONTRIBUTING.md) para diretrizes.

---

## 📄 Licença

Distribuído sob a licença MIT. Veja [`LICENSE`](LICENSE) para mais informações.



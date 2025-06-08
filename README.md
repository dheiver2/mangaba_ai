<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mangaba.AI - Intelligent Autonomous Agents Framework</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .fade-in {
            animation: fadeIn 1s ease-in;
        }
    </style>
</head>
<body class="bg-gradient-to-br from-gray-100 to-gray-200 text-gray-800 font-sans">
    <header class="bg-gradient-to-r from-red-600 to-green-600 text-white py-6 text-center">
        <img src="logo.png" alt="Mangaba.AI Logo" class="mx-auto w-24 h-auto transition-transform duration-300 hover:scale-110">
        <h1 class="text-4xl font-bold mt-2">Mangaba.AI</h1>
        <p class="text-lg">Framework for Developing Intelligent Autonomous Agents</p>
    </header>

    <div class="flex flex-col md:flex-row">
        <!-- Sidebar Navigation -->
        <nav class="bg-green-600 text-white w-full md:w-64 p-4 space-y-2 sticky top-0 z-10">
            <a href="#overview" class="block px-4 py-2 hover:bg-yellow-400 hover:text-gray-800 rounded transition-colors duration-200">Overview</a>
            <a href="#structure" class="block px-4 py-2 hover:bg-yellow-400 hover:text-gray-800 rounded transition-colors duration-200">Project Structure</a>
            <a href="#installation" class="block px-4 py-2 hover:bg-yellow-400 hover:text-gray-800 rounded transition-colors duration-200">Installation</a>
            <a href="#usage" class="block px-4 py-2 hover:bg-yellow-400 hover:text-gray-800 rounded transition-colors duration-200">Usage</a>
            <a href="#documentation" class="block px-4 py-2 hover:bg-yellow-400 hover:text-gray-800 rounded transition-colors duration-200">Documentation</a>
            <a href="#development" class="block px-4 py-2 hover:bg-yellow-400 hover:text-gray-800 rounded transition-colors duration-200">Development</a>
            <a href="#contributing" class="block px-4 py-2 hover:bg-yellow-400 hover:text-gray-800 rounded transition-colors duration-200">Contributing</a>
            <a href="#license" class="block px-4 py-2 hover:bg-yellow-400 hover:text-gray-800 rounded transition-colors duration-200">License</a>
        </nav>

        <!-- Main Content -->
        <main class="flex-1 p-6">
            <div class="space-y-8">
                <section id="overview" class="fade-in">
                    <h2 class="text-3xl font-semibold text-red-600 border-b-4 border-green-600 pb-2 mb-4">Overview</h2>
                    <p class="text-lg">Mangaba.AI is a powerful framework designed to simplify the development of intelligent autonomous agents. It provides a modular structure, comprehensive tools, and seamless integrations to create, manage, and execute agent-based tasks efficiently.</p>
                </section>

                <section id="structure" class="fade-in">
                    <h2 class="text-3xl font-semibold text-red-600 border-b-4 border-green-600 pb-2 mb-4">Project Structure</h2>
                    <button class="bg-yellow-400 text-gray-800 px-4 py-2 rounded hover:bg-red-600 hover:text-white transition-colors duration-200" onclick="toggleSection('structure-content')">Show/Hide Structure</button>
                    <div id="structure-content" class="hidden mt-4">
                        <pre class="bg-gray-100 p-4 rounded overflow-x-auto"><code>
mangaba_ai/
├── .github/                    # GitHub configurations
├── docs/                       # Documentation
│   ├── api/                   # API documentation
│   ├── guides/                # Usage guides
│   └── examples/              # Documented examples
├── src/                       # Source code
│   ├── core/                  # Framework core
│   │   ├── agents/           # Agent implementations
│   │   ├── models/           # Data models
│   │   ├── protocols/        # Protocols and interfaces
│   │   └── tools/            # Base tools
│   ├── integrations/         # Optional integrations
│   └── utils/                # General utilities
├── tests/                     # Tests
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── e2e/                  # End-to-end tests
├── examples/                  # Examples
│   ├── basic/                # Basic examples
│   └── advanced/             # Advanced examples
└── scripts/                   # Utility scripts
                        </code></pre>
                    </div>
                </section>

                <section id="installation" class="fade-in">
                    <h2 class="text-3xl font-semibold text-red-600 border-b-4 border-green-600 pb-2 mb-4">Installation</h2>
                    <ol class="list-decimal list-inside space-y-2 text-lg">
                        <li>Clone the repository:
                            <pre class="bg-gray-100 p-4 rounded mt-2"><code>git clone https://github.com/your-username/mangaba_ai.git
cd mangaba_ai</code></pre>
                        </li>
                        <li>Create and activate a virtual environment:
                            <pre class="bg-gray-100 p-4 rounded mt-2"><code>python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows</code></pre>
                        </li>
                        <li>Install dependencies:
                            <pre class="bg-gray-100 p-4 rounded mt-2"><code>pip install -r requirements.txt</code></pre>
                        </li>
                        <li>Configure environment variables:
                            <pre class="bg-gray-100 p-4 rounded mt-2"><code>cp .env.example .env
# Edit the .env file with your settings</code></pre>
                        </li>
                    </ol>
                </section>

                <section id="usage" class="fade-in">
                    <h2 class="text-3xl font-semibold text-red-600 border-b-4 border-green-600 pb-2 mb-4">Basic Usage</h2>
                    <button class="bg-yellow-400 text-gray-800 px-4 py-2 rounded hover:bg-red-600 hover:text-white transition-colors duration-200" onclick="toggleSection('usage-content')">Show/Hide Code</button>
                    <div id="usage-content" class="hidden mt-4">
                        <pre class="bg-gray-100 p-4 rounded overflow-x-auto"><code>from mangaba_ai import MangabaAI

# Initialize the framework
ai = MangabaAI()

# Create an agent
agent = ai.create_agent(
    name="my_agent",
    role="Analyst",
    goal="Analyze data and generate insights"
)

# Create a task
task = ai.create_task(
    description="Analyze sales data",
    agent=agent
)

# Execute the task
result = await ai.execute([task])</code></pre>
                    </div>
                </section>

                <section id="documentation" class="fade-in">
                    <h2 class="text-3xl font-semibold text-red-600 border-b-4 border-green-600 pb-2 mb-4">Documentation</h2>
                    <ul class="list-disc list-inside space-y-2 text-lg">
                        <li><a href="docs/guides/quickstart.md" class="text-red-600 hover:underline">Quick Start Guide</a></li>
                        <li><a href="docs/api/README.md" class="text-red-600 hover:underline">API Documentation</a></li>
                        <li><a href="docs/examples/README.md" class="text-red-600 hover:underline">Examples</a></li>
                    </ul>
                </section>

                <section id="development" class="fade-in">
                    <h2 class="text-3xl font-semibold text-red-600 border-b-4 border-green-600 pb-2 mb-4">Development</h2>
                    <ol class="list-decimal list-inside space-y-2 text-lg">
                        <li>Install development dependencies:
                            <pre class="bg-gray-100 p-4 rounded mt-2"><code>pip install -r requirements-dev.txt</code></pre>
                        </li>
                        <li>Configure pre-commit hooks:
                            <pre class="bg-gray-100 p-4 rounded mt-2"><code>pre-commit install</code></pre>
                        </li>
                        <li>Run tests:
                            <pre class="bg-gray-100 p-4 rounded mt-2"><code>pytest</code></pre>
                        </li>
                    </ol>
                </section>

                <section id="contributing" class="fade-in">
                    <h2 class="text-3xl font-semibold text-red-600 border-b-4 border-green-600 pb-2 mb-4">Contributing</h2>
                    <ol class="list-decimal list-inside space-y-2 text-lg">
                        <li>Fork the project</li>
                        <li>Create your feature branch (<pre class="inline bg-gray-100 p-2 rounded"><code>git checkout -b feature/new-feature</code></pre>)</li>
                        <li>Commit your changes (<pre class="inline bg-gray-100 p-2 rounded"><code>git commit -am 'Add new feature'</code></pre>)</li>
                        <li>Push to the branch (<pre class="inline bg-gray-100 p-2 rounded"><code>git push origin feature/new-feature</code></pre>)</li>
                        <li>Create a Pull Request</li>
                    </ol>
                </section>

                <section id="license" class="fade-in">
                    <h2 class="text-3xl font-semibold text-red-600 border-b-4 border-green-600 pb-2 mb-4">License</h2>
                    <p class="text-lg">This project is licensed under the MIT License - see the <a href="LICENSE" class="text-red-600 hover:underline">LICENSE</a> file for details.</p>
                </section>
            </div>
        </main>
    </div>

    <footer class="bg-green-600 text-white py-4 text-center mt-8">
        <p>© 2025 Mangaba.AI. All rights reserved.</p>
    </footer>

    <script>
        function toggleSection(sectionId) {
            const section = document.getElementById(sectionId);
            section.classList.toggle('hidden');
        }
    </script>
</body>
</html>

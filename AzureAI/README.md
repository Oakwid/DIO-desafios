# Resumo do Curso de Azure AI  

## Foco: IA Generativa, Speech e Language

### 1. Introdução à IA Generativa

- **Definição:**  
  A IA generativa é capaz de criar conteúdo original em diversos formatos — como texto, código e imagem — ao imitar comportamentos humanos.
- **Aplicações:**  
  - Chatbots e assistentes conversacionais  
  - Geração de código, resumir textos e elaborar apresentações  
  - Criação e edição de imagens (ex.: uso do DALL-E)

### 2. Modelos de Linguagem Grandes (LLMs)

- **Arquitetura do Transformador:**  
  - **Codificador:** Cria representações semânticas a partir do vocabulário do treinamento.  
  - **Decodificador:** Utiliza essas representações para prever a sequência mais provável de tokens.
- **Tokenização e Inserções:**  
  - O processo de converter textos em tokens numéricos, onde palavras são representadas por valores únicos.
  - **Embeddings:** Inserções que capturam as relações semânticas entre os tokens para determinar a próxima palavra.
- **Mecanismo de Atenção:**  
  - Atribui “peso” às relações entre os tokens, ajudando o modelo a focar nas partes mais relevantes do texto.

### 3. Engenharia de Prompts

- **Objetivo:**  
  Otimizar as respostas da IA através de perguntas e instruções bem definidas.
- **Técnicas Utilizadas:**  
  - Linguagem direta e instruções precisas (ex.: “Crie uma lista de 10 coisas para fazer em Edimburgo durante o mês de agosto”)  
  - Utilização de mensagens do sistema e exemplos para guiar o comportamento do modelo  
  - Inclusão de dados de fundamentação para contextualizar o prompt

### 4. Serviço OpenAI do Azure

- **Recursos e Funcionalidades:**  
  - Hospedagem, customização e implantação de LLMs, incluindo modelos como GPT-4, GPT-3.5, e DALL-E para geração de imagem.
  - Métodos de desenvolvimento:  
    - Azure OpenAI Studio  
    - API REST, SDKs e interface de linha de comando  
  - Segurança corporativa integrada (RBAC e redes privadas) para proteger os dados.
- **Casos de Uso:**  
  - Geração e resumo de textos  
  - Tradução, análise de sentimentos e extração de informações  
  - Automação de geração de código e criação de conteúdos visuais

### 5. Funcionalidades de Linguagem Natural do Azure

- **Capacidades oferecidas:**  
  - Processamento de linguagem natural para análise de texto e mineração de opiniões  
  - Detecção automática de idioma e análise de sentimento  
  - Serviços de conversão de fala para texto e vice-versa, além de tradução e síntese de fala
- **Ferramentas:**  
  - Azure Cognitive Services com Language Studio  
  - Serviços de bot para criar experiências interativas

### 6. IA Generativa Responsável

- **Princípios e Desafios:**  
  - Imparcialidade, transparência, privacidade, confiabilidade e segurança  
  - Processo de desenvolvimento dividido em fases: Identificar, Medir, Mitigar e Operar
- **Importância:**  
  Garantir que as soluções baseadas em IA sejam éticas, seguras e confiáveis, respeitando a privacidade dos dados.

### 7. Outras Aplicações e Conceitos Abordados

- **Copilotos:**  
  Ferramentas integradas (ex.: no Microsoft 365, Microsoft Teams e GitHub Copilot) que auxiliam em tarefas do dia a dia, aumentando a produtividade e a criatividade.
- **Aprendizado de Máquina e Profundo:**  
  - Fundamentos sobre treinamento, avaliação e implantação de modelos.
  - Uso de redes neurais para generalização e previsão com base em dados históricos.
  
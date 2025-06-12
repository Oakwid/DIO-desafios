# Resumo dos Meus Aprendizados no Copilot Studio

## Configuração de Ambientes na Power Platform

- **Ambientes na Power Platform:** Compreensão sobre os tipos (`Sandbox`, `Produção`, `Desenvolvimento`) e suas diferenças funcionais.
- **Ambiente híbrido:** Conversão de um ambiente `Sandbox` para `Produção` com o objetivo de organizar implantações e validações antes de liberar em produção.

## Power Apps e Migração de Soluções

- **Criação de soluções:** Uso do `Dataverse` como repositório de dados e desenvolvimento de aplicativos com `Canvas Apps` e `Model-driven Apps`.
- **Organização para migração:** Gerenciamento de componentes via `Explorador de Soluções` para facilitar reusabilidade e controle.
- **Pipelines de implantação:** Criação de pipelines para automatizar a migração de soluções entre ambientes (ex.: Dev → Teste → Produção).
- **Migração de soluções:** Processo de empacotamento (exportação) e reaproveitamento (importação) entre ambientes, com validação de integridade e versões.

## Copilot Studio e Criação de Agentes

### Fundamentos

- **Agentes baseados em modelos:** Aceleração da criação por meio de templates prontos disponíveis no Copilot Studio.
- **Criação com descrição:** Geração de tópicos por linguagem natural, descrevendo a intenção do fluxo desejado.
- **Configuração de respostas inteligentes:** Estruturação de `intenções` e `entidades` para interpretar entradas e guiar a conversa.
- **Criação de agente do zero:** Construção manual de fluxos de diálogo e configuração dos comportamentos com base na lógica desejada.

---

## Recursos Avançados no Copilot Studio

### Tópicos e Conversação

- **Introdução a tópicos:** Dividem o assistente em blocos reutilizáveis de conversa.
- **Boas práticas:** Nomeação clara, intenção única por tópico e escopo controlado para facilitar manutenção.
- **Criação com descrição:** Permite iniciar um fluxo com uma simples descrição do objetivo em linguagem natural.
- 📘 *Referência:* [Fundamentos – Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)

### Ramificação de Tópicos

- **Quando ramificar:** Quando múltiplos caminhos ou decisões dependem da entrada do usuário.
- **Criação de condições:** Uso de expressões condicionais com base em variáveis ou entidades.
- **Redirecionamento de fluxo:** Encaminhar a conversa para outro tópico utilizando a ação “Chamar tópico”.
- **Transferência de controle:** Permite que um tópico delegue a condução para outro sem perder contexto.
- **Encerramento da conversa:** Uso do nó “Fim da conversa” com mensagens de fechamento personalizadas.

### Fallback (falhas de compreensão)

- **Configuração de falha:** Definição de respostas padrão quando a entrada não é reconhecida.
- **Fallbacks personalizados:** Tópicos que tratam falhas específicas para melhorar a experiência do usuário.
- 📘 *Referência:* [Gerenciar falhas e retomadas – Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/)

### Entidades e Variáveis

#### Entidades

- **O que são:** Elementos que capturam dados fornecidos na conversa (ex.: datas, localizações, nomes).
- **Uso de entidades existentes:** Aproveitamento das entidades prontas do sistema (ex.: `datetime`, `number`).
- **Criação de novas entidades:** Por lista personalizada ou expressões regulares (`Regex`) para padrões mais flexíveis.
- **Melhores práticas:** Usar nomes claros, evitar sobreposição de significado e revisar conflitos com entidades do sistema.

#### Variáveis

- **Definição e uso:** Armazenamento de informações temporárias durante a execução do agente.
- **Tipos de variáveis:** Escopo de `tópico` (local) e `global` (compartilhado entre tópicos).
- **Testes e gerenciamento:** Monitoramento pelo painel de variáveis, validação de valores em tempo real.
- **Uso com cartões adaptáveis:** Inserção de variáveis em conteúdos dinâmicos e interativos com Adaptive Cards.

### Respostas Generativas com IA

- **Definição:** Respostas criadas por modelos de IA generativa com base na entrada do usuário.
- **Configuração:** Nas opções de resposta, ativando “Usar geração de IA” para o nó desejado.
- **Conceitos de GenAI:** Uso de LLMs (Large Language Models) que aumentam a flexibilidade e naturalidade das respostas.
- **Melhores práticas:** Fornecer contexto claro, limitar escopo e validar os resultados gerados.
- **Knowledge sources:** Conexão com fontes de conhecimento (internas ou externas) para fornecer respostas mais ricas e atualizadas.
- 📘 *Referência:* [IA generativa no Copilot Studio – Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/generative-answers)

---

## Desafio Prático Concluído

Desenvolvido com base em lições aprendidas e práticas recomendadas por profissionais da comunidade, incluindo MVPs da Microsoft:

- Criação de um Copilot do zero (em branco).
- Customização de um tópico com respostas e ações.
- Personalização da mensagem de erro de um tópico.
- Ajuste da qualidade de resposta com GenAI (aumentar e diminuir "criatividade").

---

## Fontes e Referências

- 📘 [Documentação Oficial – Microsoft Learn](https://learn.microsoft.com/pt-br/microsoft-copilot-studio/)
- 🎓 [Portal de Aprendizado – romaos.com.br](https://romaos.com.br/learn/)
- ▶️ [Canal YouTube – Douglas Romão (MVP)](https://www.youtube.com/@douglasromao)

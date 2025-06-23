# PRD - Website Institucional do Programa Cerrado em Rede

## 1. Visão Geral e Objetivos

O projeto visa desenvolver o website institucional para o **Programa Cerrado em Rede**. O site servirá como uma plataforma central para apresentar o programa, suas iniciativas, pesquisas e materiais educativos. O objetivo é criar uma presença online profissional, informativa e inspiradora que comunique a missão, visão e valores do programa, além de oferecer ferramentas interativas como o Geoportal e trilhas de formação.

O projeto também prevê uma futura integração com um assistente de IA para interagir com os usuários, tornando o acesso à informação mais dinâmico.

## 2. Tecnologias Principais

-   **Linguagem**: HTML5, CSS3, JavaScript (ES6+)
-   **Framework CSS**: Tailwind CSS (via CDN) para estilização moderna e responsiva.
-   **Bibliotecas**: Font Awesome (para ícones), Google Fonts (Montserrat, Inter).
-   **Banco de Dados**: Não aplicável na fase atual (website estático).
-   **Sistema de LLM (planejado)**: Futura integração com um modelo de linguagem (ex: OpenAI API) para alimentar um chatbot.
-   **Ambiente de Desenvolvimento**: Servidor local (`python -m http.server`).
-   **Hospedagem (sugerida)**: Plataformas de hospedagem para sites estáticos como Netlify, Vercel ou GitHub Pages.

## 3. Arquitetura do Site

O site foi reestruturado de uma página única (single-page) para uma arquitetura de múltiplas páginas, melhorando a organização e a escalabilidade do conteúdo.

-   `website.html`: Página inicial (Home), com as seções principais e links para as páginas internas.
-   `geoportal.html`: Página dedicada ao Geoportal, com seções para diferentes categorias de dados.
-   `gestao-publica.html`: Página da trilha de formação em Gestão Pública.
-   `desenvolvimento-sustentavel.html`: Página da trilha de formação em Desenvolvimento Sustentável.
-   `analise-dados.html`: Página da trilha de formação em Análise de Dados.

## 4. Fases de Implementação

### Fase 1: Estrutura e Conteúdo Inicial (Concluída)

-   **Tarefa 1.1**: Configuração do ambiente de desenvolvimento e estrutura inicial do `website.html` com Tailwind CSS.
-   **Tarefa 1.2**: Correção da exibição da logo e substituição de imagens por conteúdo temático do Cerrado.
-   **Tarefa 1.3**: Criação e estilização da seção "Quem Somos", com Missão, Visão e Valores extraídos do manual da marca.
-   **Tarefa 1.4**: Implementação de responsividade para o menu de navegação e layout geral.

### Fase 2: Arquitetura Multi-Página (Concluída)

-   **Tarefa 2.1**: Criação dos arquivos HTML para o Geoportal e as três Trilhas de Formação, mantendo a consistência visual.
-   **Tarefa 2.2**: Atualização dos links e botões na `website.html` para direcionar às novas páginas internas.

### Fase 3: Detalhamento de Conteúdo e Funcionalidades Avançadas (Pendente)

-   **Tarefa 3.1**: Popular as páginas internas (`geoportal.html`, trilhas) com conteúdo detalhado, textos, imagens e, se necessário, elementos interativos.
-   **Tarefa 3.2**: Planejar a arquitetura para a integração do assistente de IA (chatbot).
-   **Tarefa 3.3**: Desenvolver o backend ou as funções serverless para conectar com a API do LLM.
-   **Tarefa 3.4**: Implementar e estilizar o widget do chatbot no frontend.

## 5. Pontos de Atenção

-   **Identidade Visual**: Manter estrita conformidade com o `manualdamarca.txt` em todas as novas páginas e conteúdos.
-   **Conteúdo**: O conteúdo final para as páginas internas precisa ser fornecido ou elaborado.
-   **Escalabilidade**: A integração com a IA exigirá uma mudança de arquitetura de puramente estática para uma que inclua um backend ou serviços serverless.

# Plano Estratégico e de Ação do Projeto

---

## 1. A Identidade do Programa

**Nome Oficial:**
> Programa de Educação Ambiental e Formação Profissional voltado para o Desenvolvimento Sustentável no bioma do Cerrado

**Conceito Central:**
> Cerrado em Rede: A Conexão do Saber

**Slogan / Tagline:**
> "Conhecimento que Transforma, Futuro que Floresce no Cerrado."

### 1.1. Missão, Visão e Valores

*   **Missão:** Promover a educação ambiental e a formação profissional qualificada, gerando e disseminando conhecimento científico e prático para o desenvolvimento sustentável do bioma do Cerrado, fomentando a conservação, a valorização da sociobiodiversidade e o uso responsável dos recursos naturais.

*   **Visão:** Ser reconhecido como um programa de referência nacional e internacional na construção de soluções inovadoras e sustentáveis para os desafios do Cerrado, consolidando uma rede de conhecimento e atuação em defesa e valorização do bioma.

*   **Valores:**
    *   **Sustentabilidade:** Compromisso com o equilíbrio ambiental, social e econômico.
    *   **Inovação:** Busca contínua por novas abordagens e soluções criativas.
    *   **Colaboração:** Fomento a redes de conhecimento e parcerias estratégicas.
    *   **Transparência:** Atuação ética, clara e responsável.
    *   **Respeito:** Valorização da diversidade cultural e biológica do Cerrado.
    *   **Excelência:** Busca pela qualidade e rigor científico em todas as atividades.

---

## 2. Objetivos e Etapas do Projeto (Extraído do Planejamento)

O portal web é uma ferramenta central para a execução das 5 etapas macro do projeto:

*   **Etapa 1: Interpretação das Funções Ecossistêmicas:**
    *   Caracterizar regiões do Cerrado, analisar ecossistemas e valorar bens e serviços ambientais.

*   **Etapa 2: Mapeamento de Elementos Simbólicos e Culturais:**
    *   Diagnosticar acesso a saneamento, recursos hídricos e uso da terra nos territórios estudados.

*   **Etapa 3: Caracterização do Estado da Arte e Disseminação:**
    *   **Atividade Chave:** Desenvolver a página web e o banco de dados para armazenar e disseminar as informações geradas.
    *   Organizar um Ciclo de Rodas de Conversas Temáticas.

*   **Etapa 4: Aprimoramento do Conhecimento (Capacitação):**
    *   Promover cursos e treinamentos para lideranças e gestores municipais.

*   **Etapa 5: Apoio à Gestão Ambiental Municipal:**
    *   A página web servirá como ferramenta de apoio à estruturação da gestão ambiental nos municípios.

---

## 3. Plano de Ação para o Portal Web

### Fase 1: Fundação e Identidade (Concluída)

*   **Status:** 100% Concluído.
*   **Entregas:**
    *   Estrutura inicial do site com Flask.
    *   Páginas institucionais estáticas (Home, Sobre, Contato).
    *   Aplicação da identidade visual (cores, fontes) conforme o manual da marca.
    *   Deploy funcional na Vercel.

### Fase 2: Estruturação do Backend e Banco de Dados (Próximos Passos)

*   **Objetivo:** Tornar o site dinâmico e prepará-lo para receber conteúdo.
*   **Tarefas:**
    1.  Escolha e configuração de um banco de dados (Sugestão: PostgreSQL).
    2.  Instalação e configuração do SQLAlchemy no projeto Flask.
    3.  Criação dos modelos de dados: `Curso`, `Publicacao`, `Noticia`, `CamadaGeoespacial`.
    4.  Desenvolvimento de uma área administrativa (Flask-Admin) para gerenciamento de conteúdo.

### Fase 3: Desenvolvimento dos Módulos Principais

*   **Objetivo:** Construir as funcionalidades centrais do portal.
*   **Módulos:**
    1.  **Geoportal Interativo:**
        *   Integrar o `Leaflet.js` no frontend.
        *   Criar rotas de API no Flask para servir dados geoespaciais do banco de dados.
        *   Permitir a visualização de camadas de dados no mapa.
    2.  **Plataforma de Cursos (Trilhas de Formação):**
        *   Criar uma página que lista dinamicamente os cursos disponíveis.
        *   Desenvolver um template para a página de cada curso, exibindo descrição, módulos, vídeos e materiais para download.
    3.  **Biblioteca de Conhecimento:**
        *   Criar uma seção para listar publicações, artigos e relatórios do projeto.
        *   Permitir a busca e o filtro por tema ou ano.

---

## 4. Pilha Tecnológica (Stack)

*   **Backend:** Python com Flask.
*   **Frontend:** HTML, Tailwind CSS, JavaScript.
*   **Banco de Dados:** PostgreSQL (Recomendado).
*   **ORM:** SQLAlchemy com Flask-SQLAlchemy.
*   **Geoprocessamento:** GeoPandas (backend), Leaflet.js (frontend).
*   **Deploy:** Vercel.

## 5. Pontos de Atenção

*   **Ponto 1:** Garantir a consistência da identidade visual em todas as páginas do portal.
*   **Ponto 2:** Realizar testes rigorosos de usabilidade e acessibilidade antes do lançamento público.

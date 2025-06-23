# Programa de Educação Ambiental e Formação Profissional no Cerrado

Este repositório contém o código-fonte do portal web do **Programa de Educação Ambiental e Formação Profissional voltado para o Desenvolvimento Sustentável no bioma do Cerrado**.

O portal serve como uma ferramenta central para a disseminação de conhecimento, capacitação e apoio à gestão ambiental, alinhado com os objetivos estratégicos do programa.

---

## Documentação do Projeto

Toda a documentação estratégica e o acompanhamento de tarefas estão centralizados nos seguintes arquivos:

-   **[PLANO_PROJETO.md](./templates/PLANO_PROJETO.md)**: O documento mestre. Contém a identidade do programa, os objetivos, as etapas e o plano de ação detalhado. **Consulte este arquivo para a visão completa do projeto.**
-   **[TASKS.md](./TASKS.md)**: A lista de tarefas atualizada, dividida por fases, para acompanhamento do progresso.

---

## Pilha Tecnológica (Stack)

-   **Backend:** Python com Flask.
-   **Frontend:** HTML, Tailwind CSS, JavaScript.
-   **Banco de Dados (Planejado):** PostgreSQL com SQLAlchemy.
-   **Geoprocessamento (Planejado):** GeoPandas (backend), Leaflet.js (frontend).
-   **Deploy:** Vercel.

---

## Como Executar o Projeto Localmente

**Pré-requisitos:**
-   Ter o [Python](https://www.python.org/downloads/) instalado.

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DA_PASTA>
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # MacOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    flask run
    ```

5.  **Acesse no navegador:** [http://127.0.0.1:5000](http://127.0.0.1:5000)

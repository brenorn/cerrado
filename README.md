# Website Institucional - Programa Cerrado em Rede

Este repositório contém o código-fonte do website institucional do Programa Cerrado em Rede. O projeto foi desenvolvido para ser uma plataforma informativa, apresentando o programa, suas trilhas de formação e o Geoportal interativo.

## Visão Geral do Projeto

O site foi construído com uma abordagem moderna e responsiva, utilizando HTML semântico e Tailwind CSS para a estilização. A estrutura evoluiu de uma página única para um site com múltiplas páginas, permitindo uma melhor organização e escalabilidade do conteúdo.

Para mais detalhes sobre os requisitos, fases e arquitetura, consulte o arquivo `PRD.md`.

Para um acompanhamento das tarefas, veja o `TASKS.md`.

## Tecnologias Utilizadas

-   **Frontend**:
    -   HTML5
    -   Tailwind CSS (via CDN)
    -   JavaScript (para interatividade, como o menu mobile)
    -   Font Awesome (ícones)
    -   Google Fonts (Montserrat e Inter)
-   **Ambiente de Desenvolvimento**:
    -   Qualquer editor de código (VS Code, Sublime Text, etc.)
    -   Um servidor web local para servir os arquivos estáticos.

## Como Executar o Projeto Localmente

O projeto agora é uma aplicação web baseada em Flask.

**Pré-requisitos:**
-   Ter o [Python](https://www.python.org/downloads/) instalado em sua máquina.

**Passos:**

1.  **Clone este repositório** para a sua máquina local.

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows, use `venv\Scripts\activate`
    # No MacOS/Linux, use `source venv/bin/activate`
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação Flask:**
    ```bash
    flask run
    ```

5.  **Abra seu navegador** e acesse a URL: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Estrutura dos Arquivos (Flask)

```
/
├── static/
│   └── imagens/          # Contém as imagens e a logo do projeto
├── templates/
│   ├── website.html      # Template da página inicial
│   ├── geoportal.html    # Template do Geoportal
│   └── ...               # Outros templates HTML
├── app.py                # Arquivo principal da aplicação Flask
├── requirements.txt      # Dependências do Python
├── vercel.json           # Configuração de deploy para a Vercel
├── .gitignore            # Arquivos a serem ignorados pelo Git
├── README.md             # Este arquivo
├── PRD.md                # Documento de Requisitos do Projeto
└── TASKS.md              # Lista de Tarefas
```

---

*Teste de sincronização para forçar novo deploy na Vercel.*

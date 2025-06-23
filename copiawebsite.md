<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programa Cerrado em Rede: A Conexão do Saber</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'cerrado-verde-profundo': '#316836',
                        'cerrado-azul-ceu-agua': '#0070C0',
                        'cerrado-amarelo-ipe': '#FFD400',
                        'cerrado-ocre-terra': '#C8A05A',
                        'institucional-cinza': '#666666',
                        'institucional-branco': '#FFFFFF',
                        'institucional-preto': '#000000',
                    },
                    fontFamily: {
                        'montserrat': ['Montserrat', 'sans-serif'],
                        'open-sans': ['Open Sans', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <!-- Google Fonts for Montserrat and Open Sans -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Open+Sans:wght@400;700&display=swap" rel="stylesheet">
    <style>
        /* Custom styles for smooth scrolling and general body font */
        html {
            scroll-behavior: smooth;
        }
        body {
            font-family: 'Open Sans', sans-serif;
            color: #333; /* Default text color */
        }
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Montserrat', sans-serif;
        }
        /* Style for the logo placeholder - replace with actual image */
        .logo-placeholder {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 50px; /* Adjust size as needed */
            height: 50px; /* Adjust size as needed */
            border-radius: 50%;
            background-color: #316836; /* cerrado-verde-profundo */
            color: #FFD400; /* cerrado-amarelo-ipe */
            font-weight: bold;
            font-family: 'Montserrat', sans-serif;
            font-size: 1.25rem;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .network-pattern {
            background-image: radial-gradient(#666666 1px, transparent 1px);
            background-size: 20px 20px;
            opacity: 0.1;
        }
        .image-placeholder {
            background-color: #e0e0e0;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #666;
            text-align: center;
            font-style: italic;
            height: 300px; /* Default height */
            width: 100%;
            border-radius: 0.75rem; /* rounded-xl */
        }
    </style>
</head>
<body class="bg-institucional-branco">

    <!-- Header Section -->
    <header class="bg-cerrado-verde-profundo shadow-lg py-4 fixed w-full z-50">
        <div class="container mx-auto px-6 flex justify-between items-center">
            <!-- Logo - Replace with actual logo image -->
            <a href="#" class="flex items-center space-x-3">
                <div class="logo-placeholder">C</div>
                <span class="text-institucional-branco font-montserrat font-bold text-xl md:text-2xl">Cerrado em Rede</span>
            </a>

            <!-- Mobile Menu Button -->
            <button id="mobile-menu-button" class="md:hidden text-institucional-branco focus:outline-none">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>

            <!-- Navigation Links -->
            <nav id="main-navigation" class="hidden md:flex space-x-8">
                <a href="#home" class="text-institucional-branco hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">Início</a>
                <a href="#sobre" class="text-institucional-branco hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">Sobre</a>
                <a href="#cerrado" class="text-institucional-branco hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">O Cerrado</a>
                <a href="#pesquisa" class="text-institucional-branco hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">Pesquisa</a>
                <a href="#educacao" class="text-institucional-branco hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">Educação</a>
                <a href="#parceiros" class="text-institucional-branco hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">Parceiros</a>
                <a href="#noticias" class="text-institucional-branco hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">Notícias</a>
                <a href="#contato" class="text-institucional-branco hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">Contato</a>
            </nav>
        </div>
        <!-- Mobile Navigation Menu (hidden by default) -->
        <nav id="mobile-menu" class="md:hidden bg-cerrado-verde-profundo mt-4 px-6 pb-4 hidden">
            <a href="#home" class="block text-institucional-branco py-2 hover:bg-cerrado-azul-ceu-agua rounded-md transition duration-300 font-open-sans">Início</a>
            <a href="#sobre" class="block text-institucional-branco py-2 hover:bg-cerrado-azul-ceu-agua rounded-md transition duration-300 font-open-sans">Sobre o Programa</a>
            <a href="#cerrado" class="block text-institucional-branco py-2 hover:bg-cerrado-azul-ceu-agua rounded-md transition duration-300 font-open-sans">O Cerrado</a>
            <a href="#pesquisa" class="block text-institucional-branco py-2 hover:bg-cerrado-azul-ceu-agua rounded-md transition duration-300 font-open-sans">Pesquisa e Conhecimento</a>
            <a href="#educacao" class="block text-institucional-branco py-2 hover:bg-cerrado-azul-ceu-agua rounded-md transition duration-300 font-open-sans">Educação e Formação</a>
            <a href="#parceiros" class="block text-institucional-branco py-2 hover:bg-cerrado-azul-ceu-agua rounded-md transition duration-300 font-open-sans">Parceiros</a>
            <a href="#noticias" class="block text-institucional-branco py-2 hover:bg-cerrado-azul-ceu-agua rounded-md transition duration-300 font-open-sans">Notícias e Eventos</a>
            <a href="#contato" class="block text-institucional-branco py-2 hover:bg-cerrado-azul-ceu-agua rounded-md transition duration-300 font-open-sans">Contato</a>
        </nav>
    </header>

    <main class="pt-20"> <!-- Padding top to account for fixed header -->

        <!-- Hero Section -->
        <section id="home" class="relative bg-gradient-to-br from-cerrado-verde-profundo to-cerrado-azul-ceu-agua text-institucional-branco py-20 md:py-32 flex items-center justify-center min-h-screen">
            <div class="absolute inset-0 network-pattern"></div>
            <div class="container mx-auto px-6 text-center z-10">
                <h1 class="text-4xl md:text-6xl font-montserrat font-bold leading-tight mb-6 animate-fade-in">
                    Programa de Educação Ambiental e Formação Profissional
                    <br class="hidden md:block"> voltado para o Desenvolvimento Sustentável no Bioma do Cerrado
                </h1>
                <p class="text-xl md:text-2xl font-open-sans mb-8 animate-fade-in delay-200">
                    "Conhecimento que Transforma, Futuro que Floresce no Cerrado."
                </p>
                <a href="#sobre" class="inline-block bg-cerrado-amarelo-ipe text-institucional-preto font-montserrat font-bold py-3 px-8 rounded-full shadow-lg hover:bg-yellow-400 transform hover:scale-105 transition duration-300 animate-slide-up delay-400">
                    Saiba Mais Sobre Nós
                </a>
            </div>
        </section>

        <!-- About Section -->
        <section id="sobre" class="bg-institucional-branco py-16 md:py-24">
            <div class="container mx-auto px-6">
                <h2 class="text-3xl md:text-4xl font-montserrat font-bold text-cerrado-verde-profundo text-center mb-12">
                    Sobre o Programa
                </h2>
                <div class="grid md:grid-cols-2 gap-12 items-center">
                    <div>
                        <p class="text-lg font-open-sans mb-6 text-institucional-cinza leading-relaxed">
                            O Programa de Educação Ambiental e Formação Profissional voltado para o Desenvolvimento Sustentável no bioma do Cerrado é uma iniciativa fundamental para a pesquisa, disseminação do conhecimento e capacitação em prol da sustentabilidade em um dos biomas mais ricos e ameaçados do Brasil. Nosso trabalho está enraizado na convicção de que o desenvolvimento sustentável do Cerrado passa necessariamente pela educação ambiental e pela formação de profissionais engajados e conscientes.
                        </p>
                        <h3 class="text-2xl font-montserrat font-bold text-cerrado-azul-ceu-agua mb-4">Missão</h3>
                        <p class="text-lg font-open-sans mb-6 text-institucional-cinza leading-relaxed">
                            Promover a educação ambiental e a formação profissional qualificada, gerando e disseminando conhecimento científico e prático para o desenvolvimento sustentável do bioma do Cerrado, fomentando a conservação, a valorização da sociobiodiversidade e o uso responsável dos recursos naturais.
                        </p>
                        <h3 class="text-2xl font-montserrat font-bold text-cerrado-azul-ceu-agua mb-4">Visão</h3>
                        <p class="text-lg font-open-sans mb-6 text-institucional-cinza leading-relaxed">
                            Ser reconhecido como um programa de referência nacional e internacional na construção de soluções inovadoras e sustentáveis para os desafios do Cerrado, consolidando uma rede de conhecimento e atuação em defesa e valorização do bioma.
                        </p>
                    </div>
                    <div class="image-placeholder rounded-xl overflow-hidden shadow-xl">
                        [Imagem da equipe ou de atividades do programa]
                        <img src="https://placehold.co/600x400/C8A05A/FFFFFF?text=Equipe+e+Ações+do+Programa" alt="Equipe e Ações do Programa" class="w-full h-auto object-cover">
                    </div>
                </div>
            </div>
        </section>

        <!-- Values Section (part of About) -->
        <section class="bg-gray-50 py-16 md:py-24">
            <div class="container mx-auto px-6">
                <h3 class="text-3xl md:text-4xl font-montserrat font-bold text-cerrado-verde-profundo text-center mb-12">Nossos Valores</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <!-- Value Card 1 -->
                    <div class="bg-institucional-branco p-8 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-200">
                        <h4 class="text-2xl font-montserrat font-bold text-cerrado-azul-ceu-agua mb-4">Sustentabilidade</h4>
                        <p class="text-lg font-open-sans text-institucional-cinza leading-relaxed">Compromisso inabalável com o equilíbrio ambiental, social e econômico, visando a perenidade dos ecossistemas e da vida.</p>
                    </div>
                    <!-- Value Card 2 -->
                    <div class="bg-institucional-branco p-8 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-200">
                        <h4 class="text-2xl font-montserrat font-bold text-cerrado-azul-ceu-agua mb-4">Inovação</h4>
                        <p class="text-lg font-open-sans text-institucional-cinza leading-relaxed">Busca contínua por novas abordagens, tecnologias e soluções criativas para os complexos desafios do Cerrado.</p>
                    </div>
                    <!-- Value Card 3 -->
                    <div class="bg-institucional-branco p-8 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-200">
                        <h4 class="text-2xl font-montserrat font-bold text-cerrado-azul-ceu-agua mb-4">Colaboração</h4>
                        <p class="text-lg font-open-sans text-institucional-cinza leading-relaxed">Fomento à construção de redes de conhecimento e parcerias estratégicas, valorizando a multidisciplinaridade e a troca de saberes.</p>
                    </div>
                    <!-- Value Card 4 -->
                    <div class="bg-institucional-branco p-8 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-200">
                        <h4 class="text-2xl font-montserrat font-bold text-cerrado-azul-ceu-agua mb-4">Transparência</h4>
                        <p class="text-lg font-open-sans text-institucional-cinza leading-relaxed">Atuação ética, clara e responsável em todas as ações, com prestação de contas e comunicação aberta.</p>
                    </div>
                    <!-- Value Card 5 -->
                    <div class="bg-institucional-branco p-8 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-200">
                        <h4 class="text-2xl font-montserrat font-bold text-cerrado-azul-ceu-agua mb-4">Respeito</h4>
                        <p class="text-lg font-open-sans text-institucional-cinza leading-relaxed">Valorização profunda da diversidade cultural e biológica do Cerrado e de suas comunidades tradicionais.</p>
                    </div>
                    <!-- Value Card 6 -->
                    <div class="bg-institucional-branco p-8 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-200">
                        <h4 class="text-2xl font-montserrat font-bold text-cerrado-azul-ceu-agua mb-4">Excelência</h4>
                        <p class="text-lg font-open-sans text-institucional-cinza leading-relaxed">Busca pela qualidade e rigor científico em todas as atividades, garantindo a relevância e o impacto do trabalho.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- O Cerrado Section -->
        <section id="cerrado" class="bg-cerrado-ocre-terra py-16 md:py-24">
            <div class="container mx-auto px-6">
                <h2 class="text-3xl md:text-4xl font-montserrat font-bold text-institucional-branco text-center mb-12">
                    O Bioma do Cerrado
                </h2>
                <div class="grid md:grid-cols-2 gap-12 items-center">
                    <div class="image-placeholder rounded-xl overflow-hidden shadow-xl">
                        [Imagem do bioma Cerrado]
                        <img src="https://placehold.co/600x400/316836/FFFFFF?text=Paisagem+do+Cerrado" alt="Paisagem do Bioma Cerrado" class="w-full h-auto object-cover">
                    </div>
                    <div>
                        <p class="text-lg font-open-sans mb-6 text-institucional-branco leading-relaxed">
                            O Cerrado, conhecido como a savana mais rica em biodiversidade do mundo, é um bioma de extrema importância para o Brasil e para o planeta, atuando como "berço das águas" e abrigando uma vasta sociobiodiversidade.
                        </p>
                        <p class="text-lg font-open-sans text-institucional-branco leading-relaxed">
                            No entanto, enfrenta grandes pressões devido ao avanço da fronteira agrícola, queimadas e outras atividades humanas. O Programa surge como uma resposta estratégica a esses desafios, promovendo o conhecimento e a capacitação para um desenvolvimento que integre conservação e progresso. Nosso foco é o Cerrado Brasileiro, suas particularidades ecológicas e culturais, e a urgência de sua preservação.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Research and Knowledge Section -->
        <section id="pesquisa" class="bg-institucional-branco py-16 md:py-24">
            <div class="container mx-auto px-6">
                <h2 class="text-3xl md:text-4xl font-montserrat font-bold text-cerrado-verde-profundo text-center mb-12">
                    Pesquisa e Conhecimento
                </h2>
                <div class="grid md:grid-cols-2 gap-12 items-start">
                    <div>
                        <p class="text-lg font-open-sans mb-6 text-institucional-cinza leading-relaxed">
                            Promovemos a geração e disseminação de conhecimento científico e prático, através de pesquisas inovadoras e projetos que abordam os desafios e oportunidades do Cerrado. Nossa equipe de pesquisadores está engajada em diversas frentes, desde a ecologia da paisagem até as soluções socioeconômicas sustentáveis.
                        </p>
                        <ul class="list-disc list-inside space-y-2 text-lg font-open-sans text-institucional-cinza">
                            <li>Publicações e Artigos Científicos</li>
                            <li>Projetos em Andamento e Resultados</li>
                            <li>Banco de Dados e Informações do Bioma</li>
                            <li>Workshops e Seminários de Pesquisa</li>
                        </ul>
                        <a href="#" class="mt-8 inline-block bg-cerrado-azul-ceu-agua text-institucional-branco font-montserrat font-bold py-3 px-8 rounded-full shadow-lg hover:bg-blue-700 transition duration-300">
                            Ver Publicações
                        </a>
                    </div>
                    <div class="image-placeholder rounded-xl overflow-hidden shadow-xl">
                        [Imagem de laboratório ou pesquisa em campo]
                        <img src="https://placehold.co/600x400/0070C0/FFFFFF?text=Pesquisa+e+Conhecimento" alt="Pesquisa e Conhecimento" class="w-full h-auto object-cover">
                    </div>
                </div>
            </div>
        </section>

        <!-- Education and Training Section -->
        <section id="educacao" class="bg-cerrado-verde-profundo py-16 md:py-24">
            <div class="container mx-auto px-6">
                <h2 class="text-3xl md:text-4xl font-montserrat font-bold text-institucional-branco text-center mb-12">
                    Educação e Formação
                </h2>
                <div class="grid md:grid-cols-2 gap-12 items-start">
                    <div class="image-placeholder rounded-xl overflow-hidden shadow-xl">
                        [Imagem de sala de aula ou workshop]
                        <img src="https://placehold.co/600x400/316836/FFFFFF?text=Educação+e+Formação" alt="Educação e Formação" class="w-full h-auto object-cover">
                    </div>
                    <div>
                        <p class="text-lg font-open-sans mb-6 text-institucional-branco leading-relaxed">
                            Oferecemos uma variedade de cursos e programas de formação profissional voltados para a sustentabilidade no Cerrado. Nossos materiais didáticos são desenvolvidos para capacitar indivíduos e comunidades, promovendo a conscientização e a aplicação de práticas sustentáveis.
                        </p>
                        <ul class="list-disc list-inside space-y-2 text-lg font-open-sans text-institucional-branco">
                            <li>Cursos e Workshops Presenciais e Online</li>
                            <li>Materiais Didáticos e E-books</li>
                            <li>Programas de Capacitação para Comunidades</li>
                            <li>Certificados de Participação</li>
                        </ul>
                        <a href="#" class="mt-8 inline-block bg-cerrado-amarelo-ipe text-institucional-preto font-montserrat font-bold py-3 px-8 rounded-full shadow-lg hover:bg-yellow-400 transition duration-300">
                            Conheça Nossos Cursos
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Partners Section -->
        <section id="parceiros" class="bg-institucional-branco py-16 md:py-24">
            <div class="container mx-auto px-6 text-center">
                <h2 class="text-3xl md:text-4xl font-montserrat font-bold text-cerrado-verde-profundo mb-12">
                    Nossos Parceiros
                </h2>
                <p class="text-lg font-open-sans mb-10 text-institucional-cinza leading-relaxed max-w-3xl mx-auto">
                    Agradecemos a colaboração e o apoio das instituições que tornam o Programa de Educação Ambiental e Formação Profissional uma realidade. Juntos, fortalecemos a rede de conhecimento e atuação em prol do Cerrado.
                </p>
                <div class="flex flex-wrap justify-center items-center gap-8 md:gap-16">
                    <!-- Partner Logo 1 -->
                    <div class="image-placeholder w-32 h-20 md:w-48 md:h-32 rounded-lg p-2 shadow-md">
                        [Logo UnB FT]
                        <img src="https://placehold.co/150x80/666666/FFFFFF?text=Logo+UnB+FT" alt="Logo UnB FT" class="max-w-full max-h-full object-contain">
                    </div>
                    <!-- Partner Logo 2 -->
                    <div class="image-placeholder w-32 h-20 md:w-48 md:h-32 rounded-lg p-2 shadow-md">
                        [Logo UFG Hub do Conhecimento]
                        <img src="https://placehold.co/150x80/666666/FFFFFF?text=Logo+UFG+Hub" alt="Logo UFG Hub do Conhecimento" class="max-w-full max-h-full object-contain">
                    </div>
                    <!-- Partner Logo 3 -->
                    <div class="image-placeholder w-32 h-20 md:w-48 md:h-32 rounded-lg p-2 shadow-md">
                        [Logo Prospecta]
                        <img src="https://placehold.co/150x80/666666/FFFFFF?text=Logo+Prospecta" alt="Logo Prospecta Escritório de Ligação da FT" class="max-w-full max-h-full object-contain">
                    </div>
                </div>
            </div>
        </section>

        <!-- News and Events Section -->
        <section id="noticias" class="bg-gray-50 py-16 md:py-24">
            <div class="container mx-auto px-6">
                <h2 class="text-3xl md:text-4xl font-montserrat font-bold text-cerrado-verde-profundo text-center mb-12">
                    Notícias e Eventos
                </h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <!-- News Card 1 -->
                    <div class="bg-institucional-branco rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 overflow-hidden">
                        <div class="image-placeholder h-48">
                            [Imagem da Notícia 1]
                            <img src="https://placehold.co/400x200/FFD400/316836?text=Notícia+1" alt="Imagem da Notícia 1" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-xl font-montserrat font-bold text-cerrado-azul-ceu-agua mb-2">Novo Projeto de Restauração do Cerrado Lançado</h3>
                            <p class="text-sm text-institucional-cinza mb-4">20 de Junho, 2025</p>
                            <p class="text-base font-open-sans text-institucional-cinza leading-relaxed mb-4">
                                Iniciativa ambiciosa visa recuperar áreas degradadas e promover a biodiversidade.
                            </p>
                            <a href="#" class="text-cerrado-azul-ceu-agua hover:text-cerrado-verde-profundo font-montserrat font-bold text-sm">Leia Mais &rarr;</a>
                        </div>
                    </div>
                    <!-- News Card 2 -->
                    <div class="bg-institucional-branco rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 overflow-hidden">
                        <div class="image-placeholder h-48">
                            [Imagem da Notícia 2]
                            <img src="https://placehold.co/400x200/0070C0/FFFFFF?text=Evento+2" alt="Imagem do Evento 2" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-xl font-montserrat font-bold text-cerrado-azul-ceu-agua mb-2">Inscrições Abertas para Workshop de Bioconstrução</h3>
                            <p class="text-sm text-institucional-cinza mb-4">15 de Junho, 2025</p>
                            <p class="text-base font-open-sans text-institucional-cinza leading-relaxed mb-4">
                                Aprenda técnicas sustentáveis de construção com foco no bioma local.
                            </p>
                            <a href="#" class="text-cerrado-azul-ceu-agua hover:text-cerrado-verde-profundo font-montserrat font-bold text-sm">Inscreva-se &rarr;</a>
                        </div>
                    </div>
                    <!-- News Card 3 -->
                    <div class="bg-institucional-branco rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 overflow-hidden">
                        <div class="image-placeholder h-48">
                            [Imagem da Notícia 3]
                            <img src="https://placehold.co/400x200/316836/FFD400?text=Publicação+3" alt="Imagem da Notícia 3" class="w-full h-full object-cover">
                        </div>
                        <div class="p-6">
                            <h3 class="text-xl font-montserrat font-bold text-cerrado-azul-ceu-agua mb-2">Novo Artigo: O Papel das Comunidades no Cerrado</h3>
                            <p class="text-sm text-institucional-cinza mb-4">10 de Junho, 2025</p>
                            <p class="text-base font-open-sans text-institucional-cinza leading-relaxed mb-4">
                                Análise aprofundada sobre a importância das comunidades tradicionais na conservação.
                            </p>
                            <a href="#" class="text-cerrado-azul-ceu-agua hover:text-cerrado-verde-profundo font-montserrat font-bold text-sm">Baixe o Artigo &rarr;</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contato" class="bg-cerrado-azul-ceu-agua py-16 md:py-24">
            <div class="container mx-auto px-6 text-center">
                <h2 class="text-3xl md:text-4xl font-montserrat font-bold text-institucional-branco mb-12">
                    Entre em Contato
                </h2>
                <p class="text-lg font-open-sans mb-10 text-institucional-branco leading-relaxed max-w-3xl mx-auto">
                    Tem alguma dúvida, sugestão ou deseja colaborar? Preencha o formulário abaixo ou entre em contato pelos nossos canais.
                </p>
                <div class="bg-institucional-branco p-8 md:p-12 rounded-xl shadow-xl max-w-lg mx-auto">
                    <form>
                        <div class="mb-6 text-left">
                            <label for="name" class="block text-institucional-cinza text-lg font-open-sans font-semibold mb-2">Nome Completo</label>
                            <input type="text" id="name" name="name" class="w-full px-5 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cerrado-amarelo-ipe font-open-sans" placeholder="Seu nome">
                        </div>
                        <div class="mb-6 text-left">
                            <label for="email" class="block text-institucional-cinza text-lg font-open-sans font-semibold mb-2">Seu E-mail</label>
                            <input type="email" id="email" name="email" class="w-full px-5 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cerrado-amarelo-ipe font-open-sans" placeholder="seu.email@exemplo.com">
                        </div>
                        <div class="mb-6 text-left">
                            <label for="message" class="block text-institucional-cinza text-lg font-open-sans font-semibold mb-2">Mensagem</label>
                            <textarea id="message" name="message" rows="6" class="w-full px-5 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cerrado-amarelo-ipe font-open-sans" placeholder="Escreva sua mensagem aqui..."></textarea>
                        </div>
                        <button type="submit" class="w-full bg-cerrado-amarelo-ipe text-institucional-preto font-montserrat font-bold py-3 px-8 rounded-full shadow-lg hover:bg-yellow-400 transition duration-300">
                            Enviar Mensagem
                        </button>
                    </form>
                </div>
            </div>
        </section>

    </main>

    <!-- Footer Section -->
    <footer class="bg-institucional-preto text-institucional-branco py-12">
        <div class="container mx-auto px-6 text-center">
            <div class="flex flex-col md:flex-row justify-between items-center mb-8">
                <div class="mb-6 md:mb-0">
                    <a href="#" class="flex items-center space-x-3 justify-center md:justify-start mb-2">
                        <div class="logo-placeholder logo-footer">C</div>
                        <span class="text-institucional-branco font-montserrat font-bold text-xl">Cerrado em Rede</span>
                    </a>
                    <p class="text-sm font-open-sans text-gray-400">
                        "Conhecimento que Transforma, Futuro que Floresce no Cerrado."
                    </p>
                </div>
                <nav class="flex flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-8 text-lg mb-6 md:mb-0">
                    <a href="#home" class="text-gray-300 hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">Início</a>
                    <a href="#sobre" class="text-gray-300 hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">Sobre</a>
                    <a href="#pesquisa" class="text-gray-300 hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">Pesquisa</a>
                    <a href="#educacao" class="text-gray-300 hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">Educação</a>
                    <a href="#contato" class="text-gray-300 hover:text-cerrado-amarelo-ipe transition duration-300 font-open-sans">Contato</a>
                </nav>
                <div class="flex space-x-4">
                    <!-- Social Media Icons (placeholders) -->
                    <a href="#" class="text-gray-300 hover:text-cerrado-amarelo-ipe transition duration-300">
                        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.779 1.674 4.931 4.931.058 1.265.07 1.645.07 4.85s-.012 3.584-.07 4.85c-.148 3.252-1.674 4.779-4.931 4.931-1.265.058-1.645.07-4.85.07s-3.584-.012-4.85-.07c-3.252-.148-4.779-1.674-4.931-4.931-.058-1.265-.07-1.645-.07-4.85s.012-3.584.07-4.85c.148-3.252 1.674-4.779 4.931-4.931 1.265-.058 1.645-.07 4.85-.07zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948s.014 3.668.072 4.948c.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.073 4.948.073s3.668-.014 4.948-.072c4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948s-.014-3.667-.072-4.947c-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.689-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.162 6.162 6.162 6.162-2.759 6.162-6.162-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4s1.791-4 4-4 4 1.79 4 4-1.791 4-4 4zm6.406-11.845c-.796 0-1.44-.643-1.44-1.439s.643-1.44 1.44-1.44 1.44.643 1.44 1.44-.643 1.439-1.44 1.439z"/></svg>
                    </a>
                    <a href="#" class="text-gray-300 hover:text-cerrado-amarelo-ipe transition duration-300">
                        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm6.993 6.079c-.742-.484-1.798-.79-2.887-.935l.006-.002c-1.077-.146-2.18-.216-3.279-.216h-1.666c-.33 0-.6-.27-.6-.6v-2.4c0-.33.27-.6.6-.6h1.5c.33 0 .6-.27.6-.6s-.27-.6-.6-.6h-1.5c-1.93 0-3.5 1.57-3.5 3.5v2.5c0 .33-.27.6-.6.6h-.5c-1.758 0-3.328.784-4.417 2.054-.336.398-.246.969.191 1.258.438.289.967.147 1.298-.291.802-.808 1.884-1.254 3.018-1.254h.5c.33 0 .6.27.6.6v7.35c0 .33.27.6.6.6h3.4c.33 0 .6-.27.6-.6v-7.35c0-.33-.27-.6-.6-.6h-.5c1.134 0 2.216-.446 3.018-1.254.331-.438.86-.58 1.298-.291.437.289.527.86.191 1.258-1.089 1.27-2.659 2.054-4.417 2.054h-.5c-.33 0-.6.27-.6.6v2.4c0 .33.27.6.6.6h1.5c.33 0 .6-.27.6-.6v-2.4c0-.33-.27-.6-.6-.6h-1.666c1.099 0 2.202-.07 3.279-.216l-.006-.002c1.089-.145 2.145-.451 2.887-.935.438-.289.527-.86.191-1.258-.336-.398-.865-.54-1.298-.291zm-2.493 2.621l-.004-.002z"/></svg>
                    </a>
                </div>
            </div>
            <div class="border-t border-gray-700 pt-8 text-sm text-gray-400">
                <p>&copy; 2025 Programa Cerrado em Rede. Todos os direitos reservados.</p>
                <p class="mt-2">Desenvolvido por Prof. Cláudio Henrique Feitosa e Breno Peixoto Cortez</p>
            </div>
        </div>
    </footer>

    <!-- JavaScript for Mobile Menu Toggle -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');
            const navLinks = document.querySelectorAll('#main-navigation a, #mobile-menu a');

            mobileMenuButton.addEventListener('click', function() {
                mobileMenu.classList.toggle('hidden');
            });

            // Close mobile menu when a link is clicked
            mobileMenu.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', () => {
                    mobileMenu.classList.add('hidden');
                });
            });

            // Smooth scrolling for navigation links
            navLinks.forEach(link => {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    const targetId = this.getAttribute('href').substring(1);
                    const targetElement = document.getElementById(targetId);
                    if (targetElement) {
                        const headerOffset = document.querySelector('header').offsetHeight;
                        const elementPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;
                        const offsetPosition = elementPosition - headerOffset;

                        window.scrollTo({
                            top: offsetPosition,
                            behavior: "smooth"
                        });
                    }
                });
            });
        });
    </script>
</body>
</html>

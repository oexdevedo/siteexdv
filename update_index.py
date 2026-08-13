import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = """<!-- =============================================
     HERO FULLSCREEN (100vh, vídeo de fundo)
     ============================================= -->
<section class="stack-section stack-hero hero-fullscreen" id="hero-section">
    <video class="hero-video-bg" autoplay muted loop playsinline>
        <source src="img/cena.mp4" type="video/mp4">
    </video>
    <div class="hero-overlay"></div>
    <div class="hero-fullscreen-inner container">
        <div class="hero-text-col">
            <h1 class="hero-title" style="text-transform: none; font-size: 3.2rem; line-height: 1.1;">Transformando a relação das pessoas com o dinheiro.</h1>
            <p class="hero-subtitle">
                Um ecossistema que une tecnologia, educação financeira e acompanhamento humano para ajudar pessoas e empresas a conquistarem uma vida financeira mais saudável.
            </p>
            <div class="hero-fullscreen-actions">
                <a href="#intro" class="btn btn-hero-primary">Conheça o Ecossistema <i data-lucide="arrow-right"></i></a>
            </div>
        </div>
    </div>
</section>

<!-- =============================================
     CONTEÚDO PRINCIPAL (abaixo da hero)
     ============================================= -->
<div class="stack-section stack-section--white" id="stack-info">
<main class="container">

    <!-- INTRODUÇÃO -->
    <section class="section" id="intro" style="padding-top: 4rem; padding-bottom: 4rem; text-align: center; max-width: 800px; margin: 0 auto;">
        <h2 style="font-family: 'Lato'; font-size: 2.5rem; color: var(--brand-navy); margin-bottom: 1.5rem;">Você não precisa enfrentar sua vida financeira sozinho.</h2>
        <p style="font-size: 1.2rem; color: var(--text-secondary); margin-bottom: 1.5rem; line-height: 1.6;">
            No Ex Devedor acreditamos que organização financeira vai muito além de planilhas ou renegociação de dívidas.
        </p>
        <p style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 1.5rem; line-height: 1.6;">
            Criamos um ecossistema que combina inteligência artificial, educação financeira comportamental, mentorias e treinamentos para transformar hábitos e gerar resultados duradouros.
        </p>
        <p style="font-size: 1.3rem; font-weight: 700; color: var(--accent-orange);">
            Porque sair das dívidas é importante.<br>Mas permanecer organizado é o que muda vidas.
        </p>
    </section>

    <!-- NOSSO ECOSSISTEMA -->
    <section class="section" id="ecossistema" style="padding-top: 2rem; border-top: 1px solid var(--border-light);">
        <div style="text-align: center; margin-bottom: 4rem;">
            <span class="image-card-badge" style="background-color: var(--brand-navy); margin-bottom: 1rem; display: inline-block;">NOSSO ECOSSISTEMA</span>
            <h2 style="font-family: 'Lato'; font-size: 2rem; margin-bottom: 1rem;">Soluções conectadas para cada momento da sua jornada financeira.</h2>
            <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
                Não importa se você está começando a organizar suas finanças, deseja alcançar um objetivo ou busca levar educação financeira para sua empresa. Temos uma solução para cada etapa.
            </p>
        </div>

        <div class="packages-grid" style="grid-template-columns: repeat(2, 1fr); gap: 2rem;">
            
            <!-- Tutu -->
            <div class="package-image-card" style="padding: 2rem; background-color: var(--bg-panel); border-radius: 12px; border: 1px solid var(--border-light);">
                <h3 style="font-size: 1.8rem; color: var(--brand-navy); margin-bottom: 0.5rem;">Tutu</h3>
                <h4 style="color: var(--accent-orange); margin-bottom: 1.5rem;">Seu assistente financeiro inteligente.</h4>
                <p style="margin-bottom: 1rem; font-size: 0.95rem;">O Tutu transforma o WhatsApp em um assistente financeiro que acompanha sua rotina. Você registra receitas e despesas por áudio, texto ou foto e recebe uma visão clara da sua vida financeira.</p>
                <p style="margin-bottom: 1.5rem; font-size: 0.95rem;">Enquanto você conversa, o Tutu organiza suas informações, acompanha suas metas e utiliza inteligência artificial para oferecer análises e sugestões personalizadas.</p>
                
                <h5 style="font-weight: 700; margin-bottom: 0.5rem;">O que você encontra:</h5>
                <ul style="list-style: none; padding: 0; margin-bottom: 1.5rem; font-size: 0.9rem;">
                    <li><i data-lucide="check-circle" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Organização pelo WhatsApp</li>
                    <li><i data-lucide="check-circle" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Controle de receitas e despesas</li>
                    <li><i data-lucide="check-circle" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Limite diário inteligente e Metas</li>
                    <li><i data-lucide="check-circle" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Gestão de dívidas e Diário financeiro</li>
                    <li><i data-lucide="check-circle" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Planejador com IA e Relatórios</li>
                    <li><i data-lucide="check-circle" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Conta Compartilhada e Acompanhamento</li>
                </ul>
                <p style="font-weight: 700; font-style: italic; color: var(--brand-navy);">Porque controlar dinheiro precisa ser simples.</p>
            </div>

            <!-- Escola Ex Devedor -->
            <div class="package-image-card" style="padding: 2rem; background-color: var(--bg-panel); border-radius: 12px; border: 1px solid var(--border-light);">
                <h3 style="font-size: 1.8rem; color: var(--brand-navy); margin-bottom: 0.5rem;">Escola Ex Devedor</h3>
                <h4 style="color: var(--accent-orange); margin-bottom: 1.5rem;">Aprenda a cuidar do seu dinheiro para a vida toda.</h4>
                <p style="margin-bottom: 1.5rem; font-size: 0.95rem;">Nossa escola reúne cursos, oficinas e conteúdos práticos para desenvolver uma relação mais saudável com o dinheiro. Aqui você aprende a transformar conhecimento em comportamento.</p>
                
                <h5 style="font-weight: 700; margin-bottom: 0.5rem;">Trilhas de aprendizado:</h5>
                <ul style="list-style: none; padding: 0; font-size: 0.9rem;">
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="book-open" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Planejamento Financeiro</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="book-open" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Organização Financeira</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="book-open" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Educação Financeira Comportamental</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="book-open" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Negociação de Dívidas</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="book-open" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Construção de Patrimônio</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="book-open" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Uso Inteligente da Inteligência Artificial nas Finanças</li>
                </ul>
            </div>

            <!-- Mentorias -->
            <div class="package-image-card" style="padding: 2rem; background-color: var(--bg-panel); border-radius: 12px; border: 1px solid var(--border-light);">
                <h3 style="font-size: 1.8rem; color: var(--brand-navy); margin-bottom: 0.5rem;">Mentorias</h3>
                <h4 style="color: var(--accent-orange); margin-bottom: 1.5rem;">Cada realidade financeira merece um plano diferente.</h4>
                <p style="margin-bottom: 1.5rem; font-size: 0.95rem;">Nossas mentorias unem estratégia, acompanhamento e tecnologia para acelerar sua evolução financeira. Durante os encontros você recebe orientação prática.</p>
                
                <h5 style="font-weight: 700; margin-bottom: 0.5rem;">Orientação prática para:</h5>
                <ul style="list-style: none; padding: 0; font-size: 0.9rem;">
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="target" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Organizar sua vida financeira</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="target" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Criar um plano de ação</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="target" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Negociar dívidas</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="target" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Construir reserva financeira</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="target" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Definir metas e desenvolver novos hábitos</li>
                </ul>
                <p style="font-weight: 700; margin-top: 1rem; font-size: 0.9rem;">Disponíveis nas modalidades individual e em grupo.</p>
            </div>

            <!-- Empresas -->
            <div class="package-image-card" style="padding: 2rem; background-color: var(--brand-navy); color: white; border-radius: 12px;">
                <h3 style="font-size: 1.8rem; color: white; margin-bottom: 0.5rem;">Empresas</h3>
                <h4 style="color: var(--accent-orange); margin-bottom: 1.5rem;">Transforme a saúde financeira dos seus colaboradores.</h4>
                <p style="margin-bottom: 1.5rem; color: rgba(255,255,255,0.9); font-size: 0.95rem;">Funcionários financeiramente saudáveis vivem com menos estresse, tomam melhores decisões e produzem mais. Desenvolvemos programas completos de educação financeira corporativa.</p>
                
                <h5 style="font-weight: 700; margin-bottom: 0.5rem; color: white;">Nossas soluções corporativas:</h5>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; font-size: 0.85rem; color: rgba(255,255,255,0.9);">
                    <div><i data-lucide="briefcase" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Diagnóstico Financeiro</div>
                    <div><i data-lucide="briefcase" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Palestras e Workshops</div>
                    <div><i data-lucide="briefcase" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Treinamentos</div>
                    <div><i data-lucide="briefcase" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Licenciamento do Tutu</div>
                    <div><i data-lucide="briefcase" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Programas de acompanhamento</div>
                    <div><i data-lucide="briefcase" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Mentorias e Trilhas</div>
                    <div><i data-lucide="briefcase" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Indicadores de impacto</div>
                    <div><i data-lucide="briefcase" size="14" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Projetos personalizados</div>
                </div>
            </div>

            <!-- Palestras -->
            <div class="package-image-card" style="padding: 2rem; background-color: var(--bg-panel); border-radius: 12px; border: 1px solid var(--border-light);">
                <h3 style="font-size: 1.8rem; color: var(--brand-navy); margin-bottom: 0.5rem;">Palestras</h3>
                <h4 style="color: var(--accent-orange); margin-bottom: 1.5rem;">Educação financeira que inspira mudanças.</h4>
                <p style="margin-bottom: 1.5rem; font-size: 0.95rem;">Levamos conteúdos práticos para empresas, escolas, universidades, eventos e instituições públicas. Mais do que palestras, entregamos experiências capazes de mudar a forma como as pessoas enxergam o dinheiro.</p>
                
                <h5 style="font-weight: 700; margin-bottom: 0.5rem;">Temas:</h5>
                <ul style="list-style: none; padding: 0; font-size: 0.9rem;">
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="mic" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Dinheiro e comportamento</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="mic" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Como sair das dívidas</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="mic" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Planejamento financeiro</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="mic" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Saúde financeira</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="mic" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Inteligência Artificial aplicada às finanças</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="mic" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Produtividade financeira</li>
                    <li style="margin-bottom: 0.5rem;"><i data-lucide="mic" size="14" style="color: var(--brand-navy); margin-right: 0.5rem;"></i> Educação financeira para empresas</li>
                </ul>
            </div>

            <!-- Impacto Social -->
            <div class="package-image-card" style="padding: 2rem; background-color: var(--accent-orange); color: white; border-radius: 12px;">
                <h3 style="font-size: 1.8rem; color: white; margin-bottom: 0.5rem;">Impacto Social</h3>
                <h4 style="color: var(--brand-navy); margin-bottom: 1.5rem;">Transformar vidas é o nosso maior resultado.</h4>
                <p style="margin-bottom: 1.5rem; color: white; font-size: 0.95rem;">Acreditamos que educação financeira precisa ser acessível. Por isso desenvolvemos projetos sociais, ações educativas e iniciativas voltadas para comunidades, mulheres, jovens, escolas e organizações públicas.</p>
                <p style="font-weight: 700; font-size: 1.05rem; color: var(--brand-navy);">Nosso propósito é democratizar o acesso à educação financeira utilizando tecnologia e inovação.</p>
            </div>

        </div>
    </section>

    <!-- NOSSO MÉTODO E PARA QUEM É -->
    <section class="section" id="metodo-publico" style="padding-top: 4rem; padding-bottom: 4rem;">
        <div class="info-section">
            
            <!-- NOSSO MÉTODO -->
            <div class="info-text-col">
                <span class="image-card-badge" style="background-color: var(--bg-panel); margin-bottom: 1rem;">NOSSO MÉTODO</span>
                <h2 style="font-family: 'Lato';">Quatro pilares para uma transformação duradoura.</h2>
                
                <div style="margin-top: 2.5rem;">
                    <div style="margin-bottom: 1.5rem;">
                        <h4 style="color: var(--accent-orange); font-size: 1.2rem; display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;"><i data-lucide="layers"></i> Organização</h4>
                        <p style="margin-left: 2rem;">Entenda exatamente para onde seu dinheiro está indo.</p>
                    </div>
                    <div style="margin-bottom: 1.5rem;">
                        <h4 style="color: var(--accent-orange); font-size: 1.2rem; display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;"><i data-lucide="map"></i> Planejamento</h4>
                        <p style="margin-left: 2rem;">Construa um caminho claro para seus objetivos.</p>
                    </div>
                    <div style="margin-bottom: 1.5rem;">
                        <h4 style="color: var(--accent-orange); font-size: 1.2rem; display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;"><i data-lucide="activity"></i> Comportamento</h4>
                        <p style="margin-left: 2rem;">Transforme pequenas atitudes em grandes resultados.</p>
                    </div>
                    <div style="margin-bottom: 1.5rem;">
                        <h4 style="color: var(--accent-orange); font-size: 1.2rem; display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.25rem;"><i data-lucide="users"></i> Acompanhamento</h4>
                        <p style="margin-left: 2rem;">Conte com tecnologia e especialistas durante toda a jornada.</p>
                    </div>
                </div>
            </div>

            <!-- PARA QUEM É -->
            <div class="cards-col">
                <span class="image-card-badge" style="background-color: var(--bg-panel); margin-bottom: 1rem;">PARA QUEM É</span>
                
                <div class="stacked-card">
                    <div class="stacked-card-icon" style="background-color: rgba(6, 26, 53, 0.05); color: var(--brand-navy);"><i data-lucide="user"></i></div>
                    <div class="stacked-card-content">
                        <h3>Pessoas</h3>
                        <p>Organize sua vida financeira. Saia das dívidas. Construa patrimônio.</p>
                    </div>
                </div>
                
                <div class="stacked-card">
                    <div class="stacked-card-icon" style="background-color: rgba(223, 168, 63, 0.1); color: var(--accent-orange);"><i data-lucide="home"></i></div>
                    <div class="stacked-card-content">
                        <h3>Famílias</h3>
                        <p>Planejem objetivos juntos. Compartilhem responsabilidades. Criem hábitos saudáveis.</p>
                    </div>
                </div>

                <div class="stacked-card">
                    <div class="stacked-card-icon" style="background-color: rgba(6, 26, 53, 0.05); color: var(--brand-navy);"><i data-lucide="briefcase"></i></div>
                    <div class="stacked-card-content">
                        <h3>Empresas</h3>
                        <p>Invistam no bem-estar financeiro dos colaboradores.</p>
                    </div>
                </div>

                <div class="stacked-card">
                    <div class="stacked-card-icon" style="background-color: rgba(223, 168, 63, 0.1); color: var(--accent-orange);"><i data-lucide="building"></i></div>
                    <div class="stacked-card-content">
                        <h3>Instituições</h3>
                        <p>Projetos de educação financeira para escolas, universidades, órgãos públicos e comunidades.</p>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- DIFERENCIAL E RESULTADOS -->
    <section class="section" id="diferencial" style="border-top: 1px solid var(--border-light); padding-top: 4rem; padding-bottom: 2rem;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem;">
            
            <div style="display: flex; flex-direction: column; justify-content: center;">
                <div>
                    <span class="image-card-badge" style="background-color: var(--bg-panel); margin-bottom: 1rem;">DIFERENCIAL</span>
                    <h2 style="font-family: 'Lato'; margin-bottom: 1rem;">Tecnologia com propósito.</h2>
                </div>
                <p style="margin-bottom: 1rem; font-size: 1.05rem;">Enquanto outras soluções apenas mostram números, o Ex Devedor ajuda você a desenvolver hábitos que tornam esses números melhores.</p>
                <p style="margin-bottom: 1rem; font-size: 1.05rem;">Nossa tecnologia trabalha junto com especialistas para transformar conhecimento em ação.</p>
                <blockquote style="border-left: 4px solid var(--accent-orange); padding-left: 1.5rem; margin: 1.5rem 0; font-style: italic; font-weight: 700; color: var(--brand-navy); font-size: 1.1rem;">
                    Porque educação financeira não acontece em uma planilha. Ela acontece todos os dias.
                </blockquote>
            </div>

            <div style="background-color: var(--brand-navy); color: white; padding: 3rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(6,26,53,0.1);">
                <span class="image-card-badge" style="background-color: var(--accent-orange); color: white; margin-bottom: 1rem;">RESULTADOS</span>
                <h2 style="font-family: 'Lato'; color: white; margin-bottom: 1.5rem;">Muito além do controle financeiro.</h2>
                <ul style="list-style: none; padding: 0; font-size: 1.1rem; line-height: 1.8;">
                    <li><i data-lucide="arrow-right" size="16" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Mais organização.</li>
                    <li><i data-lucide="arrow-right" size="16" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Mais tranquilidade.</li>
                    <li><i data-lucide="arrow-right" size="16" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Mais clareza para tomar decisões.</li>
                    <li><i data-lucide="arrow-right" size="16" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Mais autonomia.</li>
                    <li><i data-lucide="arrow-right" size="16" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Mais qualidade de vida.</li>
                    <li><i data-lucide="arrow-right" size="16" style="color: var(--accent-orange); margin-right: 0.5rem;"></i> Mais liberdade financeira.</li>
                </ul>
            </div>

        </div>
    </section>

    <!-- FINAL BRANDING -->
    <section class="section" style="text-align: center; padding-top: 4rem; padding-bottom: 5rem;">
        <h2 style="font-size: 3rem; color: var(--brand-navy); margin-bottom: 0.5rem; font-family: 'Lato'; font-weight: 900;">Ex Devedor</h2>
        <p style="font-size: 1.1rem; font-weight: 700; color: var(--accent-orange); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1.5rem;">
            Tecnologia. Educação. Comportamento. Transformação.
        </p>
        <p style="max-width: 600px; margin: 0 auto; color: var(--text-secondary); font-size: 1.1rem; line-height: 1.6;">
            Ajudamos pessoas e organizações a desenvolver uma relação mais saudável com o dinheiro por meio de inteligência artificial, educação financeira e acompanhamento especializado.
        </p>
    </section>

</main>
</div><!-- /.stack-section#stack-info -->"""

pattern = re.compile(r'<!-- =============================================\n     HERO FULLSCREEN.*?</div><!-- /\.stack-section#stack-info -->', re.DOTALL)
updated_content = pattern.sub(new_content, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)
print("Updated successfully")

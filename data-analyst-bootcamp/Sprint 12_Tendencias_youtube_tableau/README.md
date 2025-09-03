# 📊 Dashboard Interativo — Tendências do YouTube (Sprint 12 | TripleTen)

Este projeto foi desenvolvido como parte da **Sprint 12** do Bootcamp de Análise de Dados da [TripleTen](https://tripleten.com), sendo nosso **primeiro contato com o Tableau** — e já aprovado com sucesso ✅.

O objetivo foi criar um **dashboard interativo** para analisar tendências de vídeos no YouTube, permitindo explorar o comportamento das visualizações por categoria, data e região.

---

## 🎯 Objetivo do Projeto

- Explorar e visualizar dados de vídeos em alta no YouTube.
- Identificar padrões e tendências por categoria e região.
- Desenvolver habilidades no **Tableau Public** para criação de dashboards interativos.
- Aplicar boas práticas de design e storytelling visual.

---

## 🛠 Ferramentas e Tecnologias

- **Tableau Public** → criação e publicação do dashboard.
- **Excel / CSV** → organização e pré-tratamento dos dados.
- **Dataset:** informações sobre vídeos em alta no YouTube, contendo:
  - `trending_date` — data em que o vídeo entrou nos trends.
  - `category_title` — categoria do vídeo.
  - `videos_count` — número de vídeos por categoria.
  - `region` — país/região.
  - Outras métricas relacionadas às tendências.

---

## 📌 Estrutura do Dashboard

O dashboard foi organizado em três partes principais:

### 1️⃣ Histórico de Tendências (Valores Absolutos)
- **Gráfico:** Área empilhada.
- **Eixo X:** `trending_date` (contínuo, por dia).
- **Eixo Y:** Soma de `videos_count`.
- **Cor:** `category_title`.
- **Filtros globais:** `trending_date` e `region`.

**Insight:**  
Foi possível identificar picos de vídeos em determinadas categorias, com variação significativa em eventos sazonais e datas específicas.

---

### 2️⃣ Distribuição por Categoria
- **Gráfico:** Barras horizontais.
- **Métrica:** Soma de `videos_count`.
- **Filtro:** Aplicado por região e data.
  
**Insight:**  
Algumas categorias, como *Entertainment* e *Music*, dominaram o volume de vídeos em alta, mas com variações regionais marcantes.

---

### 3️⃣ Evolução por Região
- **Gráfico:** Linha.
- **Dimensão:** `region`.
- **Métrica:** `videos_count`.
  
**Insight:**  
Regiões específicas tiveram picos concentrados, sugerindo eventos locais ou lançamentos relevantes.

---

## 🔍 Principais Descobertas

- **Categoria dominante:** *Entertainment* liderou em quase todas as regiões.
- **Sazonalidade:** Datas próximas a feriados e grandes eventos apresentaram alta concentração de vídeos virais.
- **Regionalidade:** Algumas categorias são mais fortes em regiões específicas — por exemplo, *Music* teve maior destaque na América Latina.
- **Volume geral:** Houve tendência de crescimento constante na quantidade de vídeos em alta ao longo do período analisado.

---

## 🌐 Links de Acesso

- 📊 **Dashboard no Tableau Public:** [Acessar aqui](https://public.tableau.com/app/profile/seu-link-aquihttps://public.tableau.com/app/profile/gabriel.schmidel/viz/ProjetoSprint12-TendnciasYouTube-SterlingDraper/Painel1?publish=yes)
- 💻 **Repositório no GitHub:** *Você está aqui!*

---

## 📷 Prévia do Dashboard

![Preview do Dashboard](images/dashboard_preview.png)

---

## 📚 Aprendizados e Próximos Passos

- Primeiro contato com o **Tableau**: aprendemos a criar gráficos dinâmicos, configurar filtros globais e formatar eixos para melhor legibilidade.
- Aplicamos conceitos de **storytelling com dados**, deixando a navegação intuitiva.
- Próximo passo: integrar este dashboard com **dados atualizados automaticamente** a partir de um script em Python para análise contínua.

---

✍️ **Autor:** Gabriel Schmidel  
📅 **Data:** Agosto/2025




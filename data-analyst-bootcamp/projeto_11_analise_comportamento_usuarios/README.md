# Projeto 11 - Análise de Comportamento de Usuários e Teste A/A/B

## 📌 Objetivo

Analisar o comportamento de usuários dentro de um aplicativo de venda de alimentos, com foco em:

- Estudo do funil de eventos
- Análise de conversão por etapa
- Validação de experimento A/A/B para mudança de fonte no app

## 📊 Dados Utilizados

- **logs_exp_us.csv**: Contém registros de eventos de usuários no app, incluindo:
  - `EventName`: nome do evento (ação do usuário)
  - `DeviceIDHash`: identificador do usuário
  - `EventTimestamp`: data e hora do evento
  - `ExpId`: grupo experimental (246, 247 ou 248)

## 🔍 Etapas da Análise

### 1. Pré-processamento
- Conversão de datas e tipos
- Verificação de duplicatas e dados ausentes
- Criação de colunas auxiliares para data/hora

### 2. Exploração Inicial
- Contagem de eventos e usuários únicos
- Cálculo de eventos médios por usuário
- Determinação do intervalo confiável de dados (período de integridade)

### 3. Análise do Funil de Vendas
- Identificação das principais etapas: MainScreenAppear → OffersScreenAppear → CartScreenAppear → PaymentScreenSuccessful
- Cálculo das taxas de conversão entre etapas
- Identificação dos maiores pontos de evasão

### 4. Análise do Teste A/A/B
- Verificação de homogeneidade entre os grupos de controle (246 e 247)
- Testes de hipótese por evento entre os grupos:
  - Controle A1 x A2
  - Teste (248) x Controle
- Uso de proporções e testes estatísticos (Z-test para proporções)

## 📈 Conclusão Geral do Projeto

### Conclusões:

- A divisão dos grupos de controle (A/A) foi válida e não apresentou diferenças estatísticas significativas.
- O grupo de teste com nova fonte não apresentou melhora estatística consistente na taxa de conversão.
- O evento mais popular foi `MainScreenAppear`, seguido por `OffersScreenAppear`.
- A maior evasão acontece entre `CartScreenAppear` e `PaymentScreenSuccessful`.
- A análise sugere que a mudança de fonte **não impacta negativamente** a experiência, mas **também não gera melhoria significativa**.

## 💡 Recomendações
# Insights práticos e recomendações baseadas nos dados
# Recomendações e Conselhos para a Empresa

- A alteração visual (fonte) pode ser mantida, mas não como uma ação estratégica prioritária.
- Foco em melhorar a etapa entre carrinho e pagamento (alto abandono).
- Implementar experimentos futuros com base nos dados obtidos sobre conversão.

- **Identificação dos pontos críticos no funil:** Observamos que as maiores perdas de usuários ocorrem entre as etapas _OffersScreenAppear_ e _CartScreenAppear_. Isso indica que muitos usuários visualizam as ofertas, mas não avançam para o carrinho, sugerindo possíveis dificuldades na navegação ou falta de interesse nas ofertas apresentadas.

- **Melhorar a experiência nas telas críticas:** Recomendamos simplificar o processo de adicionar itens ao carrinho e destacar benefícios pode ajudar a reduzir a queda.

- **Avaliação do teste A/A/B das fontes:** Os testes indicaram que não há diferenças estatisticamente significativas entre os grupos de controle e o grupo com fontes alteradas. Isso sugere que a mudança de fontes não impacta negativamente o comportamento dos usuários, podendo ser adotada sem riscos.

- **Próximos passos:**  
  - Continuar monitorando o funil de vendas para validar melhorias implementadas.  
  - Testar outras variações no design e funcionalidades que possam incentivar a finalização da compra.  
  - Considerar a segmentação dos usuários para entender diferentes comportamentos e personalizar a experiência.  
  - Avaliar a coleta de feedback direto dos usuários nas etapas críticas para compreender melhor suas dificuldades.


---

**Status:** ✅ Concluído  


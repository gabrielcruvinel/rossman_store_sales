# Rossman Store Sales
Esse problema foi retirado da competição da Rossman Store, disponivel
no link: https://www.kaggle.com/c/rossmann-store-sales

# Contexto do problema
 A rossman é uma empresa de farmacias que possui mais de 3.000 unidades espalhadas
em 7 paises europeus. Atualmente, os gerentes da rossman possuem a tarefa de realizar uma previsão
de vendas diarias de suas respectivas lojas nas proximas 6 semanas.
As vendas das lojas são influenciadas por vários fatores, incluindo promoções, competidores, feriados,
temporadas e localização. Devido a quantidade de gerentes, as previsões de cada circunstancias podem váriar.

### Questão de négocio ( objetivo )
Qual o valor de vendas de cada loja nas proximas 6 semanas ? 

### Formato da solução
É um problema de vendas

### 1 - Como foi a estratégia utilizada para definição do problema ?
 1. Realizar o download dos dados
 2. Manipulação dos tipos de dados e preenchimento de dados faltantes
 3. Análise exploratoria dos dados
 4. Feature Engineering
 5. Preparação dos dados - Feature transformation
 6. Separo o conjunto de treino em:
  - Dados do treino :95.09%
  - Dados de teste: 4.90%
 7. Feature Selection
 8. Definição da Baseline com os algoritmos escolhidos (Random Forest Regressor, Averange Model, Linear Regression, Linear Regression - lasso, XGBoost Regressor)
 9. Comparação de performance da baseline utilizando validação cruzada
 10. Analise das performances dos algoritmos
 11. Criado grid para teste de hiperparametros utilizando Random Search
 12. Com os melhores hiperparametros, treinar o modelo de teste
 13. Avaliar o resultado final

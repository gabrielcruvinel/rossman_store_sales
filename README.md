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

# 1 - Como foi a estratégia utilizada para definição do problema ?
 1. Realizar o download dos dados
 2. Manipulação dos tipos de dados e preenchimento de dados faltantes
 3. Análise exploratoria dos dados
 4. Feature Engineering
 5. Preparação dos dados - Feature transformation
 6. Separo o conjunto de treino em:
  - Dados do treino :95.09%
  - Dados de teste: 4.90% ( Duas Semanas anteriores a ultima data)
 7. Feature Selection
 8. Definição da Baseline com os algoritmos escolhidos (Random Forest Regressor, Averange Model, Linear Regression, Linear Regression - lasso, XGBoost Regressor)
 9. Comparação de performance da baseline utilizando validação cruzada
 10. Analise das performances dos algoritmos
 11. Criado grid para teste de hiperparametros utilizando Random Search
 12. Com os melhores hiperparametros, treinar o modelo de teste utilizando XGBoost
 13. Avaliar o resultado final
 
 #2 - Qual foi o critério utilizado na seleção do Modelo Final?
  O modelo que obteve a melhor performance entre entre os resultados da baseline, utilizando os hiperparametros, utilizando as 3 métricas avaliadas( MAE, MAPE, RMSE)
  
  #3 - Quais evidencias que mostram que o modelo treinado é bom
  Verificando o resultado final com o baseline, obtive uma melhora significativa nas métricas avaliadas. Separei apenas 5% do conjunto de treino para teste afim de simular
  uma situação proxima do real, com datas de vendas mais recentes.
  Resultados da baseline dos algoritmos treinados:
  
  Baseline:
  
  |Model Name   |      MAE     |  MAPE |  RMSE |
  |-------------|:------------:|:-----:| -----:|
  | Random Forest Regressor|  680.193831	 | 0.100006 |   1011.665881 |
  | col 2 is |    centered   |   $12 |   $12 |
  | col 3 is | right-aligned |    $1 |   $12 |
  | col 1 is |  left-aligned | $1600 |   $12 |
  | col 1 is |  left-aligned | $1600 |   $12 |

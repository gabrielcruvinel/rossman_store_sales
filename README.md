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

### Data fields
Most of the fields are self-explanatory. The following are descriptions for those that aren't.

Id - an Id that represents a (Store, Date) duple within the test set
Store - a unique Id for each store
Sales - the turnover for any given day (this is what you are predicting)
Customers - the number of customers on a given day
Open - an indicator for whether the store was open: 0 = closed, 1 = open
StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
SchoolHoliday - indicates if the (Store, Date) was affected by the closure of public schools
StoreType - differentiates between 4 different store models: a, b, c, d
Assortment - describes an assortment level: a = basic, b = extra, c = extended
CompetitionDistance - distance in meters to the nearest competitor store
CompetitionOpenSince[Month/Year] - gives the approximate year and month of the time the nearest competitor was opened
Promo - indicates whether a store is running a promo on that day
Promo2 - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
Promo2Since[Year/Week] - describes the year and calendar week when the store started participating in Promo2
PromoInterval - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store
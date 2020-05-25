https://www.investing.com/equities/StocksFilter?index_id=17920
iBovespa:
name, last_rs, high_rs, low_rs, chg, chg%, vol, time

Nasdaq:
https://www.investing.com/equities/StocksFilter?index_id=20
name, last_usd, high_usd, low_usd, chg, chg%, vol, time

Dolar em relação ao real:
https://investing.com/currencies/usd-brl
currency, value, change, perc, e timestamp

# As capturas (1, 2, 3) devem ser independentes e ocorrer a cada 2 min.

# Os arquivos das capturas (2 e 3) devem ser processados para conversão dos valores de Dólares(US$) para Reais (R$), resultando num arquivo, cujo nome contém o timestamp e com os seguintes campos: name, last_rs, high_rs, low_rs, last_usd, high_usd, low_usd, chg, chg_perc, vol, time.

# Os dados deverão ser inseridos em uma base de dados relacional, usando o SQLite. No código deverá constar a criação das bases de dados e a criação das tabelas.

# O código deverá estar encapsulado dentro de um Docker.

# O código deverá ser realizado em Python 3.
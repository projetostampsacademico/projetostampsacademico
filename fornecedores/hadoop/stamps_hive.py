#!./env/bin/python2.7
import pyhs2

medicamento='CALTREN 10 MG 30 CP S LIBBS'


with pyhs2.connect(host='192.168.56.101',
                   port=10000,
                   authMechanism="PLAIN",
                   user='hadoop',
                   password='mcosta',
                   database='fornecedores') as conn:
    with conn.cursor() as cur:
        # Execute query
        cur.execute( "select movimentacao.des_estado, movimentacao.des_cidade, movimentacao.medicamento, sum(quantidade) as quantidade \
                      from movimentacao where movimentacao.medicamento='"+ medicamento +"' \
                      GROUP BY movimentacao.des_estado, movimentacao.des_cidade, movimentacao.medicamento ")
        # Fetch table results
        for i in cur.fetch():
            print (i)
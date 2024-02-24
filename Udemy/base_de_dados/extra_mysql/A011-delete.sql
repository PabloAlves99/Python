-- Delete apaga registros da tabela
DELETE FROM users where id = 112;

-- Aviso: use SELECT para garantir que está
-- apagando os valores corretos
select * from users where id BETWEEN 110 and 112;
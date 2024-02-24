-- in seleciona elementos entre os valores enviados
select * from users
where id in (1,2,5,10,30,100,112,1212545)
and first_name in ('Pablo', 'Alves');
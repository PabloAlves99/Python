-- Update - Atualiza registros
update users set 
first_name = 'Pablo',
last_name = 'Alves'
where id between 10 and 12;

select * from users where id between 10 and 12;
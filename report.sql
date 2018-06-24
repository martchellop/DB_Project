-- Report 0

SELECT uni.*
	FROM universitaria uni
	INNER JOIN universitaria_espaco ue
		ON ue.data = uni.data AND ue.organizador = uni.organizador
	INNER JOIN espaco esp
		ON ue.espaco = esp.cep
	WHERE esp.categoria = 'chacara';


-- Report 1
-- É possivel fazer isso de duas formas, com duas consultas separadas como mostrado a baixo, ou com essa maluquice que eu criei, acho que essa ai da mais nota

-- SELECT avg(preco) as media from universitaria;
-- SELECT avg(preco) as media from casamento;

select tipo, avg(preco) as media from  ((select u.*, ft.tipo from universitaria u inner join festa_tipo ft on u.data = ft.data and u.organizador = ft.organizador) union (select c.data, c.organizador, c.preco, ft.tipo from casamento c inner join festa_tipo ft on c.data = ft.data and c.organizador = ft.organizador)) as z group by tipo;


-- Report 2

SELECT avg(preco) as media, stddev_samp(preco) as std
	FROM universitaria_espaco;

-- Report 3

SELECT avg(preco) as media
	FROM bilhete
	WHERE preco > 10;

-- Report 4
SELECT data, organizador, count(nome) as quantidade
	FROM lista_casamento
	GROUP BY data, organizador;

-- Report 5

SELECT distinct et.tipo, l.empresa
	FROM universitaria uni
	INNER JOIN universitaria_espaco ue
		ON ue.data = uni.data AND ue.organizador = uni.organizador
	INNER JOIN espaco esp
		ON ue.espaco = esp.cep
	INNER JOIN locacao l
		ON esp.empresa = l.empresa
	INNER JOIN empresa_tipo et
		ON l.empresa = et.CNPJ

UNION

SELECT distinct et.tipo, t.empresa
	FROM universitaria uni
	INNER JOIN aluga a
		ON uni.data = a.data and uni.organizador = a.organizador
	INNER JOIN transporte t
		ON a.empresa = t.empresa
	INNER JOIN empresa_tipo et
		ON t.empresa = et.CNPJ;

-- search_events
-- Não entendi pra que serve o nome do organizador, checar com o Brunao depois
-- mudar o WHERE para os parametros recebidos

-- universitaria

SELECT f.tipo, u.data, u.organizador, o.nome
	FROM universitaria u
	INNER JOIN festa_tipo f
		ON f.data = u.data AND f.organizador = u.organizador
	INNER JOIN organizador o
		ON o.cpf = f.organizador
	WHERE u.data BETWEEN '2015-06-23'::timestamp AND now()::timestamp
		AND u.organizador = '11111111111';

-- casamento
SELECT f.tipo, c.data, c.organizador, o.nome, c.conjuge1, c.conjuge2
	FROM casamento c
	INNER JOIN festa_tipo f
		ON f.data = c.data AND f.organizador = c.organizador
	INNER JOIN organizador o
		ON o.cpf = f.organizador
	WHERE c.data BETWEEN '2015-06-23'::timestamp AND now()::timestamp
		AND c.organizador = '11111111111';

-- ambos
-- e possivel fazer um where so, so que por razoes vistas em aula da AR, desse jeito eh mais rapido

SELECT f.tipo, u.data, u.organizador, o.nome
	FROM universitaria u
	INNER JOIN festa_tipo f
		ON f.data = u.data AND f.organizador = u.organizador
	INNER JOIN organizador o
		ON o.cpf = f.organizador
	WHERE u.data BETWEEN '2015-06-23'::timestamp AND now()::timestamp
		AND u.organizador = '11111111111'

UNION

SELECT f.tipo, c.data, c.organizador, o.nome
	FROM casamento c
	INNER JOIN festa_tipo f
		ON f.data = c.data AND f.organizador = c.organizador
	INNER JOIN organizador o
		ON o.cpf = f.organizador
	WHERE c.data BETWEEN '2015-06-23'::timestamp AND now()::timestamp
		AND c.organizador = '11111111111';


-- localization_service

-- insert
INSERT INTO espaco (CEP) VALUES ('99999999');

-- delete
DELETE FROM espaco WHERE CEP = '99999999';

-- update_localization_service
-- estou supondo que seja alterar ir na tabela universitaria_espaco e alterar o preco de todas as festas que tenham aquele CEP

UPDATE universitaria_espaco SET preco = 10 WHERE espaco = '78171828';

-- tickets_service

-- insert
INSERT INTO bilhete (data, organizador) VALUES ('2017-05-21'::timestamp, '11111111111');

-- delete
DELETE FROM bilhete WHERE data = '2017-05-21'::timestamp and organizador = '11111111111' and id = 7;

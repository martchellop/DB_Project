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

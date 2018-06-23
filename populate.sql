/* TOTAL OF 0 ERRORS WHILE BUILDING METADATA STRUCTURE. */
BEGIN TRANSACTION;
/* TABLE organizador */
/* NULL INSERTION FOR ATTRIBUTE telefone AT TABLE organizador */
INSERT INTO organizador ( CPF, nome, email, telefone )
	VALUES ( 'Saepe minus', 'Enrico Lopes', 'Ipsum consequatur praesentium doloremq', NULL );
/* NULL INSERTION FOR ATTRIBUTE email AT TABLE organizador */
INSERT INTO organizador ( CPF, nome, email, telefone )
	VALUES ( 'Aspernatur ', 'Dra. Ana Carolina Novaes', NULL, 'Nobis at ' );
INSERT INTO organizador ( CPF, nome, email, telefone )
	VALUES ( 'Voluptate m', 'Camila das Neves', 'Dolore suscipit quam expedi', 'Dicta sint d' );

/* TABLE festa_tipo */
INSERT INTO festa_tipo ( data, organizador, tipo )
	VALUES ( to_timestamp ('2018-11-26 10:48:37', 'YYYY-MM-DD HH24:MI:SS'), 'Quam accusa', 'Porro minus' );

/* TABLE universitaria */
INSERT INTO universitaria ( data, organizador, preco )
	VALUES ( to_timestamp ('2018-11-26 10:48:37', 'YYYY-MM-DD HH24:MI:SS'), 'Quam accusa', -27986 );

/* TABLE bilhete */
INSERT INTO bilhete ( data, organizador, id, preco, lote, vendido )
	VALUES ( to_timestamp ('2018-11-26 10:48:37', 'YYYY-MM-DD HH24:MI:SS'), 'Quam accusa', None, -13408, -28147, None );

/* TABLE casamento */
INSERT INTO casamento ( data, organizador, preco, conjuge1, conjuge2 )
	VALUES ( to_timestamp ('2012-03-05 23:24:48', 'YYYY-MM-DD HH24:MI:SS'), 'Voluptate m', -30035, 'Repudiandae minus unde occaecati', 'Autem unde ipsa. Veritatis ' );

/* TABLE cerimonialista */
/* NULL INSERTION FOR ATTRIBUTE linha_atuacao AT TABLE cerimonialista */
INSERT INTO cerimonialista ( nome, telefone, linha_atuacao )
	VALUES ( 'Dr. Ian Cardoso', 'Culpa quib', NULL );
/* NULL INSERTION FOR ATTRIBUTE telefone AT TABLE cerimonialista */
INSERT INTO cerimonialista ( nome, telefone, linha_atuacao )
	VALUES ( 'Srta. Agatha das Neves', NULL, 'Laborum et repelle' );
INSERT INTO cerimonialista ( nome, telefone, linha_atuacao )
	VALUES ( 'Vitor Hugo Novaes', 'At asperna', 'Illum laborios' );

/* TABLE casamento_cerimonialista */
INSERT INTO casamento_cerimonialista ( data, organizador, cerimonialista )
	VALUES ( to_timestamp ('2012-03-05 23:24:48', 'YYYY-MM-DD HH24:MI:SS'), 'Voluptate m', 'Vitor Hugo Novaes' );

/* TABLE empresa_tipo */
INSERT INTO empresa_tipo ( CNPJ, tipo )
	VALUES ( 'Sunt ea volupt', 'Explicabo maio' );

/* TABLE locacao */
INSERT INTO locacao ( empresa, telefone, email, endereco )
	VALUES ( 'Sunt ea volupt', 'Tempora exercit', 'Ratione doloribus a dolorum. Optio temp', 'Chácara de Alves, 817 Mangueiras 70805-649 Costela de Minas / RO' );

/* TABLE decoracao */
INSERT INTO decoracao ( empresa, telefone, email, endereco )
	VALUES ( 'Sunt ea volupt', 'Deleniti cor', 'Nulla iure reiciendis ad aliquid. Harum autem ', 'Setor de Silva, 56 Santa Sofia 78920219 Barbosa da Prata / PB' );

/* TABLE floricultura */
INSERT INTO floricultura ( empresa, telefone, email, endereco )
	VALUES ( 'Sunt ea volupt', 'Vero maiores ', 'Est cum perspiciatis veritatis eligendi quibusd', 'Avenida Vitória Araújo, 2 Alto Das Antenas 32152471 da Conceição de da Rosa / PR' );

/* TABLE transporte */
INSERT INTO transporte ( empresa, telefone, email, endereco )
	VALUES ( 'Sunt ea volupt', 'Voluptatem p', 'Explicabo ipsam laboriosam nihil. Sapiente', 'Núcleo Luiz Fernando Nogueira, 456 São Benedito 62125491 Duarte / AL' );

/* TABLE decor */
INSERT INTO decor ( tipo, cor, marca, empresa )
	VALUES ( 'Necessitat', 'Reiciendis distincti', 'Eos necessit', 'Sunt ea volupt' );

/* TABLE casamento_decoracao */
INSERT INTO casamento_decoracao ( data, organizador, empresa, preco )
	VALUES ( to_timestamp ('2012-03-05 23:24:48', 'YYYY-MM-DD HH24:MI:SS'), 'Voluptate m', 'Sunt ea volupt', -32053 );

/* TABLE flor */
INSERT INTO flor ( empresa, especie, cor )
	VALUES ( 'Sunt ea volupt', 'Ea quaerat animi', 'Temporibus n' );

/* TABLE casamento_floricultura */
INSERT INTO casamento_floricultura ( data, organizador, empresa, preco )
	VALUES ( to_timestamp ('2012-03-05 23:24:48', 'YYYY-MM-DD HH24:MI:SS'), 'Voluptate m', 'Sunt ea volupt', -943 );

/* TABLE veiculo_tipo */
INSERT INTO veiculo_tipo ( modelo, n_assentos )
	VALUES ( 'Ex vel ut quisq', 14506 );

/* TABLE transporte_veiculo */
INSERT INTO transporte_veiculo ( empresa, tipo )
	VALUES ( 'Sunt ea volupt', 'Quia ipsum qui qui' );

/* TABLE aluga */
INSERT INTO aluga ( data, organizador, empresa )
	VALUES ( to_timestamp ('2018-11-26 10:48:37', 'YYYY-MM-DD HH24:MI:SS'), 'Quam accusa', 'Sunt ea volupt' );

/* TABLE espaco */
/* NULL INSERTION FOR ATTRIBUTE capacidade AT TABLE espaco */
INSERT INTO espaco ( CEP, categoria, endereco, capacidade, empresa )
	VALUES ( 'Dolor in', 'Vitae molestias odio c', 'Trecho de da Rocha, 37 Conjunto Novo Dom Bosco 50843-212 Barros Grande / PR', NULL, 'Sunt ea volupt' );
/* NULL INSERTION FOR ATTRIBUTE endereco AT TABLE espaco */
INSERT INTO espaco ( CEP, categoria, endereco, capacidade, empresa )
	VALUES ( 'Cum quis', 'Id cum veniam.Accusan', NULL, 488193, 'Sunt ea volupt' );
/* NULL INSERTION FOR ATTRIBUTE categoria AT TABLE espaco */
INSERT INTO espaco ( CEP, categoria, endereco, capacidade, empresa )
	VALUES ( 'Suscipit', NULL, 'Conjunto Fogaça, 340 Distrito Industrial Do Jatoba 53513146 Pires Paulista / RN', 888049, 'Sunt ea volupt' );
INSERT INTO espaco ( CEP, categoria, endereco, capacidade, empresa )
	VALUES ( 'Est nemo', 'Ratione quis exercitati', 'Colônia Porto Confisco 27701523 da Rocha / PA', 754223, 'Sunt ea volupt' );

/* TABLE casamento_espaco */
INSERT INTO casamento_espaco ( data, organizador, espaco, preco )
	VALUES ( to_timestamp ('2012-03-05 23:24:48', 'YYYY-MM-DD HH24:MI:SS'), 'Voluptate m', 'Est nemo', 18670 );

/* TABLE universitaria_espaco */
INSERT INTO universitaria_espaco ( data, organizador, espaco, preco )
	VALUES ( to_timestamp ('2018-11-26 10:48:37', 'YYYY-MM-DD HH24:MI:SS'), 'Quam accusa', 'Est nemo', 1576 );

/* TABLE NUMBER TOTAL: 22 */
ROLLBACK;

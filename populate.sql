INSERT INTO organizador VALUES ('11111111111', 'Marcello Pagano', 'meuemail@gmail.com', '11 997965007');
INSERT INTO organizador VALUES ('22222222222', 'Gabriel Cruz', 'outroemaill@gmail.com', '11 999999999');
INSERT INTO organizador VALUES ('33333333333', 'Gabriel Cyrillo', 'eeeemall@gmail.com', '16 811818181');
INSERT INTO organizador VALUES ('55555555555', 'Bruno Gomes Coelho', 'emaildele@yaho.com.br', '16 123456789');

INSERT INTO festa_tipo VALUES (to_timestamp('2017-05-21', 'YYYY-MM-DD'), '11111111111', 'universitaria');
INSERT INTO festa_tipo VALUES (to_timestamp('2018-09-12', 'YYYY-MM-DD'), '11111111111', 'universitaria');
INSERT INTO festa_tipo VALUES (to_timestamp('2017-04-11', 'YYYY-MM-DD'), '22222222222', 'universitaria');
INSERT INTO festa_tipo VALUES (to_timestamp('2013-11-05', 'YYYY-MM-DD'), '55555555555', 'universitaria');

INSERT INTO universitaria VALUES (to_timestamp('2017-05-21', 'YYYY-MM-DD'), '11111111111', 50000);
INSERT INTO universitaria VALUES (to_timestamp('2018-09-12', 'YYYY-MM-DD'), '11111111111', 20000);
INSERT INTO universitaria VALUES (to_timestamp('2017-04-11', 'YYYY-MM-DD'), '22222222222', 200000);
INSERT INTO universitaria VALUES (to_timestamp('2013-11-05', 'YYYY-MM-DD'), '55555555555', 640);

INSERT INTO bilhete (data, organizador, preco, lote) VALUES (to_timestamp('2017-05-21', 'YYYY-MM-DD'), '11111111111', 30, 1);
INSERT INTO bilhete (data, organizador, preco, lote) VALUES (to_timestamp('2017-05-21', 'YYYY-MM-DD'), '11111111111', 20, 2);
INSERT INTO bilhete (data, organizador, preco, lote) VALUES (to_timestamp('2017-05-21', 'YYYY-MM-DD'), '11111111111', 30, 1);
INSERT INTO bilhete (data, organizador, preco, lote) VALUES (to_timestamp('2017-05-21', 'YYYY-MM-DD'), '11111111111', 30, 1);
INSERT INTO bilhete (data, organizador, preco, lote) VALUES (to_timestamp('2017-05-21', 'YYYY-MM-DD'), '11111111111', 30, 1);
INSERT INTO bilhete (data, organizador, preco, lote) VALUES (to_timestamp('2018-09-12', 'YYYY-MM-DD'), '11111111111', 25, 1);

INSERT INTO empresa_tipo VALUES ('11111111111111', 'transporte');
INSERT INTO empresa_tipo VALUES ('22222222222222', 'transporte');
INSERT INTO empresa_tipo VALUES ('33333333333333', 'transporte');
INSERT INTO empresa_tipo VALUES ('44444444444444', 'locacao');
INSERT INTO empresa_tipo VALUES ('77777777777777', 'locacao');
INSERT INTO empresa_tipo VALUES ('55555555555555', 'decoracao');
INSERT INTO empresa_tipo VALUES ('66666666666666', 'floricultura');

INSERT INTO locacao VALUES ('44444444444444', '11 998191', 'locmae@hotmail.com', 'rua sao carlos');
INSERT INTO locacao VALUES ('77777777777777', '0800 5050 7171', 'comp@bol.com.br', 'avenida paulista');

INSERT INTO transporte VALUES ('11111111111111', '21 717818731', 'mais_email_1000@yahoo.com', 'avenida botafogo');
INSERT INTO transporte VALUES ('22222222222222', '21 12698731', 'eeeeeeemail@yahoo.com.br', 'avenida tiradentes');

INSERT INTO veiculo_tipo VALUES ('ix35', 5);
INSERT INTO veiculo_tipo VALUES ('minivan', 10);

INSERT INTO transporte_veiculo VALUES ('11111111111111', 'ix35');
INSERT INTO transporte_veiculo VALUES ('11111111111111', 'minivan');

INSERT INTO aluga VALUES (to_timestamp('2017-04-11', 'YYYY-MM-DD'), '22222222222', '11111111111111');
INSERT INTO aluga VALUES (to_timestamp('2018-09-12', 'YYYY-MM-DD'), '11111111111', '22222222222222');

INSERT INTO espaco VALUES ('50505050', 'republica', 'endereco', 70, '44444444444444');
INSERT INTO espaco VALUES ('78171828', 'campo', 'outro endereco', 500, '44444444444444');

INSERT INTO universitaria_espaco VALUES (to_timestamp('2017-05-21', 'YYYY-MM-DD'), '11111111111', '78171828', 200);
INSERT INTO universitaria_espaco VALUES (to_timestamp('2013-11-05', 'YYYY-MM-DD'), '55555555555', '50505050', 200);



INSERT INTO casamento ( preco, data, organizador, conjuge2, conjuge1 )
	VALUES ( 6563, to_timestamp ('2035-02-11', 'YYYY-MM-DD'), '11111111111', 'Delectus eius doloribus veniam.', 'Reprehenderit debitis quos.' );

INSERT INTO casamento ( preco, data, organizador, conjuge2, conjuge1 )
	VALUES ( 5127, to_timestamp ('2038-01-13', 'YYYY-MM-DD'), '22222222222', 'Minima saepe quis.', 'Qui voluptates magnam totam.' );

INSERT INTO casamento ( preco, data, organizador, conjuge2, conjuge1 )
	VALUES ( 14377, to_timestamp ('2008-09-22', 'YYYY-MM-DD'), '33333333333', 'Ut adipisci temporibus.', 'Natus iusto enim fugiat ea.' );




INSERT INTO lista_casamento ( data, organizador, nome )
	VALUES ( to_timestamp ('2035-02-11', 'YYYY-MM-DD'), '11111111111', 'Kaique Caldeira' );

INSERT INTO lista_casamento ( data, organizador, nome )
	VALUES ( to_timestamp ('2035-02-11', 'YYYY-MM-DD'), '11111111111', 'Henrique Caldeira' );

INSERT INTO lista_casamento ( data, organizador, nome )
	VALUES ( to_timestamp ('2035-02-11', 'YYYY-MM-DD'), '11111111111', 'Maria Caldeira' );

INSERT INTO lista_casamento ( data, organizador, nome )
	VALUES ( to_timestamp ('2035-02-11', 'YYYY-MM-DD'), '11111111111', 'Frei Caldeira' );

INSERT INTO lista_casamento ( data, organizador, nome )
	VALUES ( to_timestamp ('2038-01-13', 'YYYY-MM-DD'), '22222222222', 'Laura Melo' );

INSERT INTO lista_casamento ( data, organizador, nome )
	VALUES ( to_timestamp ('2038-01-13', 'YYYY-MM-DD'), '22222222222', 'Rodrigues Melo' );

INSERT INTO lista_casamento ( data, organizador, nome )
	VALUES ( to_timestamp ('2038-01-13', 'YYYY-MM-DD'), '22222222222', 'Gabriel Melo' );

INSERT INTO lista_casamento ( data, organizador, nome )
	VALUES ( to_timestamp ('2038-01-13', 'YYYY-MM-DD'), '22222222222', 'Frei Melo' );

INSERT INTO lista_casamento ( data, organizador, nome )
	VALUES ( to_timestamp ('2008-09-22', 'YYYY-MM-DD'), '33333333333', 'Gustavo Henrique Alves' );

INSERT INTO lista_casamento ( data, organizador, nome )
	VALUES ( to_timestamp ('2008-09-22', 'YYYY-MM-DD'), '33333333333', 'Jair Henrique Alves' );

INSERT INTO lista_casamento ( data, organizador, nome )
	VALUES ( to_timestamp ('2008-09-22', 'YYYY-MM-DD'), '33333333333', 'Geremias Henrique Alves' );

INSERT INTO lista_casamento ( data, organizador, nome )
	VALUES ( to_timestamp ('2008-09-22', 'YYYY-MM-DD'), '33333333333', 'Gabriel Henrique Alves' );




INSERT INTO cerimonialista ( linha_atuacao, nome, telefone )
	VALUES ( 'Perferendis eaque.', 'Isaac Porto', NULL );

INSERT INTO cerimonialista ( linha_atuacao, nome, telefone )
	VALUES ( NULL, 'Yasmin Araújo', '+55 (041) 4091 ' );

INSERT INTO cerimonialista ( linha_atuacao, nome, telefone )
	VALUES ( 'Voluptatum.', 'João Lucas Cavalcanti', '(051) 8767 2709' );

INSERT INTO cerimonialista ( linha_atuacao, nome, telefone )
	VALUES ( 'Adipisci.', 'Alexia Rocha', '+55 (021) 6008 ' );

INSERT INTO cerimonialista ( linha_atuacao, nome, telefone )
	VALUES ( 'Nam sint iusto.', 'Eloah Martins', '11 9927 9885' );




INSERT INTO casamento_cerimonialista ( data, organizador, cerimonialista )
	VALUES ( to_timestamp ('2008-09-22', 'YYYY-MM-DD'), '33333333333', 'Eloah Martins' );

INSERT INTO casamento_cerimonialista ( data, organizador, cerimonialista )
	VALUES ( to_timestamp ('2038-01-13', 'YYYY-MM-DD'), '22222222222', 'João Lucas Cavalcanti' );

INSERT INTO casamento_cerimonialista ( data, organizador, cerimonialista )
	VALUES ( to_timestamp ('2035-02-11', 'YYYY-MM-DD'), '11111111111', 'Eloah Martins' );



INSERT INTO decoracao ( endereco, email, empresa, telefone )
	VALUES ( 'Largo Vieira, 33 Conjunto Lagoa 57846-681 Monteiro do Galho / SC', 'testando@mailinator.com', 'Repellat enim decor.', '+55 31 1862 633' );

INSERT INTO decoracao ( endereco, email, empresa, telefone )
	VALUES ( 'Alameda Costa, 380 São Geraldo 02865-500 Dias dos Dourados / MT', 'umaEmpresa@example.com', 'Rem decor', '5546 9756' );

INSERT INTO decoracao ( endereco, email, empresa, telefone )
	VALUES ( 'Jardim de Nogueira, 706 Zilah Sposito 68142907 Duarte / PE', 'talvezResponda@mailinator.com', 'Maiores saepe', '81 5227 3613' );



INSERT INTO floricultura ( endereco, email, empresa, telefone )
	VALUES ( 'Colônia Maria Sophia Castro, 84 São Vicente 72734614 Freitas do Galho / MA', 'remoFlores@foo.com', 'Rem.', '31 4883-8376' );

INSERT INTO floricultura ( endereco, email, empresa, telefone )
	VALUES ( 'Trevo Pietro Moreira, 480 Jardim Atlântico 31598-879 Pires / MA', 'repellatFloricultura@mailinator.com', 'Repellat enim flores', '+55 (041) 9981-' );

INSERT INTO floricultura ( endereco, email, empresa, telefone )
	VALUES ( 'Chácara Gonçalves, 75 Vila Madre Gertrudes 4ª Seção 56692-021 Costela do Norte / SC', 'foresMaiores@server.com', 'Maiores saepe flores', '+55 61 6474-052' );



INSERT INTO decor ( tipo, cor, empresa, marca )
	VALUES ( 'Sequi modi cumque', 'Amarelo', 'Repellat enim decor.', 'Ut natus.' );
INSERT INTO decor ( tipo, cor, empresa, marca )
	VALUES ( 'Possimus', 'Vermelho', 'Maiores saepe', 'Natus.' );
INSERT INTO decor ( tipo, cor, empresa, marca )
	VALUES ( 'Omnis est', 'Verde', 'Rem decor', 'Eius nostrum.' );



INSERT INTO casamento_decoracao ( preco, data, empresa, organizador )
	VALUES ( 6110, to_timestamp ('2008-09-22', 'YYYY-MM-DD'), 'Maiores saepe', '33333333333' );
INSERT INTO casamento_decoracao ( preco, data, empresa, organizador )
	VALUES ( 20435, to_timestamp ('2035-02-11', 'YYYY-MM-DD'), 'Rem decor', '22222222222' );
INSERT INTO casamento_decoracao ( preco, data, empresa, organizador )
	VALUES ( 8425, to_timestamp ('2038-01-13', 'YYYY-MM-DD'), 'Repellat enim decor.', '11111111111' );



INSERT INTO flor ( especie, empresa, cor )
	VALUES ( 'Tempora.', 'Maiores saepe', 'Violeta' );
INSERT INTO flor ( especie, empresa, cor )
	VALUES ( 'Sed', 'Rem decor', 'Aqua' );
INSERT INTO flor ( especie, empresa, cor )
	VALUES ( 'Nihil', 'Repellat enim decor.', 'Magenta' );



INSERT INTO casamento_floricultura ( preco, data, empresa, organizador )
	VALUES ( 1836, to_timestamp ('2038-01-13', 'YYYY-MM-DD'), 'Maiores saepe.', '11111111111' );
INSERT INTO casamento_floricultura ( preco, data, empresa, organizador )
	VALUES ( 6283, to_timestamp ('2038-01-13', 'YYYY-MM-DD'), 'Repellat enim.', '11111111111' );
INSERT INTO casamento_floricultura ( preco, data, empresa, organizador )
	VALUES ( 27087, to_timestamp ('2008-09-22', 'YYYY-MM-DD'), 'Maiores saepe.', '33333333333' );



INSERT INTO casamento_espaco ( espaco, data, organizador, preco )
	VALUES ( '50505050', to_timestamp ('2008-09-22', 'YYYY-MM-DD'), '33333333333', 4392 );
INSERT INTO casamento_espaco ( espaco, data, organizador, preco )
	VALUES ( '50505050', to_timestamp ('2038-01-13', 'YYYY-MM-DD'), '11111111111', 8056 );
INSERT INTO casamento_espaco ( espaco, data, organizador, preco )
	VALUES ( '78171828', to_timestamp ('2035-02-11', 'YYYY-MM-DD'), '22222222222', 7472 );



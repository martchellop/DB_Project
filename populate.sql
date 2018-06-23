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

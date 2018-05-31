CREATE TABLE organizador (
	CPF char(11),
	nome varchar(50) NOT NULL,
	email varchar(50),
	telefone varchar(15),
	CONSTRAINT pk_organizador PRIMARY KEY (CPF)
);

CREATE TABLE festa_tipo (
	data timestamp,
	organizador char(11),
	tipo varchar(21) NOT NULL,
	CONSTRAINT pk_festa_tipo PRIMARY KEY (data, organizador)
);

CREATE TABLE universitaria (
	data timestamp,
	organizador char(11),
	preco smallint NOT NULL,
	CONSTRAINT pk_universitaria PRIMARY KEY (data, organizador),
	CONSTRAINT fk_universitaria_org FOREIGN KEY (organizador)
		REFERENCES organizador(CPF),
	CONSTRAINT fk_universitaria_fes FOREIGN KEY (data, organizador)
		REFERENCES festa_tipo(data, organizador)
);

CREATE TABLE casamento (
	data timestamp,
	organizador char(11),
	preco smallint NOT NULL,
	conjuge1 varchar(50) NOT NULL,
	conjuge2 varchar(50) NOT NULL,
	CONSTRAINT pk_casamento PRIMARY KEY (data, organizador),
	CONSTRAINT fk_casamento FOREIGN KEY (organizador)
		REFERENCES organizador(CPF)
);

INSERT INTO organizador(cpf, nome) values ("11122233344", "oi");
INSERT INTO organizador(cpf, nome) values ("11122233388", "ta");
INSERT INTO organizador(cpf, nome) values ("11122233311", "ok");


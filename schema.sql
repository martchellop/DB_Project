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

CREATE TABLE bilhete (
	data timestamp,
	organizador char(11),
	id serial,
	preco smallint,
	lote smallint,
	vendido bool DEFAULT FALSE,
	CONSTRAINT pk_bilhete PRIMARY KEY (data, organizador, id),
	CONSTRAINT fk_bilhete FOREIGN KEY (data, organizador)
		REFERENCES universitaria(data, organizador)
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

CREATE TABLE cerimonialista (
	nome varchar(50),
	telefone varchar(15),
	linha_atuacao varchar(20),
	CONSTRAINT pk_cerimonialista PRIMARY KEY (nome)
);

CREATE TABLE casamento_cerimonialista (
	data timestamp,
	organizador char(11),
	cerimonialista varchar(50),
	CONSTRAINT pk_casamento_cerimonialista PRIMARY KEY (data, organizador),
	CONSTRAINT fk_casamento_cerimonialista_casa FOREIGN KEY (data, organizador)
		REFERENCES casamento(data, organizador),
	CONSTRAINT fk_casamento_cerimonialista_ceri FOREIGN KEY (cerimonialista)
		REFERENCES cerimonialista(nome)
);

CREATE TABLE empresa_tipo (
	CNPJ char(14),
	tipo varchar(20) NOT NULL,
	CONSTRAINT pk_empresa_tipo PRIMARY KEY (CNPJ)
);

CREATE TABLE locacao (
	empresa char(14),
	telefone varchar(15),
	email varchar(50),
	endereco varchar(150),
	CONSTRAINT pk_locacao PRIMARY KEY (empresa),
	CONSTRAINT fk_locacao FOREIGN KEY (empresa) REFERENCES empresa_tipo(CNPJ)
);

CREATE TABLE decoracao (
	empresa char(14),
	telefone varchar(15),
	email varchar(50),
	endereco varchar(150),
	CONSTRAINT pk_decoracao PRIMARY KEY (empresa),
	CONSTRAINT fk_decoracao FOREIGN KEY (empresa) REFERENCES empresa_tipo(CNPJ)
);

CREATE TABLE floricultura (
	empresa char(14),
	telefone varchar(15),
	email varchar(50),
	endereco varchar(150),
	CONSTRAINT pk_floricultura PRIMARY KEY (empresa),
	CONSTRAINT fk_floricultura FOREIGN KEY (empresa)
		REFERENCES empresa_tipo(CNPJ)
);

CREATE TABLE transporte (
	empresa char(14),
	telefone varchar(15),
	email varchar(50),
	endereco varchar(150),
	CONSTRAINT pk_transporte PRIMARY KEY (empresa),
	CONSTRAINT fk_transporte FOREIGN KEY (empresa) REFERENCES empresa_tipo(CNPJ)
);

CREATE TABLE decor (
	tipo varchar(20),
	cor varchar(20),
	marca varchar(20),
	empresa char(14),
	CONSTRAINT pk_decor PRIMARY KEY (tipo, cor, marca),
	CONSTRAINT fk_decor FOREIGN KEY (empresa) REFERENCES decoracao(empresa)
);

CREATE TABLE casamento_decoracao (
	data timestamp,
	organizador char(11),
	empresa char(14),
	preco smallint NOT NULL,
	CONSTRAINT pk_casamento_decoracao PRIMARY KEY (data, organizador, empresa),
	CONSTRAINT fk_casamento_decoracao_casa FOREIGN KEY (data, organizador)
		REFERENCES casamento(data, organizador),
	CONSTRAINT fk_casamento_decoracao_deco FOREIGN KEY (empresa)
		REFERENCES decoracao(empresa)
);

CREATE TABLE flor(
	empresa char(14),
	especie varchar(20),
	cor varchar(20),
	CONSTRAINT pk_flor PRIMARY KEY (empresa, especie, cor),
	CONSTRAINT fk_flor FOREIGN KEY (empresa) REFERENCES floricultura(empresa)
);

CREATE TABLE casamento_floricultura (
	data timestamp,
	organizador char(11),
	empresa char(14),
	preco smallint NOT NULL,
	CONSTRAINT pk_casamento_floricultura PRIMARY KEY
		(data, organizador, empresa),
	CONSTRAINT fk_casamento_floricultura_casa FOREIGN KEY (data, organizador)
		REFERENCES casamento(data, organizador),
	CONSTRAINT fk_casamento_floricultura_flor FOREIGN KEY (empresa)
		REFERENCES floricultura(empresa)

);

CREATE TABLE veiculo_tipo (
	modelo varchar(20),
	n_assentos smallint NOT NULL,
	CONSTRAINT pk_veiculo_tipo PRIMARY KEY (modelo)
);

CREATE TABLE transporte_veiculo (
	empresa char(14),
	tipo varchar(20),
	CONSTRAINT pk_transporte_veiculo PRIMARY KEY (empresa, tipo),
	CONSTRAINT fk_transporte_veiculo_trans FOREIGN KEY (empresa)
		REFERENCES transporte(empresa)
);

CREATE TABLE aluga (
	data timestamp,
	organizador char(11),
	empresa char(14),
	CONSTRAINT pk_aluga PRIMARY KEY (data, organizador, empresa),
	CONSTRAINT fk_aluga_univ FOREIGN KEY (data, organizador)
		REFERENCES universitaria(data, organizador),
	CONSTRAINT fk_aluga_trans FOREIGN KEY (empresa)
		REFERENCES transporte(empresa)
);


CREATE TABLE organizador (
	CPF char(11) NOT NULL,
	nome varchar(50) NOT NULL,
	email varchar(50),
	telefone varchar(15),
	CONSTRAINT pk_organizador PRIMARY KEY (CPF)
);

CREATE TABLE festa_tipo (
	data timestamp NOT NULL,
	organizador char(11) NOT NULL,
	tipo varchar(21) NOT NULL,
	CONSTRAINT pk_festa_tipo PRIMARY KEY (data, organizador),
	CONSTRAINT fk_organizador FOREIGN KEY (organizador)
		REFERENCES organizador(CPF)
        ON DELETE CASCADE
);

CREATE TABLE universitaria (
	data timestamp NOT NULL,
	organizador char(11) NOT NULL,
	preco int,
	CONSTRAINT pk_universitaria PRIMARY KEY (data, organizador),
	CONSTRAINT fk_universitaria_fes FOREIGN KEY (data, organizador)
		REFERENCES festa_tipo(data, organizador)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE bilhete (
	data timestamp NOT NULL,
	organizador char(11) NOT NULL,
	id serial NOT NULL,
	preco smallint,
	lote smallint,
	vendido bool DEFAULT FALSE,
	CONSTRAINT pk_bilhete PRIMARY KEY (data, organizador, id),
	CONSTRAINT fk_bilhete FOREIGN KEY (data, organizador)
		REFERENCES universitaria(data, organizador)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE casamento (
	data timestamp NOT NULL,
	organizador char(11) NOT NULL,
	preco smallint NOT NULL,
	conjuge1 varchar(50) NOT NULL,
	conjuge2 varchar(50) NOT NULL,
	CONSTRAINT pk_casamento PRIMARY KEY (data, organizador),
	CONSTRAINT fk_casamento_fes FOREIGN KEY (data, organizador)
		REFERENCES festa_tipo(data, organizador)
        ON DELETE CASCADE

);

CREATE TABLE lista_casamento (
	data timestamp NOT NULL,
	organizador char(11) NOT NULL,
	nome varchar(50) NOT NULL,
	CONSTRAINT pk_lista_casamento PRIMARY KEY (data, organizador, nome),
	CONSTRAINT fk_lista_casemento FOREIGN KEY (data, organizador)
		REFERENCES casamento(data, organizador)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE cerimonialista (
	nome varchar(50) NOT NULL,
	telefone varchar(15),
	linha_atuacao varchar(20),
	CONSTRAINT pk_cerimonialista PRIMARY KEY (nome)
);

CREATE TABLE casamento_cerimonialista (
	data timestamp NOT NULL,
	organizador char(11) NOT NULL,
	cerimonialista varchar(50),
	CONSTRAINT pk_casamento_cerimonialista PRIMARY KEY (data, organizador),
	CONSTRAINT fk_casamento_cerimonialista_casa FOREIGN KEY (data, organizador)
		REFERENCES casamento(data, organizador),
	CONSTRAINT fk_casamento_cerimonialista_ceri FOREIGN KEY (cerimonialista)
		REFERENCES cerimonialista(nome)
        ON DELETE SET NULL
);

CREATE TABLE empresa_tipo (
	CNPJ char(14) NOT NULL,
	tipo varchar(20) NOT NULL,
	CONSTRAINT pk_empresa_tipo PRIMARY KEY (CNPJ)
);

CREATE TABLE locacao (
	empresa char(14) NOT NULL,
	telefone varchar(15),
	email varchar(50),
	endereco varchar(150),
	CONSTRAINT pk_locacao PRIMARY KEY (empresa),
	CONSTRAINT fk_locacao FOREIGN KEY (empresa)
        REFERENCES empresa_tipo(CNPJ)
        ON DELETE CASCADE
);

CREATE TABLE decoracao (
	empresa char(14) NOT NULL,
	telefone varchar(15),
	email varchar(50),
	endereco varchar(150),
	CONSTRAINT pk_decoracao PRIMARY KEY (empresa),
	CONSTRAINT fk_decoracao FOREIGN KEY (empresa)
        REFERENCES empresa_tipo(CNPJ)
        ON DELETE CASCADE
);

CREATE TABLE floricultura (
	empresa char(14) NOT NULL,
	telefone varchar(15),
	email varchar(50),
	endereco varchar(150),
	CONSTRAINT pk_floricultura PRIMARY KEY (empresa),
	CONSTRAINT fk_floricultura FOREIGN KEY (empresa)
		REFERENCES empresa_tipo(CNPJ)
        ON DELETE CASCADE
);

CREATE TABLE transporte (
	empresa char(14) NOT NULL,
	telefone varchar(15),
	email varchar(50),
	endereco varchar(150),
	CONSTRAINT pk_transporte PRIMARY KEY (empresa),
	CONSTRAINT fk_transporte FOREIGN KEY (empresa)
        REFERENCES empresa_tipo(CNPJ)
        ON DELETE CASCADE
);

CREATE TABLE decor (
	tipo varchar(20) NOT NULL,
	cor varchar(20) NOT NULL,
	marca varchar(20) NOT NULL,
	empresa char(14),
	CONSTRAINT pk_decor PRIMARY KEY (tipo, cor, marca),
	CONSTRAINT fk_decor FOREIGN KEY (empresa)
        REFERENCES decoracao(empresa)
        ON DELETE CASCADE
);

CREATE TABLE casamento_decoracao (
	data timestamp NOT NULL,
	organizador char(11) NOT NULL,
	empresa char(14) NOT NULL,
	preco smallint NOT NULL,
	CONSTRAINT pk_casamento_decoracao PRIMARY KEY (data, organizador, empresa),
	CONSTRAINT fk_casamento_decoracao_casa FOREIGN KEY (data, organizador)
		REFERENCES casamento(data, organizador)
        ON DELETE CASCADE,
	CONSTRAINT fk_casamento_decoracao_deco FOREIGN KEY (empresa)
		REFERENCES decoracao(empresa)
        ON DELETE SET CASCADE
);

CREATE TABLE flor(
	empresa char(14) NOT NULL,
	especie varchar(20) NOT NULL,
	cor varchar(20) NOT NULL,
	CONSTRAINT pk_flor PRIMARY KEY (empresa, especie, cor),
	CONSTRAINT fk_flor FOREIGN KEY (empresa)
        REFERENCES floricultura(empresa)
        ON DELETE SET NULL
);

CREATE TABLE casamento_floricultura (
	data timestamp NOT NULL,
	organizador char(11) NOT NULL,
	empresa char(14) NOT NULL,
	preco smallint NOT NULL,
	CONSTRAINT pk_casamento_floricultura PRIMARY KEY
		(data, organizador, empresa),
	CONSTRAINT fk_casamento_floricultura_casa FOREIGN KEY (data, organizador)
		REFERENCES casamento(data, organizador)
        ON DELETE CASCADE,
	CONSTRAINT fk_casamento_floricultura_flor FOREIGN KEY (empresa)
		REFERENCES floricultura(empresa)
        ON DELETE SET NULL

);

CREATE TABLE veiculo_tipo (
	modelo varchar(20) NOT NULL,
	n_assentos smallint NOT NULL,
	CONSTRAINT pk_veiculo_tipo PRIMARY KEY (modelo)
);

CREATE TABLE transporte_veiculo (
	empresa char(14) NOT NULL,
	tipo varchar(20) NOT NULL,
	CONSTRAINT pk_transporte_veiculo PRIMARY KEY (empresa, tipo),
	CONSTRAINT fk_transporte_veiculo_trans FOREIGN KEY (empresa)
		REFERENCES transporte(empresa)
        ON DELETE CASCADE,
	CONSTRAINT fk_transporte_veiculo_mode FOREIGN KEY (tipo)
		REFERENCES veiculo_tipo(modelo)
        ON DELETE CASCADE
);

CREATE TABLE aluga (
	data timestamp NOT NULL,
	organizador char(11) NOT NULL,
	empresa char(14) NOT NULL,
	CONSTRAINT pk_aluga PRIMARY KEY (data, organizador, empresa),
	CONSTRAINT fk_aluga_univ FOREIGN KEY (data, organizador)
		REFERENCES universitaria(data, organizador)
        ON DELETE SET NULL,
	CONSTRAINT fk_aluga_trans FOREIGN KEY (empresa)
		REFERENCES transporte(empresa)
        ON DELETE CASCADE
);

CREATE TABLE espaco (
	CEP char(8) NOT NULL,
	categoria varchar(30),
	endereco varchar(200),
	capacidade integer,
	empresa char(14),
	CONSTRAINT pk_espaco PRIMARY KEY (CEP),
	CONSTRAINT fk_espaco FOREIGN KEY (empresa)
        REFERENCES locacao(empresa)
        ON DELETE CASCADE
);

CREATE TABLE casamento_espaco (
	data timestamp NOT NULL,
	organizador char(11) NOT NULL,
	espaco char(8),
	preco smallint NOT NULL,
	CONSTRAINT pk_casamento_espaco PRIMARY KEY (data, organizador),
	CONSTRAINT fk_casamento_espaco_casa FOREIGN KEY (data, organizador)
		REFERENCES casamento(data, organizador)
        ON DELETE CASCADE,
	CONSTRAINT fk_casamento_espaco_espa FOREIGN KEY (espaco)
		REFERENCES espaco(CEP)
        ON DELETE CASCADE
);

CREATE TABLE universitaria_espaco (
	data timestamp NOT NULL,
	organizador char(11) NOT NULL,
	espaco char(8),
	preco smallint NOT NULL,
	CONSTRAINT pk_universitaria_espaco PRIMARY KEY (data, organizador),
	CONSTRAINT fk_universitaria_espaco_casa FOREIGN KEY (data, organizador)
		REFERENCES universitaria(data, organizador)
        ON DELETE CASCADE,
	CONSTRAINT fk_universitaria_espaco_espa FOREIGN KEY (espaco)
		REFERENCES espaco(CEP)
        ON DELETE CASCADE
);

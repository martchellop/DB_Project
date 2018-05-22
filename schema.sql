
CREATE TABLE organizador (
	CPF char(11),
	nome varchar(50) NOT NULL,
	email varchar(50),
	telefone varchar(15),
	CONSTRAINT pk_organizador PRIMARY KEY (CPF)
);

CREATE TABLE empresa_tipo (
	CNPJ char(14),
	tipo varchar(20) not null,
	constraint pk_empresa_tipo primary key (CNPJ)
);

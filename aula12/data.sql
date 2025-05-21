create database etecBD;
use etecBD;
create table cadastro (
	id int auto_increment primary key,
    nome varchar(30) not null,
    sobrenome varchar(30) not null,
    idade int,
    sexo varchar(10),
    data_cadastro timestamp default current_timestamp
);

INSERT INTO aluno (nome, sobrenome, idade, sexo) VALUES 
('João', 'Silva', 18, 'Masculino'),
('Maria', 'Santos', 19, 'Feminino'),
('Pedro', 'Oliveira', 20, 'Masculino'),
('Ana', 'Costa', 17, 'Feminino'),
('Carlos', 'Pereira', 21, 'Masculino');

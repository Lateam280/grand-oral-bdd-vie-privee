create table utilisateurs (id int PRIMARY KEY not null,
                            nom varchar(15),
                            prenom varchar(15),
                            email varchar(50),
                            mot_de_passe varchar(100),
                            date_inscription date 
                            );

create table posts (id int PRIMARY KEY not null,
                    id_utilisateurs int,
                    contenu varchar(500),
                    date_publication date,
                    FOREIGN KEY (id_utilisateurs) REFERENCES utilisateurs(id)
);

create table connexions (id int PRIMARY KEY not null,
                         id_utilisateurs int,
                         date_connexion date,
                         adresse_ip varchar(15),
                         FOREIGN KEY (id_utilisateurs) REFERENCES utilisateurs(id)
);


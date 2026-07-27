DROP TABLE Installer CASCADE CONSTRAINTS;
DROP TABLE Poste CASCADE CONSTRAINTS;
DROP TABLE Logiciel CASCADE CONSTRAINTS;
DROP TABLE Salle CASCADE CONSTRAINTS;
DROP TABLE Agent CASCADE CONSTRAINTS;

CREATE TABLE Agent (
    NumAgent   VARCHAR2(5) PRIMARY KEY,
    NomAgent   VARCHAR2(30) NOT NULL,
    Prenom     VARCHAR2(30) NOT NULL
);

CREATE TABLE Salle (
    NumSalle     VARCHAR2(5) PRIMARY KEY,
    NomSalle     VARCHAR2(40) NOT NULL,
    TypeSalle    VARCHAR2(20),
    NbPoste      NUMBER(3),
    Responsable  VARCHAR2(5),
    CONSTRAINT fk_salle_agent FOREIGN KEY (Responsable) REFERENCES Agent(NumAgent)
);

CREATE TABLE Poste (
    NumPoste   VARCHAR2(5) PRIMARY KEY,
    NomPoste   VARCHAR2(40) NOT NULL,
    NumSalle   VARCHAR2(5),
    CONSTRAINT fk_poste_salle FOREIGN KEY (NumSalle) REFERENCES Salle(NumSalle)
);

CREATE TABLE Logiciel (
    NumLog     VARCHAR2(5) PRIMARY KEY,
    NomLog     VARCHAR2(40),
    Prix       NUMBER(8,2),
    DateAchat  DATE
);

CREATE TABLE Installer (
    NumPoste     VARCHAR2(5),
    NumLog       VARCHAR2(5),
    DateInstall  DATE,
    CONSTRAINT pk_installer PRIMARY KEY (NumPoste, NumLog),
    CONSTRAINT fk_inst_poste FOREIGN KEY (NumPoste) REFERENCES Poste(NumPoste),
    CONSTRAINT fk_inst_log FOREIGN KEY (NumLog) REFERENCES Logiciel(NumLog)
);

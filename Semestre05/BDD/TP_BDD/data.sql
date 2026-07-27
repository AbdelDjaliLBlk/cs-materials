-- Agents
INSERT INTO Agent VALUES ('A1', 'Benslimane', 'Karim');
INSERT INTO Agent VALUES ('A2', 'Dib', 'Amine');
INSERT INTO Agent VALUES ('A3', 'Saidi', 'Fedoua');

-- Salles
INSERT INTO Salle VALUES ('S1', 'Salle Réseaux', 'Réseaux', 10, 'A1');
INSERT INTO Salle VALUES ('S2', 'Salle Programmation', 'Programmation', 12, 'A2');
INSERT INTO Salle VALUES ('S3', 'Salle BigData', 'BigData', 8, 'A3');

-- Postes
INSERT INTO Poste VALUES ('P1', 'PosteReseau_1', 'S1');
INSERT INTO Poste VALUES ('P2', 'PosteReseau_2', 'S1');
INSERT INTO Poste VALUES ('P3', 'PosteProg_1', 'S2');
INSERT INTO Poste VALUES ('P4', 'PosteBigData_1', 'S3');
INSERT INTO Poste VALUES ('P5', 'PosteBigData_2', 'S3');

-- Logiciels
INSERT INTO Logiciel VALUES ('L1', 'Wireshark', 0, TO_DATE('2023-03-10','YYYY-MM-DD'));
INSERT INTO Logiciel VALUES ('L2', 'Python', 0, TO_DATE('2024-01-15','YYYY-MM-DD'));
INSERT INTO Logiciel VALUES ('L3', 'Oracle', 1500, TO_DATE('2022-07-20','YYYY-MM-DD'));
INSERT INTO Logiciel VALUES ('L4', 'VSCode', 0, TO_DATE('2024-04-05','YYYY-MM-DD'));
INSERT INTO Logiciel VALUES ('L5', 'RStudio', 500, TO_DATE('2023-12-01','YYYY-MM-DD'));

-- Installations
INSERT INTO Installer VALUES ('P1', 'L1', TO_DATE('2023-03-12','YYYY-MM-DD'));
INSERT INTO Installer VALUES ('P2', 'L1', TO_DATE('2023-03-12','YYYY-MM-DD'));
INSERT INTO Installer VALUES ('P3', 'L2', TO_DATE('2024-01-18','YYYY-MM-DD'));
INSERT INTO Installer VALUES ('P4', 'L3', TO_DATE('2022-08-01','YYYY-MM-DD'));
INSERT INTO Installer VALUES ('P5', 'L5', TO_DATE('2023-12-10','YYYY-MM-DD'));

//TP2:
//CREATE OR REPLACE VIEW VLogicielsRecents AS SELECT * FROM logiciel WHERE DateAchat > TO_DATE('2023-01-01','YYYY-MM-DD') WITH CHECK OPTION CONSTRAINT verif_dateachat; 
//CREATE TABLE TLogicielsRecents AS SELECT * FROM logiciel WHERE DateAchat > TO_DATE('2023-01-01','YYYY-MM-DD'); 
//INSERT INTO Logiciel VALUES ('L33', 'Avast', 3000, TO_DATE('2020-03-15', 'YYYY-MM-DD'));
//INSERT INTO Logiciel VALUES ('L34', 'Kaspersky', 2500, TO_DATE('2024-03-15', 'YYYY-MM-DD'));

//INSERT INTO VLogicielsRecents VALUES ('L35', 'AVG', 3500, TO_DATE('2022-03-15', 'YYYY-MM-DD')) ;
//--->Contraint violated.
//CREATE OR REPLACE VIEW VInstallationDetail 

//SELECT * FROM VLogicielsRecents;


/*
//TP3:
SET SERVEROUTPUT ON;
DECLARE
vNbposte Number;
BEGIN
SELECT nbPoste into vNbposte FROM salle
WHERE typesalle='Programmation';
DBMS_OUTPUT.PUT_LINE('Nombre total de postes (type = informatique) : ' || vNbposte);
END;
/


DECLARE
    VNumlog   logiciel.NumLog%TYPE;
    VNomlog   logiciel.NomLog%TYPE;
    VNbposte  NUMBER;
BEGIN
    SELECT l.NumLog, l.NomLog, COUNT(i.NumPoste)
    INTO VNumlog, VNomlog, VNbposte
    FROM Logiciel l
    LEFT JOIN Installer i ON l.NumLog = i.NumLog
    WHERE l.NumLog = 'L3'
    GROUP BY l.NumLog, l.NomLog;
    DBMS_OUTPUT.PUT_LINE('Le logiciel qui a le numéro ' || VNumlog ||' se nomme ' || VNomlog ||', il est installé sur ' || VNbposte || ' postes.');
END;
/
*/
GRANT CREATE TRIGGER TO USERBDDING;
/*
CREATE TRIGGER Maj_Nom_Log 
BEFORE INSERT OR UPDATE ON LOGICIEL
FOR EACH ROW
BEGIN
 :NEW.NomLog := UPPER(:NEW.NomLog);
END;
/

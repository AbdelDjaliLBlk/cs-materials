#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define Q0  0
#define Q1  1
#define Q2  2
#define ERR  -1

#define IDENTIFIANT_UL 260
#define NOMBRE_UL 261
#define PLUS 262
#define MINUS 263
#define MULTIPLY 264
#define DIVIDE 265
#define PARENTHESE_OUVRANTE 266
#define PARENTHESE_FERMANTE 267
#define SYMBOLE_AFFECTATION 269
#define SEPARATEUR_POINT_VIRGULE 270
#define FIN_SUITE_UL 999

typedef struct Unite_Lexicale {
    char Lexeme[20];
    int Code;
    int Ligne;
    struct Unite_Lexicale* Suivant;
} UL;

void inserer_fin(UL** tete, const char* lexeme, int code, int ligne) {
    UL* nouveau = (UL*)malloc(sizeof(UL));
    strcpy(nouveau->Lexeme, lexeme);
    nouveau->Code = code;
    nouveau->Ligne = ligne;
    nouveau->Suivant = NULL;

    if (*tete == NULL) {
        *tete = nouveau;
    } else {
        UL* temp = *tete;
        while (temp->Suivant != NULL) temp = temp->Suivant;
        temp->Suivant = nouveau;
    }
}

int code_caractere(char c) {
    if (c == '+') return PLUS;
    if (c == '-') return MINUS;
    if (c == '*') return MULTIPLY;
    if (c == '/') return DIVIDE;
    if (c == '(') return PARENTHESE_OUVRANTE;
    if (c == ')') return PARENTHESE_FERMANTE;
    if (c == '=') return SYMBOLE_AFFECTATION;
    if (c == ';') return SEPARATEUR_POINT_VIRGULE;
    return ERR;
}

UL* globAutomat(const char* str) {
    UL* liste_head = NULL;
    int etat = Q0;
    int ligne = 1;
    int i = 0;
    char buffer[20];
    
    FILE* file = fopen(str, "r");
    if (file == NULL) {
        printf("Erreur d'ouverture du fichier.\n");
        exit(EXIT_FAILURE);
    }

    char c;
    while ((c = fgetc(file)) != EOF) {
        if (c == '\n') {
            ligne++;
            c = ' ';
        }

        switch (etat) {
            case Q0:
                if (isalpha(c)) {
                    etat = Q1;
                    buffer[i++] = c;
                } else if (isdigit(c)) {
                    etat = Q2;
                    buffer[i++] = c;
                } else if (isspace(c)) {
                    etat = Q0;
                } else {
                    int char_code = code_caractere(c);
                    if (char_code != ERR) {
                        buffer[0] = c; 
                        buffer[1] = '\0';
                        inserer_fin(&liste_head, buffer, char_code, ligne);
                        etat = Q0;
                    } else {
                        etat = ERR;
                    }
                }
                break;

            case Q1:
                // Rule: \w[\d\w_]*
                if (isalnum(c) || c == '_') {
                    etat = Q1;
                    buffer[i++] = c;
                } else if (isspace(c) || code_caractere(c) != ERR) {
                    buffer[i] = '\0';
                    inserer_fin(&liste_head, buffer, IDENTIFIANT_UL, ligne);
                    i = 0;
                    
                    etat = Q0;
                    ungetc(c, file);
                } else {
                    etat = ERR;
                }
                break;

            case Q2:
                // Rule: [\d]+
                if (isdigit(c)) {
                    etat = Q2;
                    buffer[i++] = c;
                } else if (isspace(c) || code_caractere(c) != ERR) {
                    buffer[i] = '\0';
                    inserer_fin(&liste_head, buffer, NOMBRE_UL, ligne);
                    i = 0;
                    
                    etat = Q0;
                    ungetc(c, file);
                } else {
                    etat = ERR;
                }
                break;
        }

        if (etat == ERR) {
            printf("Erreur Lexicale : caractere invalide '%c' a la ligne %d\n", c, ligne);
            fclose(file);
            exit(EXIT_FAILURE);
        }
    }

    if (etat == Q1) {
        buffer[i] = '\0';
        inserer_fin(&liste_head, buffer, IDENTIFIANT_UL, ligne);
    } else if (etat == Q2) {
        buffer[i] = '\0';
        inserer_fin(&liste_head, buffer, NOMBRE_UL, ligne);
    }

    inserer_fin(&liste_head, "#", FIN_SUITE_UL, ligne);
    
    fclose(file);
    return liste_head;
}

int main() {
    const char* fichier_test = "C:\\Users\\PC\\CLionProjects\\Compilation\\testfile.txt";
    UL* liste = globAutomat(fichier_test);
    UL* courant = liste;

    while (courant != NULL) {
        printf("Lexeme: [%s] \t Code: [%d] \t Ligne: [%d]\n", courant->Lexeme, courant->Code, courant->Ligne);
        courant = courant->Suivant;
    }

    return 0;
}
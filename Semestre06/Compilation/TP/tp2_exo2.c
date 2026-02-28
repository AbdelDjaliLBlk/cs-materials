#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
int i=0; 

// ---Cellule---
typedef struct cellule{ 
 int valeur; 
 struct cellule * next; 
}Element; 
// ---Pile---
typedef struct pile{ 
 Element* sommet; 
}Pile; 
Pile* InitialiserPile (Pile* p){ 
  p=malloc(sizeof(Pile)); 
    p->sommet=NULL; 
 return p;} 
Pile* Empiler (Pile* p,int v){ 
    Element* nouveauElement= malloc (sizeof (Element)); 
    nouveauElement->valeur=v; 
    nouveauElement->next=p->sommet; 
    p->sommet=nouveauElement; 
    return p; 
} 
Pile* Depiler (Pile* p){ 
 if (p->sommet==NULL) 
  return p; 
 Element* e; 
 e=p->sommet; 
 p->sommet=p->sommet->next; 
 free(e); 
 return p; 
} 
int SommetPile (Pile* p){ 
 if (p->sommet==NULL) 
          return -9999; /** code pile vide */ 
     else 
          return p->sommet->valeur; 
} 
void AfficherPile (Pile* p){ 
 Element *ep=p->sommet; 
 while (ep!=NULL){ 
  printf("\n |%d|",ep->valeur); 
  ep=ep->next; 
 } 
 printf("\n"); 
} 
Pile* ViderPile (Pile* p){ 
 while (p->sommet!=NULL){ 
  Element *e=p->sommet; 
  p->sommet=p->sommet->next; 
  free(e); 
 } 
 return p; 
}

// ---File---
typedef struct file{ 
 Element* sommet; 
 Element* queue; 
}File; 
File* InitialiserFile(File* f){ 
 f=malloc(sizeof(File)); 
 f->sommet=NULL; 
 f->queue=NULL; 
 return f;} 
File* Enfiler (File* f,int v){ 
    Element* nouveauElement= malloc (sizeof (Element)); 
    nouveauElement->valeur=v; 
 nouveauElement->next=NULL; 
 if (f->sommet==NULL){ 
  f->sommet=nouveauElement; 
  f->queue=nouveauElement; 
  return f;} 
 f->queue->next=nouveauElement; 
 f->queue=nouveauElement; 
 return f;} 
File* Defiler (File* f){ 
 if (f->sommet==NULL) 
  return f; 
 else if(f->sommet==f->queue){ 
  free(f->sommet); 
  f->sommet=NULL; 
  f->queue=NULL; 
          return  f;} 
 Element* e; 
 e=f->sommet; 
 f->sommet=f->sommet->next; 
 free(e); 
 return f;} 
int SommetFile (File* f){ 
   if(f->sommet==NULL) return -9999;  /** code file vide */ 
  else    return f->sommet->valeur;} 
void AfficherFile (File* f){ 
 Element *ep=f->sommet; 
 while (ep!=NULL){ 
  printf(" |%d| ",ep->valeur); 
  ep=ep->next;} } 
File* ViderFile (File* f){ 
 while (f->sommet!=NULL){ 
  Element *e=f->sommet; 
  f->sommet=f->sommet->next; 
  free(e); } 
 f->sommet=NULL; 
 f->queue=NULL; 
 return f;} 

int main(){ 
    FILE *file;     
    char chaine[100]  = {0}; //variable chaine de caractère  
    char c;  
    file = fopen("test.txt","w");  
    /**en cas d’erreur **/ 
    if(file == NULL){ 
        printf("Erreur"); 
        return 0; 
    } 
 
    printf("Entrer une chaine: "); 
    fgets(chaine,100,stdin); 
    fprintf(file,"%s",chaine); 
    fclose(file); 
 
/**Lecture d'un fichier Ligne par Ligne et Affichage sur Ecran **/ 
    file = fopen("test.txt","r");  
    if(file == NULL){ 
        printf("Erreur"); 
        return 0; 
    } 

    while( fgets (chaine,100, file)!=NULL ) 
        puts(chaine);
    fclose(file); 
 
/**Lecture d'un fichier Carectere par Caractere et 
Affichage sur Ecran **/ 
    file = fopen("test.txt","r"); 
    if(file == NULL){ 
        printf("Erreur"); 
        return 0; 
    } 
    while ((c = fgetc(file)) != EOF)
        putc(c,stdout); 
fclose(file);
}
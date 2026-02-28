/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
package Test;
*/

/*
 *
 * @author DVSR
 */
import java.io.*;
import java.net.*;
import javax.swing.JOptionPane;

public class Client {
    public static void main(String [] args){       
        String NomDuServeur="127.0.0.1";
        int port=9500;
        Socket ConnexionAUnServeur;
        
        DataInputStream FluxDEntrer;
        DataOutputStream FluxSortie;
        String MessageATransmettre;

    try {
        
            System.out.println("Lancement de l'application Client "+InetAddress.getLocalHost());
            ConnexionAUnServeur = new Socket(InetAddress.getByName(NomDuServeur), port);
            FluxSortie = new DataOutputStream(ConnexionAUnServeur.getOutputStream()); 
            FluxDEntrer = new DataInputStream(ConnexionAUnServeur.getInputStream());
        do{
              MessageATransmettre=JOptionPane.showInputDialog("Entrez le message à transmettre:");
              byte[] b= new byte[MessageATransmettre.length()];
              
              int i=0;
              for(char c:MessageATransmettre.toCharArray()){
                  b[i]=(byte)c;
                  i++;
              }
              
              FluxSortie.write(b);
              

        }while(!MessageATransmettre.equalsIgnoreCase("Fin")); 
        
        System.out.println("Deconnexion");
        ConnexionAUnServeur.close();                       
    }
    catch (Exception e) {
        System.out.println("Erreur ="+e);
    }
    }
    
}
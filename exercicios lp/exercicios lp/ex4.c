import java.util.*;
public class Desafio

//Funções para transformar para maiúsculo

{
   public static void main(String args[])
   {
       Scanner key= new Scanner (System.in);
       System.out.println("Digite uma sequencia de caracteres");
       String valor = key.next(); //sequencia de caracteres armazenada em " valor"
       
       String valorMaiusculo= valor.toUpperCase(); //transformar todas as letras para maiusculo e armazenar em "valorMaiusculo"
       //System.out.println(valorMaiusculo);
       String strApenasNum= RetornaNumeroseLetras(valorMaiusculo);//chamar metodo e armazenar na variavel "strApenasNum"
       System.out.println(strApenasNum);
    }
    
   public static String RetornaNumeroseLetras(String str)// metodo que recebe uma string e tem a funcao de retirar todos os caracteres que nao sao numeros e nem letras
   {
       if (str != null)//caso a string nao esteja vazia
       {
           return str.replaceAll("[^0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ]","");//usa-se o metodo replaceAll, no qual tem a funcao de "nomedastring.replaceAll(String a ser substituida ou mantido, string que substitui)
       }
       else
       {
           return "";
       }
   }
}
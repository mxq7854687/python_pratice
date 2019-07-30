/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package euler_project;

/**
 *
 * @author richardlee
 */
import java.util.*;
public class Euler_Project_Solution_001 {


    public static void main(String[] args) {
        int n=1000000000;
        long sum = 0;
        int [] arr = new int [n];
        int mysum=0;
        ArrayList<Integer> array = new ArrayList<Integer>();
        for(int i =3; i<n; i+=3){
            mysum+=i;
        }
        for(int j=5; j<n; j+=5){
            if(j%3 !=0){mysum+=j;}
        }
        //for(Integer num:array){
       //     sum+=num;}
        System.out.println(mysum);
    }
    
}

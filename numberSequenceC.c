#include <stdio.h>
int main()
{
   //Since there are nested sub-sequences, all the numbers that repeat after
   //cetain count should be noted in-order to predict the next number.
   //Thus, we use the count variables to predict the difference between the 
   //current and next number.
   int count3_1 = 0;
   int count4_1 = 0;
   int count5_1 = 0;
   int count6_1 = 0;
   int count7_1 = 0;
   int count8_1 = 0;
   int count9_1 = 0;
   int count10_1 = 0;
   int count11_1 = 0;

   //Flag variables are used to add a check so that the next number predicted in the
   //sequence is the correct number.
   int flag4 = 0;
   int flag5 = 0;
   int flag6 = 0;
   int flag7 = 0;
   int flag8 = 0;
   int flag9 = 0;
   int flag10 = 0;
   int flag11 = 0;
   int count = 0;
   int number = 4;
   int flagExecuted = 0;

   //'i' is the counter variable for the loop
   int i = 0;

   // Since wee need to find the 10000th number,
   //the for loop should iterate from 0 to 10000.
   for (i = 0; i<10000 ; i++) {
      flagExecuted = 0;
      count3_1 = count3_1 + 1;
      count4_1 = count4_1 + 1;
      count5_1 = count5_1 + 1;
      count6_1 = count6_1 + 1;
      count7_1 = count7_1 + 1;
      count8_1 = count8_1 + 1;
      count9_1 = count9_1 + 1;
      count10_1 = count10_1 + 1;
      count11_1 = count11_1 + 1;
      count = count +1;

      printf("Generic Count: %d\n",count);

      if (count3_1 == 3 || count3_1 == 4) {
            number = number + 3;
            printf("Increment by 3 %d\n",number);
            if (count3_1 == 4){
               count3_1 = 0;
            } 
            else {
               flagExecuted = 1;
            }
         }

      else if (((count4_1 == 1 || count4_1 == 6) && flag4 == 0) || ((count4_1 == 3 || count4_1 == 8) && flag4 == 1)) {
         if ((count4_1 == 1 || count4_1 == 6) && flag4 == 0) {
            number = number + 4;
            printf("Increment by 4 %d\n",number);
            if (count4_1 == 6) {
               count4_1 = 0;
               flag4 = 1;
            }
         }
         else if ((count4_1 == 3 || count4_1 == 8) && flag4 == 1) {
            number = number + 4;
            printf("Increment by 4 %d\n",number);
            if (count4_1 == 8) {
               count4_1 = 0;
            }
         }
         else {
            flagExecuted = 1;
         }
      }

      else if (((count5_1 == 2 || count5_1 == 13) && flag5 == 0) || ((count5_1 == 5 || count5_1 == 16) && flag5 == 1)) {
         if ((count5_1 == 2 || count5_1 == 13) && flag5 == 0) {
            number = number + 5;
            printf("Increment by 5 %d\n",number);
            if (count5_1 == 13) {
               count5_1 = 0;
               flag5 = 1;
            }
         }
         else if ((count5_1 == 5 || count5_1 == 16) && flag5 == 1) {
            number = number + 5;
            printf("Increment by 5 %d\n",number);
            if (count5_1 == 16) {
               count5_1 = 0;
            }
         }
         else {
            flagExecuted = 1;
         }
      }

      else if (((count6_1 == 5 || count6_1 == 26) && flag6 == 0) || ((count6_1 == 11 || count6_1 == 32) && flag6 == 1)) {
         if ((count6_1 == 5 || count6_1 == 26) && flag6 == 0) {
            number = number + 6;
            printf("Increment by 6 %d\n",number);
            if (count6_1 == 26) {
               count6_1 = 0;
               flag6 = 1;
            }
         }
         else if (((count6_1 == 11 || count6_1 == 32) && flag6 == 1)) {
            number = number + 6;
            printf("Increment by 6 %d\n",number);
            if (count6_1 == 32) {
               count6_1 = 0;
            }
         }
         else {
            flagExecuted = 1;
         }
      }

      else if (((count7_1 == 10 || count7_1 == 53) && flag7 == 0) || ((count7_1 == 21 || count7_1 == 64) && flag7 == 1)) {
         if ((count7_1 == 10 || count7_1 == 53) && flag7 == 0) {
            number = number + 7;
            printf("Increment by 7 %d\n",number);
            if (count7_1 == 53) {
               count7_1 = 0;
               flag7 = 1;
            }
         }
         else if (((count7_1 == 21 || count7_1 == 64) && flag7 == 1)) {
            number = number + 7;
            printf("Increment by 7 %d\n",number);
            if (count7_1 == 64) {
               count7_1 = 0;
            }
         }
         else {
            flagExecuted = 1;
         }
      }

      else if (((count8_1 == 21 || count8_1 == 106) && flag8 == 0) || ((count8_1 == 43 || count8_1 == 128) && flag8 == 1)) {
         if ((count8_1 == 21 || count8_1 == 106) && flag8 == 0) {
            number = number + 8;
            printf("Increment by 8 %d\n",number);
            if (count8_1 == 106) {
               count8_1 = 0;
               flag8 = 1;
            }
         }
         else if (((count8_1 == 43 || count8_1 == 128) && flag8 == 1)) {
            number = number + 8;
            printf("Increment by 8 %d\n",number);
            if (count8_1 == 128) {
               count8_1 = 0;
            }
         }
         else {
            flagExecuted = 1;
         }
      }

      else if (((count9_1 == 42 || count9_1 == 213) && flag9 == 0) || ((count9_1 == 85 || count9_1 == 256) && flag9 == 1)){
         if ((count9_1 == 42 || count9_1 == 213) && flag9 == 0) {
            number = number + 9;
            printf("Increment by 9 %d\n",number);
            if (count9_1 == 213) {
               count9_1 = 0;
               flag9 = 1;
            }
         }
         else if (((count9_1 == 95 || count9_1 == 256) && flag9 == 1)) {
            number = number + 9;
            printf("Increment by 9 %d\n",number);
            if (count9_1 == 256) {
               count9_1 = 0;
            }
         }
      }

      else if (((count10_1 == 85 || count10_1 == 426) && flag10 == 0) || ((count10_1 == 171 || count10_1 == 512) && flag10 == 1)) {
         if ((count10_1 == 85) && flag10 == 0) {
            number = number + 10;
            printf("Increment by 10 %d\n",number);
         }
         else if (((count10_1 == 171 || count10_1 == 512) && flag10 == 1)) {
            number = number + 10;
            printf("Increment by 10 %d\n",number);
            if (count10_1 == 512) {
               count10_1 = 0;
            }
         }
      }

      else {
         number = number + 11;
         printf("Increment by 11 %d\n",number);
         printf("X");
      }
   }
}
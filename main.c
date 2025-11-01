#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// section Input calculator
float numberA()
{
  float a;
  printf("num 1 : ");
  scanf("%f", &a);
  return a;
}

float numberB()
{
  float b;
  printf("num 2 : ");
  scanf("%f", &b);
  printf("\n");
  return b;
}

// section TextItem
void textitem()
{
  printf("choose item calculator : \n\n");
  printf("============ \n\n");
  printf("Item 1 : (+) \n");
  printf("------------ \n");
  printf("Item 2 : (-) \n");
  printf("------------ \n");
  printf("Item 3 : (*) \n");
  printf("------------ \n");~
  printf("Item 4 : (/) \n");
  printf("------------ \n");
  printf("Item 5 : (q) \n");
  printf("\n");
}

// section KeyItem
char keyitem()
{
  char item;
  printf("enter key calculator : ");
  scanf("%c", &item);
  return item;
}

// section Add
void add()
{
  float res = numberA() + numberB();
  printf("result Add :=> %f \n\n", res);
}

// section Sub
void sub()
{
  float res = numberA() - numberB();
  printf("result Sub :=> %f \n\n", res);
}

// section Mult
void mult()
{
  float res = numberA() * numberB();
  printf("result Mult :=> %f \n\n", res);
}

// section Div
void divi()
{
  float res = numberA() / numberB();
  printf("result Div :=> %f \n\n", res);
}

// section Proccess
void proccess()
{
  textitem();
  char ch;
  while (true)
  {
    ch = keyitem();
    if (ch == 'q')
    {
      break;
    }
    else
    {
      switch (ch)
      {
      case '+':
        add();
        break;
      case '-':
        sub();
        break;
      case '*':
        mult();
        break;
      case '/':
        divi();
        break;
      default:
        break;
      }
    }
  }
}

int main()
{
  proccess();
  return 0;
}

// int arr[3][3][4];
// int x, y, z;

// printf("enter array x : \n", x);
// scanf("%d", &x);

// printf("enter array y: \n", y);
// scanf("%d", &y);

// printf("enter array z: \n", z);
// scanf("%d", &z);

// for (int i = 0; i < x; i++)
// {
//   for (int j = 0; j < y; j++)
//   {
//     for (int l = 0; l < z; l++)
//     {
//       printf("enter zoon : \n ");
//       scanf("%d", &arr[i][j][l]);
//     }
//   }
// }

// for (int i = 0; i < x; i++)
// {
//   for (int j = 0; j < y; j++)
//   {
//     for (int l = 0; l < z; l++)
//     {
//       printf("index x, y, z : %d | %d | %d \n", i + 0, j + 0, l + 0);
//       printf("output x, y, z : %d \n", arr[i][j][l]);
//     }
//   }
// }

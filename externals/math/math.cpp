#include "math.h"

#include "logger.h"

int Fibonacci(int nElements)
{
   int sum = 0;
   for (int i = 0; i <= nElements; ++i)
   {
      sum += i;
   }

   Logger log;
   log.Log("The series was calculated\n");

   return sum;
}

#include <sstream>

#include "logger.h"
#include "math.h"

int main(void)
{
   Logger log;
   log.Log("The Fibonacci series is a grand thing");

   for (int i = 0; i < 10; ++i)
   {
      std::stringstream ss;
      ss << "F" << i << " = " << Fibonacci(i) << std::endl;
      log.Log(ss.str());
   }

   return 0;
}

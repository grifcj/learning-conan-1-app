#include <gmock/gmock.h>

#include "fibonacci.h"

TEST(Fibonacci, ReturnCorrectAnswer)
{
   EXPECT_EQ(Fibonacci(0), 0);
   EXPECT_EQ(Fibonacci(1), 1);
   EXPECT_EQ(Fibonacci(2), 3);
   EXPECT_EQ(Fibonacci(3), 6);
   EXPECT_EQ(Fibonacci(4), 10);
}

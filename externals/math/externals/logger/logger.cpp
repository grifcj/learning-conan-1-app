#include "logger.h"

#include <iostream>

void Logger::Log(const std::string& msg)
{
   std::cout << msg << std::endl;
}

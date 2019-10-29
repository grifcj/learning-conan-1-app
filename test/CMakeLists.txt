add_test(NAME unittest COMMAND $<TARGET_FILE:app>)
set_tests_properties(
   unittest
   PROPERTIES
   PASS_REGULAR_EXPRESSION "Fibonacci.*grand")

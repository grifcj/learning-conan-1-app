include(FetchContent)
set(FETCHCONTENT_QUIET OFF CACHE BOOL "" FORCE)
set(FETCHCONTENT_UPDATES_DISCONNECTED ON CACHE BOOL "" FORCE)

set(prefix ${CMAKE_CURRENT_LIST_DIR}/build/externals)

FetchContent_Declare(googletest
   URL https://github.com/google/googletest/archive/release-1.8.0.zip
   SOURCE_DIR ${prefix}/googletest
   )
FetchContent_Declare(logger
   GIT_REPOSITORY git@github.com:grifcj/cmake-logger
   SOURCE_DIR ${prefix}/logger
   )
FetchContent_Declare(math
   GIT_REPOSITORY git@github.com:grifcj/cmake-math
   SOURCE_DIR ${prefix}/math
   )

function(MakeAvailable)
   foreach(ext ${ARGV})
      FetchContent_GetProperties(${ext})

      string(TOUPPER ${ext} upperExt)
      if (EXISTS ${prefix}/${ext})
         message(STATUS "External exists: ${ext}")
         set(FETCHCONTENT_SOURCE_DIR_${upperExt} ${prefix}/${ext})
      else()
         message(STATUS "External doesn't exist: ${ext}")
         unset(FETCHCONTENT_SOURCE_DIR_${upperExt} CACHE)
         file(GLOB globResult LIST_DIRECTORIES TRUE "${FETCHCONTENT_BASE_DIR}/${ext}*")
         if (${globResult})
            file(REMOVE_RECURSE ${globResult})
         endif()
      endif()

      if (NOT ${ext}_POPULATED)
         FetchContent_Populate(${ext})
         add_subdirectory(${${ext}_SOURCE_DIR} ${${ext}_BINARY_DIR})
      endif()
   endforeach()
endfunction()

MakeAvailable(googletest logger math)

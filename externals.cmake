include(FetchContent)

# We want noisy, so we can see progress of population
set(FETCHCONTENT_QUIET OFF CACHE BOOL "" FORCE)

# Don't attempt to automatically update externals. This greatly speeds up
# configure step and re-runs of build system. If user wants to change external,
# then they can simply remove it, and it will be automatically populated.
set(FETCHCONTENT_UPDATES_DISCONNECTED ON CACHE BOOL "" FORCE)

# Place externals in build directory, but at a fixed location accessible to all build configs
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
         # Prevent additional downloads for every build configuration when
         # source directory already exists.
         set(FETCHCONTENT_SOURCE_DIR_${upperExt} ${prefix}/${ext})
      else()
         # When source directory doesn't exist, assume we have removed it.
         # It'll be the same as the first time we run. We have to remove a few
         # things to force FetchContent module to repopulate content.
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

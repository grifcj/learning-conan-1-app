function(AddExternal external)
   if (${${external}_DIR})
      set(path ${${external}_DIR})
   elseif(${EXTERNAL_PREFIX})
      set(path ${EXTERNAL_PREFIX}/${external})
   else()
      set(path ${CMAKE_CURRENT_SOURCE_DIR}/externals/${external})
   endif()

   if (NOT ${external}_POPULATED)
      set(${external}_POPULATED TRUE PARENT_SCOPE)
      message(STATUS "Adding external: ${path}")

      if (EXISTS ${path}/CMakeLists.txt)
         add_subdirectory(${path})
      else()
         list(APPEND CMAKE_PREFIX_PATH ${path})
         find_package(${path} CONFIG REQUIRED)
      endif()
   endif()
endfunction()

function(AddExternals)
   foreach(external ${ARGV})
      AddExternal(${external})
   endforeach()
endfunction()



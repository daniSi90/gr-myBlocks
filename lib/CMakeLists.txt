# Copyright 2011,2012,2016 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.


########################################################################
# QT GUI file generation stuff (Q_OBJECT)
########################################################################
# Headerji iz Lib
set(QTGUI_MOC_HEADERS
  spectrogram_plot.h)
QT4_WRAP_CPP(QTGUI_MOC_OUTFILES ${QTGUI_MOC_HEADERS})


########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})
list(APPEND myBlocks_sources
    ${QTGUI_MOC_OUTFILES}
    phaseSync_cc_impl.cc
    aoa_spectrum_sink_impl.cc 
    spectrogram_plot.cc)

set(myBlocks_sources "${myBlocks_sources}" PARENT_SCOPE)
if(NOT myBlocks_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT myBlocks_sources)

add_library(gnuradio-myBlocks SHARED ${myBlocks_sources})
#add_executable(foo foo.cc)
#target_link_libraries(foo ${ARMADILLO_LIBRARIES})
target_link_libraries(gnuradio-myBlocks
                      ${Boost_LIBRARIES} 
                      ${GNURADIO_ALL_LIBRARIES} 
                      ${LAPACK_LIBRARIES} 
                      ${BLAS_LIBRARIES}
                      ${ARMADILLO_LIBRARIES}
                      ${QWT_LIBRARIES}
                      ${QT_LIBRARIES})
set_target_properties(gnuradio-myBlocks PROPERTIES DEFINE_SYMBOL "gnuradio_myBlocks_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-myBlocks PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
include(GrMiscUtils)
GR_LIBRARY_FOO(gnuradio-myBlocks RUNTIME_COMPONENT "myBlocks_runtime" DEVEL_COMPONENT "myBlocks_devel")

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_myBlocks_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_myBlocks.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_myBlocks.cc
)

add_executable(test-myBlocks ${test_myBlocks_sources})

target_link_libraries(
  test-myBlocks
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  ${QWT_LIBRARIES}
  ${QT_LIBRARIES}
  gnuradio-myBlocks
)

GR_ADD_TEST(test_myBlocks test-myBlocks)

########################################################################
# Print summary
########################################################################
message(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Building for version: ${VERSION} / ${LIBVER}")


BOOST_INC_DIR = []
BOOST_LIB_DIR = []
BOOST_COMPILER = 'gcc43'
BOOST_PYTHON_LIBNAME = ['boost_python']
USE_SHIPPED_BOOST = True
CL_TRACE = False
CL_ENABLE_GL = False
CL_ENABLE_DEVICE_FISSION = True
CL_INC_DIR = []
CL_LIB_DIR = []
CL_LIBNAME = []
CXXFLAGS = ['-arch', 'i386', '-arch', 'x86_64', '-isysroot', '/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk']
LDFLAGS = ['-arch', 'i386', '-arch', 'x86_64', '-isysroot', '/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk', '-Wl', '-framework', 'OpenCL']

# VectorPy
Python version of Seanthebuilder1's VectorMath

# Compile
To compile using g++ use command:
```
g++ -O3 -std=c++17 -static-libgcc -static-libstdc++ -o main.exe -g ./src/*.h ./src/*.cpp
```

# Using CMake
To compile using CMake
```
cmake . -G "MinGW Makefiles"
make
```

# Database
A custom C++ database editor in command line. Uses custom database format.

# Database Format
```
//table             >format (//table or //list)
//3                 >columns (1 for //list)
`Index              >index for item
content             
content
content
`Index2             >index for item
content
content
content
`                   >end of file
```

#	this was made by kieran lavato

# 								\
	▗▄▄▄▖▗▖  ▗▖▗▄▄▄▖ ▗▄▖ 		\
	  █  ▐▛▚▖▐▌▐▌   ▐▌ ▐▌		\
	  █  ▐▌ ▝▜▌▐▛▀▀▘▐▌ ▐▌		\
	▗▄█▄▖▐▌  ▐▌▐▌   ▝▚▄▞▘		\
just read config.h for more info\

CC		= g++
TARGET 	= cooke_analyzer	# set this to the name of the program being compiled
SRC		= cooke_analyzer.cpp cooke_lexemes.cpp
OBJ 	= ${SRC:.cpp=.o}	# obj is all of the things in SRC but replaced with the extension of .o instead of .cpp. basically output.

all: $(TARGET)

${TARGET}: $(OBJ)
	$(CC) ${CPPFLAGS} ${CFLAGS} -o $@ $(OBJ)

clean:
	rm -f $(TARGET) $(OBJ)
/* standard libraries */
#include <fstream>			// filesystem input + output gnu library.
#include <iostream>			// standard input and output gnu library.
#include <cstring>			// cstring gnu library
#include <string>			// manipulating and readying strings
#include <cctype>			// identify characters
#include <vector>			// vectors

// cooke_analyzer.cpp
int main(int argc, char* argv[]);
std::string shortenFile(std::ifstream& fullFile);
std::vector<std::string> tokenizeString(std::string& defString);

// cooke_lexemes.cpp
const char* findToken(const char* currentLexeme);
int checkForIdent(char currentChar);
int checkForInt(char currentChar);

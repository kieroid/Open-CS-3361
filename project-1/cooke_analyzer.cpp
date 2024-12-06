// pre-load everything from the header file
#include "cooke_analyzer.h"

int main(int argc, char* argv[]) {
	if(argc < 2 || argc > 2) { // only one argument possible
		std::cout << "Please include only one file name.";
		return(1);
	}

	std::ifstream inputFile;
	inputFile.open(argv[1]); // attempt to input the file provided
	if(inputFile.is_open() != 1) { // verify the file can open
		std::cout << "The file does not exist or cannot be opened.";
		inputFile.close();
		return(2);
	} // everything past here means the file can be read.

	std::string lexemeString = shortenFile(inputFile);
	std::vector<std::string> lexemeTokens = tokenizeString(lexemeString);

	for(int i = 0; i < lexemeTokens.size(); i++) {
		const char* cLexemeToken = lexemeTokens[i].c_str();

		std::cout << "\n" << cLexemeToken << "\t" << findToken(cLexemeToken);
	}
	std::cout << "\n";
	//std::cout << lexemeString;
	inputFile.close();
	return(0); 
}

// this function turns the long file (including spaces, tabs, newlines) into a simple string containing just characters/ints/etc.
std::string shortenFile(std::ifstream& fullFile) { // string datatype
    std::string line; // current line
	std::string fullLex; // shortened
    while (getline(fullFile, line)) {
		for( int i = 0; i < line.length(); i++) {
			if(line[i] > 32) { fullLex += line[i]; } //excludes newlines, spaces, tabs, etc.
		}
    }
	return(fullLex);
}

std::vector<std::string> tokenizeString(std::string& defString) { // gosh this looks like a tumor. datatype over datatype over datatype. help me.
	// for this part, refer to https://cplusplus.com/reference/cctype/ and https://en.cppreference.com/w/cpp/language/ascii

	std::string token;
	std::vector<std::string> tokens;

	for(int currentChar = 0; currentChar <= defString.length(); currentChar++){
		if((defString[currentChar] == '[') || (defString[currentChar] == ']') || (defString[currentChar] == '?') || (defString[currentChar] == '.') || (defString[currentChar] == '\'') || (defString[currentChar] == '@') || (defString[currentChar] == ':') || (defString[currentChar] == '^') || (defString[currentChar] == '$') || (defString[currentChar] == '#') || (defString[currentChar] == ')') || (defString[currentChar] == '(') || (defString[currentChar] == ';') || (defString[currentChar] == '}') || (defString[currentChar] == '{')) {
			if(token.empty() == 0){
				tokens.push_back(token);
				token.clear();
			}

			tokens.push_back(std::string(1, defString[currentChar]));
			continue; // continue the for loop
		}
		//std::cout << defString[currentChar];
		if(token.empty()){ // if the current token is empty, store the current character in as the token
			token = defString[currentChar];
			continue; // continue the for loop
		}

		//check for characters. add to token if so. must be alphabetical or an underscore
		if(std::isalpha(token[0]) && std::isalpha(defString[currentChar])) {
			token += defString[currentChar];
			continue; // continue the for loop
		}

		//check for digits
		if(std::isdigit(token[0]) && std::isdigit(defString[currentChar])) {
			token += defString[currentChar];
			continue; // continue the for loop
		}

		if((token[0] == '&') && (defString[currentChar] == '&')){ // if the current token is empty, store the current character in as the token
			token += defString[currentChar];
			tokens.push_back(token);
			token.clear();
			continue; // continue the for loop
		}

		//check for operator
		if(std::ispunct(token[0]) && std::ispunct(defString[currentChar])) {
			token += defString[currentChar];
			continue; // continue the for loop
		}

		tokens.push_back(token);
		token.clear();
		currentChar = currentChar - 1;
	}
	return(tokens);
}

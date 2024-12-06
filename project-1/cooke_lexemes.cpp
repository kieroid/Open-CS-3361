// pre-load everything from the header file
#include "cooke_analyzer.h"
#include "config.h"

const char* findToken(const char* currentLexeme) {
	for (int i = 0; i <= (maxLexID - 1); i++) {
		// goes through each lexeme above. so when a token in the array needs to be checked, it goes through all of this
		if (strcmp(lexemeDictionary[i][0], currentLexeme) == 0) {
			return lexemeDictionary[i][1];
		}
	}
	
	// std::strlen(currentLexeme); gets the length of the lexeme provided
	int lexemeLength = std::strlen(currentLexeme);

	// V ::= a | b | ... | y | z | aV | bV | ... | yV | zV (as defined within the project rules)
	for(int i = 0; i <= (lexemeLength - 1); i++) { // i have no idea why i made two of the same loops. i dont care. if it works it works.
		if(checkForIdent(currentLexeme[i]) == 1) { break; } // check if lexeme

		//checks if it is on the last available character (if it hasn't already broke out of it)
		if(i == (lexemeLength - 1)) { return("IDENT"); }
	}

	// N ::= 0 | 1 | ... | 8 | 9 | 0N | 1N | ... | 8N | 9N (as defined within the project rules)
	for(int i = 0; i <= (lexemeLength - 1); i++) { // look at line 18.  ¯\_(ツ)_/¯
		if(checkForInt(currentLexeme[i]) == 1) { break; } // check if int

		// read line 21
		if(i == (lexemeLength - 1)) { return("INT_LIT");}
	}

	return("UNKNOWN"); // when in doubt, "UNKNOWN" all over the place
}

int checkForIdent(char currentChar) { // i had to physically loop up a table for this.
	// heres the link https://en.cppreference.com/w/cpp/language/ascii
	if (currentChar >= 97 && currentChar <= 122) { return(0); }  
	// i know its not outlined. i just wanted the option (because i thought it would be cool)
	if (currentChar >= 65 && currentChar <= 90 && allowUpperCase_IDENT == 1) 	{ return(0);} // uppercase
	if (currentChar == 95 && allowScore_IDENT == 1)  { return(0);} // underscore
	return(1); // is there a better way to do this? dude. i dont know. i dont care. i like it.
}

int checkForInt(char currentChar) { // read line 35 and 36. same thing but for ints instead of ident.
	if (currentChar >= 48 && currentChar <= 57) {return(0); }
	return(1); // read line 95. ¯\_(ツ)_/¯
}

/*
▗▄▄▄▖ ▗▄▖ ▗▄▄▖     ▗▄▄▄▖▗▖ ▗▖▗▄▄▄▖     ▗▄▄▖▗▄▄▖  ▗▄▖ ▗▄▄▄ ▗▄▄▄▖▗▄▄▖  ▗▄▄▖
▐▌   ▐▌ ▐▌▐▌ ▐▌      █  ▐▌ ▐▌▐▌       ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌  █▐▌   ▐▌ ▐▌▐▌   
▐▛▀▀▘▐▌ ▐▌▐▛▀▚▖      █  ▐▛▀▜▌▐▛▀▀▘    ▐▌▝▜▌▐▛▀▚▖▐▛▀▜▌▐▌  █▐▛▀▀▘▐▛▀▚▖ ▝▀▚▖
▐▌   ▝▚▄▞▘▐▌ ▐▌      █  ▐▌ ▐▌▐▙▄▄▖    ▝▚▄▞▘▐▌ ▐▌▐▌ ▐▌▐▙▄▄▀▐▙▄▄▖▐▌ ▐▌▗▄▄▞▘

this is a bribe. please give me an 1000 on this project.

this is probably one of the most inneficent ways to do it. i wouldn't know, though.
NO CASE STATEMENTS. NO CONSTANT ELSE-IF STATEMENTS.
does that mean it conserves memory? probably not.
but that is not why im here.

	if you wanna know how i did it, read "cooke_lexemes.cpp"
	if you wanna know the basic functions (turning the file into an array,) read "cooke_analyzer.cpp"
	and if ya wanna just look at the functions, look at "cooke_analyzer.h"
*/

// these are features that arent required for the assignment but i just wanted to test out. feel free to go crazy.
#define maxLexID 				24	// this defines the number of possible lexemes. if you wanna add more, increase this number then go to line 27.
#define allowUpperCase_IDENT	0 	// allow upper case for IDENT
#define allowScore_IDENT		0 	// allow underscore (_) for IDENT. (i forgot what this thing is called so i called it bar)

/*
	the format of the following constant goes as follows:
	
static char lexeme[][2] = {
	{ [LEXEME],	[TOKEN]			},	//0
	...
	{ [LEXEME],	[TOKEN]			}	//[ID]
}
	
	the reason of it being out of order is so that the multi-character lexemes will be identified before the single-character lexemes.
	
	the only ones that aren't defined are:
		- "V",	"IDENT"
		- "N",	"INT_LIT"
	the reason of this is that there isn't one way that these can be defined.
	the "IDENT" lexeme contains any string that contains only latin characters.
	the "INT_LIT" lexeme contains any integer that contains only arabic numerals.

	i could also have this in some sort of json or yaml file but guess what.
	I DONT CARE.
	makes it easy for everyone. just simply edit and re-compile.
	its also so easy to allow upper-case letters as well.
*/

const char* lexemeDictionary[maxLexID][2] = {
	// EQUALITY OPERATORS
	{ "==",		"EQUAL_OP"		}, //0
	{ "!=",		"NEQUAL_OP" 	}, //1
	{ "<=",		"LEQUAL_OP" 	}, //2
	{ ">=",		"GEQUAL_OP" 	}, //3
	{ "=",		"ASSIGN_OP" 	}, //4
	{ "<",		"LESSER_OP" 	}, //5
	{ ">",		"GREATER_OP" 	}, //6

	// MODIFIER OPERATORS
	{ "+",		"ADD_OP" 		}, //7
	{ "-",		"SUB_OP" 		}, //8
	{ "*",		"MULT_OP" 		}, //9
	{ "/",		"DIV_OP" 		}, //10
	{ "%",		"MOD_OP" 		}, //11
	{ ";",		"SEMICOLON" 	}, //12
	{ "{",		"OPEN_CURL" 	}, //13
	{ "}",		"CLOSE_CURL" 	}, //14

	// PARENTHESES AND BOOLEANS
	{ "(",		"OPEN_PAREN" 	}, //15
	{ ")",		"CLOSE_PAREN" 	}, //16
	{ "&&",		"BOOL_AND" 		}, //17
	{ "||",		"BOOL_OR" 		}, //18
	{ "!",		"BOOL_NOT" 		}, //19

	// INPUT, OUTPUT, IF, ELSE
	{ "input",	"KEY_IN" 		}, //20
	{ "output",	"KEY_OUT" 		}, //21
	{ "if",		"KEY_IF" 		}, //22
	{ "else",	"KEY_ELSE" 		}  //23
};

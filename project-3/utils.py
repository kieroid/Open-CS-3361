# The reason I put this in a seperate folder is because it looked like a pain in the butt.
# No way in hell I'm going to have a computer go through a bunch of if-else statements.
# Need to reduce computation. Memory doesn't matter.

rules = {
	2: # Healthy O Lookup Dictionary
	{
		16:		0, #POWER OF 2
		15:		2,
		14:		2,
		13:		2,
		12:		2,
		11:		2,
		10:		2,
		9:		1, #LESS THAN 10
		8:		0, #POWER OF 2
		7:		1,
		6:		1,
		5:		1,
		4:		0, #POWER OF 2
		3:		1,
		2:		0, #POWER OF 2
		1:		0, #POWER OF 2
		0:		1,
		-1:		1,
		-2:		1,
		-3:		1,
		-4:		1,
		-5:		1,
		-6:		1,
		-7:		1,
		-8:		1,
		-9:		1,
		-10:	1,
		-11:	1,
		-12:	1,
		-13:	1,
		-14:	1,
		-15:	1,
		-16:	1
	},
	1: # Weakened O Lookup Dictionary
	{
		16:		2,
		15:		2,
		14:		2,
		13:		2,
		12:		2,
		11:		2,
		10:		2,
		9:		2,
		8:		2, #GREATER THAN OR EQUAL TO 8
		7:		1, # |
		6:		1, # |
		5:		1, # |
		4:		1, # |- REMAINS UNCHANGED
		3:		1, # |
		2:		1, # |
		1:		1, # |
		0:		0, #LESS THAN OR EQUAL TO 0
		-1:		0,
		-2:		0,
		-3:		0,
		-4:		0,
		-5:		0,
		-6:		0,
		-7:		0,
		-8:		0,
		-9:		0,
		-10:	0,
		-11:	0,
		-12:	0,
		-13:	0,
		-14:	0,
		-15:	0,
		-16:	0
	},
	0: # Dead Lookup Dictionary
	{
		16:		0,
		15:		0,
		14:		0,
		13:		1, #IF PRIME, WEAKENED o
		12:		0,
		11:		1, #IF PRIME, WEAKENED o
		10:		0,
		9:		0,
		8:		0,
		7:		1, #IF PRIME, WEAKENED o
		6:		0,
		5:		1, #IF PRIME, WEAKENED o
		4:		0,
		3:		1, #IF PRIME, WEAKENED o
		2:		1, #IF PRIME, WEAKENED o
		1:		0,
		0:		0,
		-1:		0,
		-2:		-1, #IF ABS(PRIME), WEAKENED x
		-3:		-1, #IF ABS(PRIME), WEAKENED x
		-4:		0,
		-5:		-1, #IF ABS(PRIME), WEAKENED x
		-6:		0,
		-7:		-1, #IF ABS(PRIME), WEAKENED x
		-8:		0,
		-9:		0,
		-10:	0,
		-11:	-1, #IF ABS(PRIME), WEAKENED x
		-12:	0,
		-13:	-1, #IF ABS(PRIME), WEAKENED x
		-14:	0,
		-15:	0,
		-16:	0
	},
	-1: # Weakened X Lookup Dictionary
	{
		16:		0,
		15:		0,
		14:		0,
		13:		0,
		12:		0,
		11:		0,
		10:		0,
		9:		0,
		8:		0,
		7:		0,
		6:		0,
		5:		0,
		4:		0,
		3:		0,
		2:		0,
		1:		0, #GREATER THAN OR EQUAL TO 1
		0:		-1, # |
		-1:		-1, # |
		-2:		-1, # |
		-3:		-1, # |- REMAINS UNCHANGED
		-4:		-1, # |
		-5:		-1, # |
		-6:		-1, # |
		-7:		-1, # |
		-8:		-2, #LESS THAN OR EQUAL TO
		-9:		-2,
		-10:	-2,
		-11:	-2,
		-12:	-2,
		-13:	-2,
		-14:	-2,
		-15:	-2,
		-16:	-2
	},
	-2: # Healthy X Lookup Dictionary
	{
		16:		0, #ABS(POWER OF 2)
		15:		-1,
		14:		-1,
		13:		-1,
		12:		-1,
		11:		-1,
		10:		-1,
		9:		-1,
		8:		0, #ABS(POWER OF 2)
		7:		-1,
		6:		-1,
		5:		-1,
		4:		0, #ABS(POWER OF 2)
		3:		-1,
		2:		0, #ABS(POWER OF 2)
		1:		0, #ABS(POWER OF 2)
		0:		-1,
		-1:		0, #ABS(POWER OF 2)
		-2:		0, #ABS(POWER OF 2)
		-3:		-1,
		-4:		0, #ABS(POWER OF 2)
		-5:		-1,
		-6:		-1,
		-7:		-1,
		-8:		0, #ABS(POWER OF 2)
		-9:		-1,
		-10:	-2, #GREATER THAN -10
		-11:	-2,
		-12:	-2,
		-13:	-2,
		-14:	-2,
		-15:	-2,
		-16:	0 #ABS(POWER OF 2)
	}
}


# You may be asking how this part works.
# These are the possible different oreintations of the sums of different nodes
# EDIT: This is an edit after I've already finished this program. In the past, I found this cool site: https://neuralpatterns.io/. It reminded me of this.
nodeSumCheck = {
	-1: #ROW r = 1
	{
		-1: # COLUMN a = 1
		(
			(0,1), (1,0), (1,1)
		),
		0: # COLUMN 1 < a < N
		(
			(0,-1), (0,1), (1,-1), (1,0), (1,1)
		),
		1: # COLUMN a = N
		(
			(0,-1), (1,-1), (1,0)
		)
	},
	0: # ROW 1 < r < N
	{
		-1: # COLUMN a = 1
		(
			(-1,0), (-1,1), (0,1), (1,0), (1,1)
		),
		0: # COLUMN 1 < a < N
		(
			(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)
		),
		1: # COLUMN a = N
		(
			(-1,-1), (-1,0), (0,-1), (1,-1), (1,0)
		)
	},
	1: # ROW r = N
	{
		-1: # COLUMN a = 1
		(
			(-1,0), (-1,1), (0,1)
		),
		0: # COLUMN 1 < a < N
		(
			(-1,-1), (-1,0), (-1,1), (0,-1), (0,1)
		),
		1: # COLUMN a = N
		(
			(-1,-1), (-1,0), (0,-1)
		)
	}
}

cellToInt = {
	"O":	2,
	"o":	1,
	".":	0,
	"x":	-1,
	"X":	-2
}

intToCell = {
	2:	"O",
	1:	"o",
	0:	".",
	-1:	"x",
	-2:	"X"
}

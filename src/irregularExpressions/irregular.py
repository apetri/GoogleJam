import sys,re

#Regular expression that matches 2 syllabes block
syllabes = re.compile(r"[aeiou]([^aeiou]+)?[aeiou]")

#Regular expression that searches for a vowel
vowel = re.compile(r"[aeiou]")

#Find if a given string contains a spell or not
def isSpell(s):

	#A spell must have at least 5 vowels
	if len(s)<5:
		return False

	#Find the first chunk of 2 syllabes
	two_syllabes_found = syllabes.search(s)
	if two_syllabes_found is None:
		return False

	two_syllabes_chunk = two_syllabes_found.group()
	two_syllabes_start = two_syllabes_found.start()
	two_syllabes_end = two_syllabes_found.end()

	#We want to find the last occurence of the same chunk in the word
	two_syllabes_last = s.rfind(two_syllabes_chunk)
	
	#If there is a distinct last occurrence, find if there is another vowel sandwiched in between
	if two_syllabes_last>two_syllabes_start:
		if vowel.search(s[two_syllabes_end:two_syllabes_last]) is not None:
			return True

	#Otherwise we need to repeat with another two syllabes chunk
	return isSpell(s[two_syllabes_start+1:])


#Main execution
if __name__=="__main__":

	#Input and output filenames
	input_filename = sys.argv[1]
	output_filename = input_filename.replace(".in.",".out.")

	#Open output file
	output = file(output_filename,"w")

	#Process each line in the input
	with open(input_filename,"r") as infile:

		#Read number of test cases
		nTest = int(infile.readline().strip("\n"))

		#Cycle over test cases
		for t in range(nTest):

			word = infile.readline().strip("\n")
			if isSpell(word):
				verdict = "Spell!"
			else:
				verdict = "Nothing."

			output.write("Case #{0}: {1}\n".format(t+1,verdict))


	#Close output
	output.close()


#!/usr/bin/python
# Importing libraries
import sys
import numpy as np
  
def readFasta(filename):
#Define a function to read every line in the file.
       fh = open(filename, 'r')
       line = fh.readline()
       name = ''
       sequence = ''
       while line:
	     line = line.rstrip('\n')
             if '>' in line:
		   name = line
             else:
		   sequence = sequence + line
             line = fh.readline()
       return sequence
	   
def ranGen(inputseq):  
#Define a function to generate random sequence which based on the permutation of the sequence in the input file and print the sequence on the screen and write it in the output file.  
  ranSeq = []
  ranSeq = np.random.permutation(list(inputseq))
  newSeq = ''.join(ranSeq)  
  print newSeq
  f.write("\n")
  f.write(newSeq)
  return newSeq
  
def calFrequency(sequence):
#Define a function to calculate the frequency of all nucleotide
  a = 0
  c = 0
  g = 0
  t = 0
  
  for letter in sequence:
	if letter == 'A':
	  a += 1
	elif letter == 'C':
	  c += 1
	elif letter == 'G':
	  g += 1
	else:
	  t += 1
	  
  fa = float(a)/float(len(sequence))      
  fc = float(c)/float(len(sequence))
  fg = float(g)/float(len(sequence))
  ft = float(t)/float(len(sequence)) 
  
  return fa, fc, fg, ft
  
def calMeanAndSD(n):
#Define a function to calculate the mean and standard deviation of every nucleotide and print all information on screen and write it on the output file
   meanfa = 0
   meanfc = 0
   meanfg = 0
   meanft = 0
   sdfa = 0
   sdfc = 0
   sdfg = 0
   sdft = 0
   dataA = []
   dataC = []
   dataG = []
   dataT = []
   for i in range(0, n):
	 fa = 0
	 fc = 0
	 fg = 0
	 ft = 0
	 newSeq= ranGen(readFasta(inputfile))
	 fa, fc, fg, ft = calFrequency(newSeq)
	 dataA.append(fa)
	 dataC.append(fc)
	 dataG.append(fg)
	 dataT.append(ft)
   meanfa = np.mean(np.array(dataA))
   meanfc = np.mean(np.array(dataC))
   meanfg = np.mean(np.array(dataG))
   meanft = np.mean(np.array(dataT))
   sdfa = np.std(np.array(dataA))
   sdfc = np.std(np.array(dataC))
   sdfg = np.std(np.array(dataG))
   sdft = np.std(np.array(dataT))
   print "The mean of A is %0.4f" %meanfa
   print "The mean of C is %0.4f" %meanfc
   print "The mean of G is %0.4f" %meanfg
   print "The mean of T is %0.4f" %meanft
   print "The standard deviation of A is %f" %sdfa
   print "The standard deviation of C is %f" %sdfc
   print "The standard deviation of G is %f" %sdfg
   print "The standard deviation of T is %f" %sdft
   f.write("\nThe mean of A is %0.4f" %meanfa)
   f.write("\nThe mean of C is %0.4f" %meanfc)
   f.write("\nThe mean of G is %0.4f" %meanfg)
   f.write("\nThe mean of T is %0.4f" %meanft)
   f.write("\nThe standard deviation of A is %f" %sdfa)
   f.write("\nThe standard deviation of C is %f" %sdfc)
   f.write("\nThe standard deviation of G is %f" %sdfg)
   f.write("\nThe standard deviation of T is %f" %sdft)

if __name__=="__main__":
#Main function which execute the command line and call the functions above
  global inputfile
  if len(sys.argv) != 7:
	print "USAGE: python RANSEQ1.py -i [input_file] -n [number_of_random_sequence] -o [output_file]"
	exit(-1)
  if sys.argv[1] == "-i":
		if sys.argv[2].endswith('.fasta'):
		  inputfile = sys.argv[2]
		else:
		   print "Input should be a fasta file." 
		   exit(-1)
  else: 
		print "USAGE: python RANSEQ1.py -i [input_file] -n [number_of_random_sequence] -o [output_file]"
		exit(-1)
  if sys.argv[3] == "-n":
		n = sys.argv[4]
  else:
		print "USAGE: python RANSEQ1.py -i [input_file] -n [number_of_random_sequence] -o [output_file]"
		exit(-1)
  if sys.argv[5] == "-o":
		outputfile = sys.argv[6]
  else:
		print "USAGE: python RANSEQ1.py -i [input_file] -n [number_of_random_sequence] -o [output_file]"
		exit(-1)
		 
  global f
  f= open(outputfile, 'w')
  f.write("Random sequence permutation:")
  calMeanAndSD(int(n))		 
  print "Output file also has the same above information."
   


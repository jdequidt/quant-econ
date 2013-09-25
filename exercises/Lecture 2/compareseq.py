def compareseq1(seq_a,seq_b):
	return set(seq_a).issubset(set(seq_b))
	
print compareseq1([1,2,3],(1,2,3,4))
print compareseq1([1,2,3],(1,2))

def compareseq2(seq_a,seq_b):
	for elementa in seq_a:
		found = 0
		for elementb in seq_b:
			if elementa == elementb:
				found = 1
		if found == 0:
			return False
		
	return True
	
print compareseq2([1,2,3],(1,2,3,4))
print compareseq2([1,2,3],(1,2))

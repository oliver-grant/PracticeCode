def subsets(l):
  l_len = len(l)
  subsets = []
  for i in range(2 ** l_len):
    ret_l = []
    for j in range(l_len):
      if ( i / (2 ** j) ) % 2 == 1:
        ret_l.append(l[j])
    subsets.append(ret_l)
  print(subsets)

subsets([1,2,3,4])

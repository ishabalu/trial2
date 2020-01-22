from calc import add,sub
eng1 = 250
ind1 = 220
eng2 = 180
etot = add(eng1, eng2)
india_need = sub(etot, ind1)
ind_target = add(india_need, 1)
print("need",ind_target,"to win")


# band depth generalizes median (or centrality) to manifolds:
# https://www.tandfonline.com/doi/abs/10.1198/jcgs.2011.09224

def banddepth(r, ds, trials=100):
  rr = r[2:].values
  dds = ds.iloc[:,2:].values
  oks = 0
  for i in range(trials):
    r1 = dds[randint(0,dds.shape[0]-1),:]
    r2 = dds[randint(0,dds.shape[0]-1),:]
    #r1 = dds[1,:]
    #r2 = dds[3,:]
    if inside(rr, r1, r2): oks += 1
  return oks / trials

def inside(r, r1, r2):
  # if the curves flip the lower bound is always the min value
  lb = np.amin([r1,r2], axis=0)
  ub = np.amax([r1,r2], axis=0)
  within = np.logical_and(r >= lb, r <= ub)
  #print(within)
  # for i in range(len(r)):
    # print("%s %s %s %s" % (r[i], r1[i], r2[i], r[i] >= r1[i] and r[i] <= r2[i]))
  return np.all(within)


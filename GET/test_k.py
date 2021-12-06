import GET as g
m1=g.m_generator("m1_input.txt")
m2=g.m_generator("m2_input.txt")
print("K值：",g.K_generator(m1,m2))
print("融合M值：",g.M_generator(m1,m2))
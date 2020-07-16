op = ['+','-','*','/', '']
for i in range(1000, 9999 + 1):
    c = str(i)
    for ii in range(len(op)):
        for jj in range(len(op)):
            for kk in range(len(op)):
                var = c[3] + op[ii] + c[2] + op[jj] + c[1] + op[kk] + c[0]
                if len(var) > 4:
                    try:
                        if i == int(eval(var)):
                            print("{0} = {1}".format(var, i))
                    except:
                        var = ''
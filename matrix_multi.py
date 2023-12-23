numRL1 = []
numCL1 = []
numRL2 = []
numCL2 = []
matRV = 0

rows1 = int(input("Enter the number of rows first matrix have "))
colm1 = int(input("Enter the the number of columns first matrix have "))

for r in range(rows1):
    for c in range(colm1):
        text = "Enter first matrix row", str(r+1) ,"column", str(c+1)," value"
        numR = int(input(text))
        numCL1.append(numR)
    numRL1.append(numCL1)
    numCL1 = []


rows2 = int(input("Enter the number of rows second matrix have "))
colm2 = int(input("Enter the the number of columns second matrix have "))

if (colm1 == rows2):
    for r in range(rows2):
        for c in range(colm2):
            text = "Enter second matrix row", str(r+1) ,"column", str(c+1)," value"
            numR = int(input(text))
            numCL2.append(numR)
        numRL2.append(numCL2)
        numCL2 = []

    for r in range(rows1):
        for rr in range(colm2):
            matRV = 0
            for c in range(rows2):
                matR = numRL1[r][c]*numRL2[c][rr]
                matRV += matR
            print(r+1,"*",rr+1,matRV)
else:
    print("This is beyond matrix pay grade")

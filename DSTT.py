import numpy as np


# CAU 1:

A = np.random.randn(3,3)
B = np.random.randn(3,3)
print("A =",A)
print("B =",B)
print("A + B =",A+B) #2
print("A - B =",A-B) #3
print("A.B =",A*B) #hadamard #5
print("A*B =",A.dot(B)) #4
print("Det(A) =",np.linalg.det(A)) #6
print("A**(-1)=",np.linalg.inv(A)) #7
print("A.T =",A.T) #8
print("Moore_A =",np.linalg.pinv(A)) #9
print("Fro_A =",np.linalg.norm(A)) #10
print("L1_norm(A) =",np.linalg.norm(A[0,:])) #11
print("L2_norm(A) =",np.linalg.norm(A[1,:]))
print("A(2x2) =",A[2,2]) #12
print("2*At =",2*A) #13
print("A.T.A =",A.T.dot(A)) #14
print("trace.A =",np.trace(A)) #15

x,v = np.linalg.eig(A) #16 
print("x =",x) #x tri rieng
print("v =",v) #v vecter rieng
v_arr = np.array(v) #17
if np.linalg.det(v_arr)!=0:
    print("A co kha nang cheo hoa")
else:
    print("A khong co kha nang cheo hoa")

C = np.ones((3,3)) #18
print("C + A =",C+A)

vector = np.random.randn(3) #19
print("diag_vector =",np.diag(vector))

D = np.random.randn(4,4) #21
print("D =",D )
if np.linalg.det(D) != 0: #22
    print("D**(-1) =",np.linalg.inv(D)) 
else:
    print("D khong co matran nghich dao")
I = np.empty_like(D) #26
print("D + T =",D+I)

D = A.T.dot(B).dot(A) #24
print("D = A.T x B x A",A.T.dot(B).dot(A))
print("det(D) =",np.linalg.det(D))


# CAU 2:

A = np.array([[1,2,3],[2,3,1],[3,1,2]]) #1
B = np.array([7,4,5])
print(
    "2x+3y+z=1\n"
    "4x+y+5z=2\n"
    "3x+2y+4z=3\n"
    "A.x=B"
    )
print("x =",np.linalg.solve(A, B))





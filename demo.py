import matplotlib.pylab as py
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed(1234)
A = np.matrix(np.random.normal(size=[3,3]))
UC,EC,VTC = np.linalg.svd(A)

##############################################################
fig = py.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)

EHat = np.matrix([[1,0,0],[0,1,0],[0,0,0]])
C = UC*EHat*UC.T
X = np.matrix(np.random.multivariate_normal(np.zeros([3]),C,size=[100]))

ax.scatter(np.array(X)[:,0], np.array(X)[:,1], np.array(X)[:,2], c='r')

##############################################################
fig = py.figure(2, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)

EHat = np.matrix([[1,0,0],[0,1,0],[0,0,0.01]])
C = UC*EHat*UC.T
X = np.matrix(np.random.multivariate_normal(np.zeros([3]),C,size=[100]))

ax.scatter(np.array(X)[:,0], np.array(X)[:,1], np.array(X)[:,2], c='r')

U,E,VT = np.linalg.svd(X, full_matrices=False)
E[2] = 0
XHat = U*np.diag(E)*VT
ax.scatter(np.array(XHat)[:,0], np.array(XHat)[:,1], np.array(XHat)[:,2], c='b')

##############################################################
fig = py.figure(3, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)

EHat = np.matrix([[1,0,0],[0,0.001,0],[0,0,0.001]])
C = UC*EHat*UC.T
X = np.matrix(np.random.multivariate_normal(np.zeros([3]),C,size=[100]))

ax.scatter(np.array(X)[:,0], np.array(X)[:,1], np.array(X)[:,2], c='r')

U,E,VT = np.linalg.svd(X, full_matrices=False)
E[1] = 0
E[2] = 0
XHat = U*np.diag(E)*VT
ax.scatter(np.array(XHat)[:,0], np.array(XHat)[:,1], np.array(XHat)[:,2], c='b')

# ##############################################################
# fig = py.figure(2, figsize=(8, 6))
# ax = Axes3D(fig, elev=-150, azim=110)
#
# EHat = np.matrix([[1,0,0],[0,1,0],[0,0,0.01]])
# C = UC*EHat*UC.T
# X = np.matrix(np.random.multivariate_normal(np.zeros([3]),C,size=[100]))
#
# ax.scatter(np.array(X)[:,0], np.array(X)[:,1], np.array(X)[:,2], c='r')
#
# U,E,VT = np.linalg.svd(X, full_matrices=False)
# E[2] = 0
# XHat = U*np.diag(E)*VT
# ax.scatter(np.array(XHat)[:,0], np.array(XHat)[:,1], np.array(XHat)[:,2], c='b')
#
# ##############################################################
# fig = py.figure(3, figsize=(8, 6))
# ax = Axes3D(fig, elev=-150, azim=110)
#
# EHat = np.matrix([[1,0,0],[0,1,0],[0,0,0.07]])
# C = UC*EHat*UC.T
# X = np.matrix(np.random.multivariate_normal(np.zeros([3]),C,size=[100]))
#
# ax.scatter(np.array(X)[:,0], np.array(X)[:,1], np.array(X)[:,2], c='r')
#
# U,E,VT = np.linalg.svd(X, full_matrices=False)
# E[2] = 0
# XHat = U*np.diag(E)*VT
# ax.scatter(np.array(XHat)[:,0], np.array(XHat)[:,1], np.array(XHat)[:,2], c='b')
#
# ##############################################################
# fig = py.figure(4, figsize=(8, 6))
# ax = Axes3D(fig, elev=-150, azim=110)
#
# EHat = np.matrix([[1,0,0],[0,1,0],[0,0,0.001]])
# C = UC*EHat*UC.T
# X = np.matrix(np.random.multivariate_normal(np.zeros([3]),C,size=[100]))
# for i in range(100):
#     if np.random.uniform() > 0.95:
#         X[i,0] += np.random.uniform(-2,2)
#         X[i,1] += np.random.uniform(-2,2)
#         X[i,2] += np.random.uniform(-2,2)
#
# ax.scatter(np.array(X)[:,0], np.array(X)[:,1], np.array(X)[:,2], c='r')
#
# U,E,VT = np.linalg.svd(X, full_matrices=False)
# E[2] = 0
# XHat = U*np.diag(E)*VT
# ax.scatter(np.array(XHat)[:,0], np.array(XHat)[:,1], np.array(XHat)[:,2], c='b')
#
py.show()

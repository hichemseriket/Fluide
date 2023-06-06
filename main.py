import numpy as np
import matplotlib.pyplot as plt

# Définition des fonctions

def fonction_scalaire(x, y):
    return np.sin(x) * np.cos(y)

def fonction_vectorielle(x, y):
    return np.array([np.cos(x), -np.sin(y)])

# Grille de points pour évaluer les fonctions
x = np.linspace(-np.pi, np.pi, 1000)
y = np.linspace(-np.pi, np.pi, 1000)
X, Y = np.meshgrid(x, y)

# Calcul des valeurs des fonctions
F_scalaire = fonction_scalaire(X, Y)
F_vectorielle = fonction_vectorielle(X, Y)

# Calcul des opérations
gradient = np.gradient(F_scalaire)
divergence = np.gradient(F_vectorielle[0], axis=0) + np.gradient(F_vectorielle[1], axis=1)
rotation = np.gradient(F_vectorielle[1], axis=0) - np.gradient(F_vectorielle[0], axis=1)
laplacien = np.gradient(np.gradient(F_scalaire, axis=0), axis=1)

# Tracé des graphiques
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

axs[0, 0].imshow(gradient[0], cmap='jet')
axs[0, 0].set_title('Gradient (x-component)')
axs[0, 0].axis('off')

axs[0, 1].imshow(gradient[1], cmap='jet')
axs[0, 1].set_title('Gradient (y-component)')
axs[0, 1].axis('off')

axs[1, 0].imshow(divergence, cmap='jet')
axs[1, 0].set_title('Divergence')
axs[1, 0].axis('off')

axs[1, 1].imshow(rotation, cmap='jet')
axs[1, 1].set_title('Rotation')
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()



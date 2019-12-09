import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera


fig = plt.figure(figsize=(10,5))
camera = Camera(fig)

coin = ['Head', 'Tail']
n_samples = int(50)
n_observations = int(10**5)
snap_freq = 4000
probs = dict(zip(np.arange(n_samples), [0]*n_samples))
for max_obs in range(0, n_observations, snap_freq):
    for obs in range(max_obs):
        n_tails, n_heads = 0, 0
        for s in range(n_samples):
            outcome = np.random.choice(coin)
            if outcome == 'Head':
                n_heads += 1
        probs[n_heads] += 1
    plt.scatter(probs.keys(), probs.values(), s=4, c='gray')
    camera.snap()
anim = camera.animate(blit=True)
anim.save('../images/ctl.gif', writer='imagemagick')

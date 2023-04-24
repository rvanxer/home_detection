"""markdown
**New `meanshift`**: To speed up the performance of the clustering algorithm, 
some key redundancies in the existing implementation of 
`sklearn.cluster.MeanShift` were removed. These include:

* Removing the labeling part which involves assigning cluster labels to all the 
sample points. This is not necessary for home detection since we only care about 
the cluster center. This prevents computation of distances between the cluster 
centers and the sample points using the BallTree algorithm, which is a massive 
speedup.

* Removing the cluster merging part. Cluster merging involves absorbing smaller 
clusters in close vicinity (within radius threshold) to larger clusters. Since 
we only care about the largest cluster and the largest cluster is always 
included in this step, there is no need to perform this step.
"""
from collections import defaultdict

import numpy as np
from sklearn.neighbors import NearestNeighbors

class MeanShift():
    def __init__(
        self,
        bandwidth=None,
        seeds=None,
        bin_seeding=False,
        min_bin_freq=1,
        cluster_all=True,
        max_iter=300,
    ):
        self.bandwidth = bandwidth
        self.seeds = seeds
        self.bin_seeding = bin_seeding
        self.cluster_all = cluster_all
        self.min_bin_freq = min_bin_freq
        self.max_iter = max_iter
        self.used_mean = False

    @staticmethod
    def get_bin_seeds(X, bin_size, min_bin_freq=1):
        if bin_size == 0:
            return X

        # Bin points
        bin_sizes = defaultdict(int)
        for point in X:
            binned_point = np.round(point / bin_size)
            bin_sizes[tuple(binned_point)] += 1

        # Select only those bins as seeds which have enough members
        bin_seeds = np.array(
            [point for point, freq in bin_sizes.items() if freq >= min_bin_freq],
            dtype=np.float32,
        )
        if len(bin_seeds) == len(X):
            return X
        bin_seeds = bin_seeds * bin_size
        return bin_seeds

    @staticmethod
    def fit_single_seed(my_mean, X, nbrs, max_iter):
        # For each seed, climb gradient until convergence or max_iter
        bandwidth = nbrs.get_params()["radius"]
        stop_thresh = 1e-3 * bandwidth  # when mean has converged
        completed_iterations = 0
        while True:
            # Find mean of points within bandwidth
            i_nbrs = nbrs.radius_neighbors([my_mean], bandwidth, return_distance=False)[0]
            points_within = X[i_nbrs]
            if len(points_within) == 0:
                break  # Depending on seeding strategy this condition may occur
            my_old_mean = my_mean  # save the old mean
            my_mean = np.mean(points_within, axis=0)
            # If converged or at max_iter, adds the cluster
            if (
                np.linalg.norm(my_mean - my_old_mean) < stop_thresh
                or completed_iterations == max_iter
            ):
                break
            completed_iterations += 1
        return tuple(my_mean), len(points_within)

    def fit(self, X):
        bandwidth, seeds = self.bandwidth, self.seeds
        if seeds is None:
            if self.bin_seeding:
                seeds = MeanShift.get_bin_seeds(X, bandwidth, self.min_bin_freq)
            else:
                seeds = X

        nbrs = NearestNeighbors(radius=bandwidth, n_jobs=1).fit(X)
        all_res = [MeanShift.fit_single_seed(seed, X, nbrs, self.max_iter) 
                   for seed in seeds]
        
        # copy results in a dictionary
        center_intensity = {}
        for i in range(len(seeds)):
            if all_res[i][1]:  # i.e. len(points_within) > 0
                center_intensity[all_res[i][0]] = all_res[i][1]

        # if there's nothing near seeds, simply return mean value
        if not center_intensity:
            self.cluster_center = tuple(X.mean(axis=0))
            self.used_mean = True
            return self
        # for other cases, select only the largest cluster
        sorted_by_intensity = sorted(
            center_intensity.items(),
            key=lambda tup: (tup[1], tup[0]),
            reverse=True,
        )
        self.cluster_center = sorted_by_intensity[0][0]
        return self

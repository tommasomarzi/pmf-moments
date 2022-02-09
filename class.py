import numpy as np

class pmf:
    """
    Pmf class.
    """
    def __init__(self, probability):
        self.probability = probability
        self.n_dim = len(probability.shape)
        self.domain = np.array(probability.shape)

        self.check_normalization()
        self.first_mom = self.first_moment()

    def check_normalization(self):
        assert(np.allclose((self.probability).sum(), 1)), "The probability mass function does not sum to 1."
    
    def first_moment(self):
        idx_matrix = np.array([np.arange(0, d) for d in self.domain], dtype=object)        
        fm = [np.dot(np.sum(self.probability, axis = tuple(d2 for d2 in range(self.n_dim) if d2!=d1)), idx_matrix[d1]) for d1 in range(self.n_dim)]
        return fm
    
    def get_first_moment(self):
        return self.first_mom


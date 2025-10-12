class Solution:
    def maximumEnergy(self, energy, k):
        n = len(energy)
        for i in range(n - k - 1, -1, -1):
            energy[i] += energy[i + k]
            
        return max(energy)
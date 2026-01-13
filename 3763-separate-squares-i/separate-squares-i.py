class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        # Sort by y-coordinate (bottom edge) to enable early breaking in the loop
        squares.sort(key=lambda x: x[1])
        
        # Calculate total area and bounds
        total_area = 0
        ymin = squares[0][1]
        ymax = squares[0][1] + squares[0][2]
        
        for _, y, l in squares:
            total_area += l * l
            ymin = min(ymin, y)
            ymax = max(ymax, y + l)
            
        target = total_area / 2.0
        
        # Binary Search
        # We run for a fixed number of iterations (e.g., 60-100) or until epsilon.
        # 100 iterations on 10^9 range gives precision far beyond 10^-5.
        for _ in range(100):
            mid = (ymin + ymax) / 2.0
            current_area_below = 0
            
            for _, y, l in squares:
                # Square is completely below the line
                if y + l <= mid:
                    current_area_below += l * l
                # Square is completely above the line
                elif y >= mid:
                    # Since squares are sorted by y, all subsequent squares 
                    # are also above mid. We can break early.
                    break
                # Square is intersected by the line
                else:
                    current_area_below += l * (mid - y)
            
            if current_area_below >= target:
                ymax = mid
            else:
                ymin = mid
                
        return ymax
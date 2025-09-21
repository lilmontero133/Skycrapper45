# imports
import heapq

# code body


class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        import heapq


class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_info = {}  # food -> (cuisine, rating)
        self.cuisine_map = {}  # cuisine -> max heap [(-rating, food)]

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = [c, r]
            if c not in self.cuisine_map:
                self.cuisine_map[c] = []
            heapq.heappush(self.cuisine_map[c], (-r, f))

    def changeRating(self, food, newRating):
        cuisine, _ = self.food_info[food]
        self.food_info[food][1] = newRating
        # Push new rating into heap (lazy update)
        heapq.heappush(self.cuisine_map[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_map[cuisine]
        # Pop until top of heap matches current rating
        while heap:
            rating, food = heap[0]
            if -rating == self.food_info[food][1]:
                return food
            heapq.heappop(heap)

# ---- Test cases ----

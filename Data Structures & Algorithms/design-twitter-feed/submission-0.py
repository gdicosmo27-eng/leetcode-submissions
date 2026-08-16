
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> [count, tweeId]
        self.followMap = defaultdict(set) # userId -> followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                idx = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(min_heap, (count, tweetId, followeeId, idx - 1))
            
        while min_heap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(min_heap)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(min_heap, (count, tweetId, followeeId, idx - 1))
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)

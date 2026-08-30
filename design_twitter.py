import heapq
from collections import defaultdict


class Twitter(object):

    def __init__(self):
        self.time = 0

        # userId -> list of (time, tweetId)
        self.tweets = defaultdict(list)

        # followerId -> set of followeeIds
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        users = self.following[userId] | {userId}

        heap = []

        # Add the latest tweet of every relevant user
        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        result = []

        # Get 10 most recent tweets
        while heap and len(result) < 10:
            neg_time, tweetId, user, index = heapq.heappop(heap)

            result.append(tweetId)

            # Add the next older tweet from the same user
            if index > 0:
                index -= 1
                time, next_tweet = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, next_tweet, user, index)
                )

        return result

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

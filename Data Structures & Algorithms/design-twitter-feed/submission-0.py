from collections import defaultdict

class Twitter:

    def __init__(self):
        self.timer = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.timer))
        self.timer -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = list(self.tweets[userId])
        for f in self.follows[userId]:
            if f != userId:
                all_tweets.extend(self.tweets[f])
        all_tweets.sort(key=lambda x: x[1])
        return [t[0] for t in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
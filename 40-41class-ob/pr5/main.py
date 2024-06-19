class Comment:
    total_comments = 0

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        Comment.total_comments += 1

    def upvote(self):
        self.votes_qty += 1

    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"

    def __add__(self, other):
        return (f"{self.text} {other.text}",
                self.votes_qty + other.votes_qty)


c1 = Comment("First comment")
c1.upvote()
c2 = Comment("Second comment")
c2.upvote()

print(c1.__add__(c2))

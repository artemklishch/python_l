class Comment:
    total_comments = 0

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        Comment.total_comments += 1

    def upvote(self, value):
        self.votes_qty += value

    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"


c1 = Comment("First comment")
c2 = Comment("Second comment")
print(c1.__dict__)
print(Comment.merge_comments("Hello, ", "world"))
# print(Comment.merge_comments(c1,"Hello, ", "world")) # error
print(Comment.total_comments)  # 2
print(c1.total_comments)  # 2

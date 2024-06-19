class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self, value):
        self.votes_qty += value


comment1 = Comment("Hello")
print(comment1.__dict__)  # {'text': 'Hello', 'votes_qty': 0}
comment1.upvote(1)
print(comment1.__dict__)  # {'text': 'Hello', 'votes_qty': 1}

comment2 = Comment("Hello one more")
print(comment2.__dict__)  # {'text': 'Hello one more', 'votes_qty': 0}

print(comment1.text)  # Hello

comment1.upvote = 10

print(comment1.__dict__)  # {'text': 'Hello', 'votes_qty': 1, 'upvote': 10}
# comment1.upvote(2) # error

class Post:
    def __init__(self, _id, title, author, text):
        self._id = _id
        self._title = title
        self._author = author
        self._text = text
        
        
    @property
    def post_id(self):
        return self._id
        
        
    @property
    def data(self):
        data = {
            'id': self._id,
            'title': self._title,
            'author': self._author,
            'text': self._text
        }
        return data
        
        
class Comment(Post):
    def __init__(self, _id, title, author, text, post_id):
        Post.__init__(self, _id, title, author, text)
        self._post_id = post_id
        
        
    @property
    def data(self):
        data = {
            'id': self._id,
            'post_id': self._post_id,
            'title': self._title,
            'author': self._author,
            'text': self._text
        }
        return data
    
    
def main():
    post = Post(1, 'test post', 'user', 'This is a test post')
    comment = Comment(1, 'comment', 'user', 'This is a test comment', post.post_id)
    print(post.data)
    print(comment.data)

if __name__ == '__main__':
    main()
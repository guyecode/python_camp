import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(self.application.settings)
        self.write('Hello Tornado')


if __name__ == '__main__':
    url_patterns = [
        (r'/', MainHandler),
    ]
    app = tornado.web.Application(url_patterns, debug=True)
    app.listen(8888, address='0.0.0.0')
    tornado.ioloop.IOLoop.current().start()
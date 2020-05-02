import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RedirectHandler):
    def get(self):
        self.write("Hello, This is a python command that is running from the backend.")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
    ])

    port = 8800
    app.listen(port)
    print(f"Application is ready and listening port {port}")
    tornado.ioloop.IOLoop.current().start()
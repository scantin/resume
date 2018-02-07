import tornado.ioloop
import tornado.web
import os



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
class LinkHandler(tornado.web.RequestHandler):
    def get(self):
       self.render("link.html")

settings = {
"static_path": os.path.join(os.path.dirname(__file__), "static") 
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/link",LinkHandler)],**settings
)

if __name__ == "__main__":
    application.listen(8090)
    tornado.ioloop.IOLoop.current().start()

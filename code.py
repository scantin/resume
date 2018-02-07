import tornado.ioloop
import tornado.web
import os



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
#class MainHandler(tornado.web.RequestHandler):
#    def get(self):
#       self.render('login.html')

settings = {
"static_path": os.path.join(os.path.dirname(__file__), "static") 
}

application = tornado.web.Application([
    (r"/index", MainHandler),],**settings
)

if __name__ == "__main__":
    application.listen(8090)
    tornado.ioloop.IOLoop.current().start()

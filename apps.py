from waitress import serve
from application.simple_echo import simple_echo_app
import config as cfg

if __name__ == "__main__":
    # app.run(debug=False)
    serve(simple_echo_app, host=cfg.host, port=cfg.port, threads=cfg.threads)

from prometheus_client import Gauge, Histogram,CollectorRegistry,start_http_server,generate_latest,REGISTRY,PROCESS_COLLECTOR,PLATFORM_COLLECTOR,GC_COLLECTOR
from flask import request,Flask,Response
import random

def setup_monitoring():
  REGISTRY.unregister(PROCESS_COLLECTOR)
  REGISTRY.unregister(PLATFORM_COLLECTOR)
  REGISTRY.unregister(GC_COLLECTOR)
  myRegister = CollectorRegistry()
  global DEMO_GUAGE 
  DEMO_GUAGE = Gauge('demo_guage', 'Testing a guage',
          ['name'],registry=myRegister)

# CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
app = Flask(__name__)

# routing
@app.route('/')
def index():
  DEMO_GUAGE.labels('saqib').set(random.randint(1,100))
  a=generate_latest()
  return a
  # return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
#   print(myRegister)
#   return "Flask is up & running\n"

app.run(host="0.0.0.0")



if __name__=='main':
  setup_monitoring()
  
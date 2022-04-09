from flask import Flask
from sqlalchemy import create_engine
from healthcheck import HealthCheck
import json

app = Flask(__name__)
db_string = "postgresql://postgresadmin:admin123@postgres-svc:5432/postgresdb"
health = HealthCheck()
db = create_engine(db_string)

def nfs_check():
    db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text")
    db.execute("INSERT INTO films (title, director, year) VALUES ('Idiocracy', 'Mike Judge', '2006')")
    result_set = db.execute("SELECT * FROM films")
    return True, json.dumps([dict(r) for r in result_set])


health.add_check(nfs_check)

app.add_url_rule("/", "healthcheck", view_func=lambda: health.run())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=443)

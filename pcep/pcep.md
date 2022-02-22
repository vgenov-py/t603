https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
https://pythoninstitute.org/certification/pcep-certification-entry-level/pcep-exam-syllabus/

### Test Online PCEP

#### El objetivo de éste proyecto es crear examenes aleatorios tipo test para preparar la certificación PCEP
* Se utilizará SQLAlchemy(sqlite3)

1. User Auth mediante session
* Estructura User:
* id TEXT
* email TEXT
* pwd TEXT
* token TEXT uuid4
* grades TEXT (tuple grade)
2. Estructura Questions
* id TEXT
* Question TEXT
* Answer TEXT
3. Estructura Options
* id TEXT
* Option TEXT
* Correct BOOL

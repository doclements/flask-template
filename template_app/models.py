from template_app import db



class DemoModel(db.Model):
    hash = db.Column(db.String(32), primary_key=True)
    result = db.Column(db.String(1000))
    mime = db.Column(db.String(100))
    
    def __init__(self, _hash, result, mime):
        self.hash = _hash
        self.result = result
        self.mime = mime

    def __repr__(self):
        return'<Cached_WCPS %s : %s mime-type: %s>' % (self.hash, self.result, self.mime)

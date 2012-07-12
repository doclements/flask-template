#!/usr/bin/env python

from flaskext.script import Command, Manager

from template_app import app

manager = Manager(app)


class SyncDB(Command):
    """
    Initializes the database tables.
    """
    def run(self):
        from template_app import db
        from template_app.models import DemoModel
        print "creating database"
        db.drop_all()
        db.create_all()
        db.session.commit()
    
   
        






class Test(Command):
    """
    Runs the application's test suite.
    """
    def run(self):
        import os
        from unittest import TestLoader, TextTestRunner
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        loader = TestLoader()
        test_suite = loader.discover(cur_dir)
        runner = TextTestRunner(verbosity=2)
        runner.run(test_suite)



manager.add_command('syncdb', SyncDB())
manager.add_command('test', Test())
manager.run()

from record_location import Base, engine

msg = 'Warning! This will drop your database. Please confirm:'
shall = True if raw_input("%s (y/N) " % msg).lower() == 'y' else False

if not shall:
    print "Cancelled database drop and creation..."
else:
    print "Dropping and creating the database..."
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

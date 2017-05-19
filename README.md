# HydraExp

A small repo for understanding the Hydra to PSQL connection and how Python objects can be stored and deleted in it.

## A few details about the scripts

1. `database_setup.py` creates relations in PostgreSQL. `db_credentials` variable contains the credentials to use PostgreSQL.

2. `generator.py` contains scripts to add random generator data directly to the DB. `entries` variable specifies the number of entries to be made in each relation. `db_credentials` contains credentials for PostgreSQL.

3. `models.py` contains the definitions for the different SQL models as Python classes. Refer to design doc to see the functioning of methods.

## Api
- `/api` - API EntryPoint
- `/api/subsystems` - Returns the collection of SubSystems
- `/api/subsystem/<id>` [GET]- Return the SubSystem with the specific `id`
- `/api/subsystem/<id>` [DELETE]- Deletes the SubSystem with the specific `id`

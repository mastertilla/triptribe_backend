# Development Guide

## Alembic

To generate a new migration, run the following command:

```bash
alembic revision --autogenerate -m "migration message"
```

To apply the migration, run the following command:

```bash
alembic upgrade head
```

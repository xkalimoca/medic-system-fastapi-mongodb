from fastapi import FastAPI
from routes.user import user
from routes.consultorio import consultorio
from routes.paciente import paciente
from routes.medico import medico
from routes.cita import cita
from docs import tags_metadata

app = FastAPI(
  docs_url="/api/v2/docs",
  redoc_url="/api/v2/redocs",
  title="SWAGGER DE CRUD EN FASTAPI & MONGODB CITAS MEDICAS",
  description="",
  version="0.0.1",
  openapi_tags=tags_metadata
)

app.include_router(user)
app.include_router(consultorio)
app.include_router(paciente)
app.include_router(medico)
app.include_router(cita)

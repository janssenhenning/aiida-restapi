# -*- coding: utf-8 -*-
"""Declaration of FastAPI application."""
from fastapi import FastAPI

from aiida_restapi.graphql import main
from aiida_restapi.routers import auth, computers, groups, nodes, process, users

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)
app.include_router(computers.router)
app.include_router(nodes.router)
app.include_router(groups.router)
app.include_router(users.router)
app.include_router(process.router)
app.add_route("/graphql", main.app, name="graphql")

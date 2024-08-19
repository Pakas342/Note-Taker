from app import db
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey, DateTime, Table, Column
from typing import List
from datetime import datetime

# Associative table for Categories and Projects

project_category = Table(
    'project_category',
    db.metadata,
    Column('category_id', ForeignKey('category.id'), primary_key=True),
    Column('project_id', ForeignKey('project.id'), primary_key=True)
)

class Category(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(1000), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    projects: Mapped[List["Project"]] = relationship(secondary=project_category, back_populates="categories")
    
class Project(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(1000), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    due_date: Mapped[datetime] = mapped_column(DateTime)
    categories: Mapped[List["Category"]] = relationship(secondary=project_category, back_populates="projects")
    tasks: Mapped[List["Task"]] = relationship(back_populates="project")
    
class Task(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(1000), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    due_date: Mapped[datetime] = mapped_column(DateTime)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"))
    project: Mapped["Project"] = relationship(back_populates="tasks")
    


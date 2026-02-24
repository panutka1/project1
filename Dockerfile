FROM python:3.13
WORKDIR /app
RUN git clone https://github.com/panutka1/project1.git
WORKDIR /app/project1

RUN pip install fastapi pydantic_settings uvicorn

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

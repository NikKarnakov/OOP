FROM continuumio/miniconda3

COPY . .

RUN conda install python=3.8 pytorch cudatoolkit -c pytorch

RUN pip install -U aiogram

RUN pip install transformers tensorflow

RUN pip install python-dotenv

CMD ["python", "app.py"]
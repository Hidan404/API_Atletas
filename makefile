run:
	@uvicorn src.api_atletas.main:app --host 0.0.0.0 --port 8000 --reload --workers 1

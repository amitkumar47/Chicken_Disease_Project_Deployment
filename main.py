from src.cnnClassifier import logger 
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline 

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<")
    object_a = DataIngestionTrainingPipeline()
    object_a.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model" 

try:
    logger.info(f"*************************")
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<\n")

except Exception as e:
    logger.exception(e)
    raise e

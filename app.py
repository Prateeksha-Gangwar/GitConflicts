import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Basic Lambda handler template
    """
    logger.info(f"Event received: {json.dumps(event)}")

    try:
        # --- Your logic here ---
        result = "Lambda executed successfully"
        # ------------------------

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': result
            })
        }

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }

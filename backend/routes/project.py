"""
Routes for project creation and management.
"""

from flask import Blueprint, request, jsonify
from utils.custom_logger import CustomLogger


# Initialize constants: blueprint, loggers, etc
project_bp = Blueprint('project_bp', __name__)
LOGGER = CustomLogger(__name__, level=20, log_file="textgpt_project.log").get_logger()


@project_bp.route('/api/v1/create_new', methods=['POST'])
def create_new():
    try:
        data = request.json

        title = data.get('title')
        url = data.get('url')
        length = data.get('length')
        src_video_lang_id = data.get('source_video_language_id')

        LOGGER.info(f"{title} project created successfully!")
        return jsonify({"message": f"{title} project created successfully!"}), 201
    
    except Exception as e:
        LOGGER.error(f'Exception in new project creation API/v1/create_new: {e}')
        return jsonify({"message": "An error when creating new project"}), 500

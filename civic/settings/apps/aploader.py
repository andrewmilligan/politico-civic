import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


APLOADER_SECRET_KEY = ""
APLOADER_AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", None)
APLOADER_AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", None)
APLOADER_AWS_REGION = "us-east-1"
APLOADER_AWS_S3_BUCKET = os.getenv("ELECTIONNIGHT_AWS_S3_BUCKET")
APLOADER_AWS_S3_STATIC_ROOT = os.getenv("ELECTIONNIGHT_AWS_S3_STATIC_ROOT")
APLOADER_RESULTS_STATIC_DIR = "static_results"
STATICFILES_DIRS = [os.path.join(BASE_DIR, APLOADER_RESULTS_STATIC_DIR)]
CIVIC_TWITTER_CONSUMER_KEY = os.getenv("CIVIC_TWITTER_CONSUMER_KEY")
CIVIC_TWITTER_CONSUMER_SECRET = os.getenv("CIVIC_TWITTER_CONSUMER_SECRET")
CIVIC_TWITTER_ACCESS_TOKEN_KEY = os.getenv("CIVIC_TWITTER_ACCESS_TOKEN_KEY")
CIVIC_TWITTER_ACCESS_TOKEN_SECRET = os.getenv(
    "CIVIC_TWITTER_ACCESS_TOKEN_SECRET"
)
CIVIC_SLACK_TOKEN = os.getenv("CIVIC_SLACK_TOKEN")
APLOADER_RESULTS_DAEMON_INTERVAL = 12
APLOADER_DATABASE_UPLOAD_DAEMON_INTERVAL = 20
from utils import db_connect
engine = db_connect()

# your code here
import seaborn as sns

total_data = sns.load_dataset("flights")
total_data.head()
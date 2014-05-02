__author__ = 'fady'
import os, sys


def add_activity(type_id, name):
	d = ActivityType.objects.get_or_create(activity_type_id=type_id, activity_name=name)[0]
	return d


def populate():
	"""

	"""

	like = add_activity("like", "like")
	dislike = add_activity("dislike", "dislike")
	eaten = add_activity("eaten", "eaten")


if __name__ == '__main__':
	script_path = os.path.dirname(__file__)
	project_dir = os.path.abspath(os.path.join(script_path, '..', '..', 'fare'))
	sys.path.insert(0, project_dir)
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fare.settings')
	from dietapp.models import ActivityType

	populate()